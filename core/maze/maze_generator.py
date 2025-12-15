"""迷宫生成器模块"""

import random
from core.maze.utils import Grid
from config.constants import NodeState


class MazeGenerator:
    #随机迷宫生成器 
    @staticmethod
    def generate_random_obstacles(grid, obstacle_ratio=0.2):

        for row in grid.nodes:
            for node in row:
                if node == grid.start_node or node == grid.end_node:
                    continue
                if random.random() < obstacle_ratio:
                    node.state = NodeState.OBSTACLE
    
    @staticmethod
    def clear_obstacles(grid):
        #清除所有障碍物
        for row in grid.nodes:
            for node in row:
                if node.state == NodeState.OBSTACLE:
                    node.state = NodeState.EMPTY
    
    @staticmethod
    def generate_rooms(grid, room_count=8, room_size=8):
       #生成房间式迷宫

        MazeGenerator.clear_obstacles(grid)
        
        rooms = []
        for _ in range(room_count):
            x = random.randint(0, grid.width - room_size - 1)
            y = random.randint(0, grid.height - room_size - 1)
            rooms.append((x, y, x + room_size, y + room_size))
        
        # 用房间之外的区域作为墙
        for y in range(grid.height):
            for x in range(grid.width):
                node = grid.get_node(x, y)
                if node and node.state != NodeState.START and node.state != NodeState.END:
                    # 检查是否在某个房间内
                    in_room = False
                    for rx1, ry1, rx2, ry2 in rooms:
                        if rx1 <= x < rx2 and ry1 <= y < ry2:
                            in_room = True
                            break
                    
                    if not in_room:
                        node.state = NodeState.OBSTACLE


class DFSMazeGenerator:
    #基于DFS的迷宫生成器
    
    @staticmethod
    def generate(grid):
        # 初始化所有节点为障碍物
        for row in grid.nodes:
            for node in row:
                if node.state not in [NodeState.START, NodeState.END]:
                    node.state = NodeState.OBSTACLE
        
        # 选择起始点（奇数坐标以保持迷宫结构）
        start_x = 1
        start_y = 1
        
        # 标记为可通行
        start_node = grid.get_node(start_x, start_y)
        if start_node:
            start_node.state = NodeState.EMPTY
        
        # DFS生成迷宫
        visited = set()
        DFSMazeGenerator._dfs(grid, start_x, start_y, visited)
    
    @staticmethod
    def _dfs(grid, x, y, visited):
        """DFS递归函数"""
        visited.add((x, y))
        
        # 四个方向（距离为2的格子）
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 检查边界
            if 0 <= nx < grid.width and 0 <= ny < grid.height and (nx, ny) not in visited:
                # 打通中间的墙
                mx, my = x + dx // 2, y + dy // 2
                middle = grid.get_node(mx, my)
                if middle:
                    middle.state = NodeState.EMPTY
                
                # 打通目标格子
                target = grid.get_node(nx, ny)
                if target:
                    target.state = NodeState.EMPTY
                
                DFSMazeGenerator._dfs(grid, nx, ny, visited)
