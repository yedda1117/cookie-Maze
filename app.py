"""
多算法路径规划可视化系统 - Flask Web应用
支持在浏览器中运行，可通过Live Share共享
"""

import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys
import os

# 添加项目路径到sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.maze.utils import Grid
from core.search_bfs import BFSAlgorithm
from core.search_dfs import DFS
from core.dijkstra import DijkstraAlgorithm
from core.astar import AStarAlgorithm
from core.maze.maze_generator import MazeGenerator, DFSMazeGenerator
from config.constants import GRID_WIDTH, GRID_HEIGHT, NodeState, HeuristicType
from events.event_queue import EventQueue
from events.event_types import EventType
from utils.logger import logger

# 创建Flask应用
app = Flask(__name__)
CORS(app)

# 全局变量
grid = Grid(GRID_WIDTH, GRID_HEIGHT)
event_queue = EventQueue()
current_algorithm = None
current_path = []


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/api/grid', methods=['GET'])
def get_grid():
    """获取网格数据"""
    grid_data = []
    for row in grid.nodes:
        row_data = []
        for node in row:
            row_data.append({
                'x': node.x,
                'y': node.y,
                'state': node.state,
                'terrain_cost': node.terrain_cost,
                'g': round(node.g, 2) if node.g != float('inf') else -1,
                'h': round(node.h, 2),
                'f': round(node.f, 2) if node.f != float('inf') else -1,
            })
        grid_data.append(row_data)
    
    return jsonify({
        'width': grid.width,
        'height': grid.height,
        'nodes': grid_data,
        'start': {'x': grid.start_node.x, 'y': grid.start_node.y} if grid.start_node else None,
        'end': {'x': grid.end_node.x, 'y': grid.end_node.y} if grid.end_node else None,
    })


@app.route('/api/set-point', methods=['POST'])
def set_point():
    """设置起点或终点"""
    data = request.json
    x = data.get('x')
    y = data.get('y')
    point_type = data.get('type')  # 'start' 或 'end' 或 'honey'
    
    if point_type == 'start':
        grid.set_start(x, y)
    elif point_type == 'end':
        grid.set_end(x, y)
    elif point_type == 'obstacle':
        grid.set_obstacle(x, y)
    elif point_type == 'honey':
        grid.set_honey(x, y)
    elif point_type == 'clear':
        grid.clear_obstacle(x, y)
    
    return jsonify({'status': 'success'})


@app.route('/api/clear-obstacles', methods=['POST'])
def clear_obstacles():
    """清除所有障碍物"""
    MazeGenerator.clear_obstacles(grid)
    return jsonify({'status': 'success'})


@app.route('/api/generate-maze', methods=['POST'])
def generate_maze():
    """生成随机迷宫"""
    data = request.json
    maze_type = data.get('type', 'random')  # 'random' 或 'dfs'
    
    if maze_type == 'dfs':
        DFSMazeGenerator.generate(grid)
    else:
        # 保留起点和终点，其他地方生成随机障碍物
        start_backup = grid.start_node
        end_backup = grid.end_node
        
        MazeGenerator.clear_obstacles(grid)
        MazeGenerator.generate_random_obstacles(grid, obstacle_ratio=0.25)
        
        grid.start_node = start_backup
        grid.end_node = end_backup
    
    return jsonify({'status': 'success'})


@app.route('/api/search', methods=['POST'])
def search():
    """执行搜索算法"""
    global current_algorithm, current_path
    
    data = request.json
    algorithm_type = data.get('algorithm', 'bfs')
    heuristic = data.get('heuristic', 'manhattan')
    
    if not grid.start_node or not grid.end_node:
        return jsonify({'status': 'error', 'message': '请先设置起点和终点'}), 400
    
    # 重置网格
    grid.reset()
    
    # 选择算法
    if algorithm_type == 'bfs':
        current_algorithm = BFSAlgorithm(grid, event_queue)
    elif algorithm_type == 'dfs':
        current_algorithm = DFS(grid, event_queue)
    elif algorithm_type == 'dijkstra':
        current_algorithm = DijkstraAlgorithm(grid, event_queue, diagonal=True)
    elif algorithm_type == 'astar':
        heuristic_map = {
            'manhattan': HeuristicType.MANHATTAN,
            'euclidean': HeuristicType.EUCLIDEAN,
            'diagonal': HeuristicType.DIAGONAL,
        }
        current_algorithm = AStarAlgorithm(
            grid, 
            event_queue, 
            heuristic=heuristic_map.get(heuristic, HeuristicType.MANHATTAN),
            diagonal=True
        )
    else:
        return jsonify({'status': 'error', 'message': '未知的算法类型'}), 400
    
    # 设置起点和终点
    current_algorithm.set_start_end(grid.start_node, grid.end_node)
    
    # 执行搜索
    current_path = current_algorithm.search()
    
    # 获取统计信息
    stats = current_algorithm.get_stats()
    
    # 获取探索步骤（用于动画）
    steps = current_algorithm.get_exploration_steps_for_visualization()
    
    # 构建路径数据（不在这里标记路径，让前端动画播放完后再标记）
    path_data = [{'x': node.x, 'y': node.y} for node in current_path] if current_path else []
    
    # 计算路径总代价（包括地形代价）
    total_cost = current_algorithm.end_node.g if current_path else 0
    
    # 调试日志
    logger.info(f"返回数据: found={current_algorithm.found}, path_length={len(current_path)}, total_cost={total_cost}, steps_count={len(steps)}")
    
    return jsonify({
        'status': 'success',
        'found': bool(current_algorithm.found and current_path),
        'path': path_data,
        'path_length': len(current_path) - 1 if current_path else 0,
        'total_cost': round(total_cost, 2) if current_path else 0,
        'steps': steps,
        'stats': stats,
    })


@app.route('/api/reset', methods=['POST'])
def reset():
    """重置网格"""
    grid.reset()
    return jsonify({'status': 'success'})


@app.route('/api/clear', methods=['POST'])
def clear():
    """清空网格"""
    grid.clear()
    return jsonify({'status': 'success'})


@app.route('/api/mark-path', methods=['POST'])
def mark_path():
    """标记路径（在动画结束后调用）"""
    data = request.json
    path_coords = data.get('path', [])
    
    # 根据坐标标记路径
    for coord in path_coords[1:-1]:  # 跳过起点和终点
        x, y = coord['x'], coord['y']
        if 0 <= x < grid.width and 0 <= y < grid.height:
            node = grid.nodes[y][x]
            if node.state not in [NodeState.START, NodeState.END]:
                node.state = NodeState.PATH
    
    return jsonify({'status': 'success'})


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取当前算法的统计信息"""
    if current_algorithm:
        return jsonify(current_algorithm.get_stats())
    else:
        return jsonify({
            'expanded_count': 0,
            'visited_count': 0,
            'elapsed_time': 0,
            'path_length': 0,
            'found': False,
        })


def run_server(debug=True, port=5000):
    """运行服务器"""
    logger.info(f"启动Web服务器: http://127.0.0.1:{port}")
    logger.info("支持Live Share共享!")
    app.run(debug=debug, port=port, host='0.0.0.0')


if __name__ == '__main__':
    run_server(debug=True, port=5000)
