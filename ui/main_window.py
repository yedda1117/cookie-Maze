"""
主窗口 - 整合所有UI组件
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

from config.constants import GRID_WIDTH, GRID_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT
from config.constants import AlgorithmType, HeuristicType, CELL_SIZE
from core.maze.utils import Grid
from core.search_bfs import BFSAlgorithm
from core.search_dfs import DFS
from core.dijkstra import DijkstraAlgorithm
from core.astar import AStarAlgorithm
from core.maze.maze_generator import MazeGenerator, DFSMazeGenerator
from events.event_queue import EventQueue
from events.event_types import EventType
from ui.grid_canvas import GridCanvas
from ui.controls import ControlPanel
from utils.logger import get_logger

logger = get_logger(__name__)


class MainWindow(QMainWindow):
    """主窗口"""
    
    def __init__(self):
        """初始化主窗口"""
        super().__init__()
        self.setWindowTitle("多算法路径规划可视化系统")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # 创建网格和事件队列
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        self.event_queue = EventQueue()
        
        # 当前算法
        self.current_algorithm = None
        self.algorithm_type = AlgorithmType.BFS
        self.heuristic_type = HeuristicType.MANHATTAN
        self.is_searching = False
        
        # 动画定时器
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.on_animation_update)
        self.animation_speed = 50
        
        # 创建UI组件
        self.canvas = GridCanvas(self.grid)
        self.control_panel = ControlPanel()
        
        # 连接信号
        self.setup_connections()
        
        # 订阅事件
        self.subscribe_events()
        
        # 创建中央窗口
        central_widget = QWidget()
        layout = QHBoxLayout()
        
        # 左侧：网格画布
        left_layout = QVBoxLayout()
        canvas_label = QLabel("网格地图")
        canvas_label.setFont(QFont("Arial", 12, QFont.Bold))
        left_layout.addWidget(canvas_label)
        left_layout.addWidget(self.canvas)
        
        # 右侧：控制面板
        layout.addLayout(left_layout, 3)
        layout.addWidget(self.control_panel, 1)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # 初始化网格（设置默认起点和终点）
        self.grid.set_start(1, 1)
        self.grid.set_end(GRID_WIDTH - 2, GRID_HEIGHT - 2)
        self.canvas.update()
    
    def setup_connections(self):
        """设置信号连接"""
        # 画布信号
        self.canvas.cell_clicked.connect(self.on_canvas_cell_clicked)
        self.canvas.cell_right_clicked.connect(self.on_canvas_cell_right_clicked)
        
        # 控制面板信号
        self.control_panel.algorithm_changed.connect(self.on_algorithm_changed)
        self.control_panel.start_search.connect(self.on_start_search)
        self.control_panel.reset_algorithm.connect(self.on_reset_algorithm)
        self.control_panel.clear_map.connect(self.on_clear_map)
        self.control_panel.generate_maze.connect(self.on_generate_maze)
        self.control_panel.speed_changed.connect(self.on_speed_changed)
    
    def subscribe_events(self):
        """订阅算法事件"""
        self.event_queue.subscribe(EventType.NODE_VISITED, self.on_node_visited)
        self.event_queue.subscribe(EventType.NODE_EXPANDED, self.on_node_expanded)
        self.event_queue.subscribe(EventType.PATH_FOUND, self.on_path_found)
        self.event_queue.subscribe(EventType.PATH_NOT_FOUND, self.on_path_not_found)
        self.event_queue.subscribe(EventType.STATS_UPDATE, self.on_stats_update)
    
    def on_canvas_cell_clicked(self, x, y):
        """网格单元格点击事件"""
        if self.is_searching:
            return
        
        # 获取节点
        node = self.grid.get_node(x, y)
        if not node:
            return
        
        # 如果点击的是起点，更新起点
        if node == self.grid.start_node:
            return
        
        # 如果点击的是终点，更新终点
        if node == self.grid.end_node:
            return
        
        # 切换障碍物状态
        if node.state == 0:  # 空格
            self.grid.set_obstacle(x, y)
        else:  # 障碍物
            self.grid.clear_obstacle(x, y)
        
        self.canvas.update_cell(x, y)
    
    def on_canvas_cell_right_clicked(self, x, y):
        """右键点击事件 - 设置起点和终点"""
        if self.is_searching:
            return
        
        node = self.grid.get_node(x, y)
        if not node:
            return
        
        # 右键切换设置起点和终点的模式
        # 实现简单方案：shift+左键设置起点，ctrl+左键设置终点
        # 这里使用右键直接循环设置
        if node.state == 2:  # 起点
            self.grid.set_end(x, y)
            old_start = self.grid.start_node
            self.grid.start_node = None
            if old_start:
                self.canvas.update_cell(old_start.x, old_start.y)
        elif node.state == 3:  # 终点
            self.grid.set_start(x, y)
            old_end = self.grid.end_node
            self.grid.end_node = None
            if old_end:
                self.canvas.update_cell(old_end.x, old_end.y)
        else:  # 其他
            # 如果没有起点，设置起点；否则设置终点
            if self.grid.start_node is None:
                self.grid.set_start(x, y)
            else:
                self.grid.set_end(x, y)
        
        self.canvas.update()
    
    def on_algorithm_changed(self, algorithm_type):
        """算法改变事件"""
        self.algorithm_type = algorithm_type
        if self.is_searching:
            self.animation_timer.stop()
            self.is_searching = False
    
    def on_start_search(self):
        """开始搜索"""
        if self.is_searching:
            return
        
        if self.grid.start_node is None or self.grid.end_node is None:
            logger.warning("请设置起点和终点")
            return
        
        # 创建算法实例
        diagonal = self.control_panel.get_diagonal_allowed()
        
        if self.algorithm_type == AlgorithmType.BFS:
            self.current_algorithm = BFSAlgorithm(self.grid, self.event_queue)
        elif self.algorithm_type == AlgorithmType.DFS:
            self.current_algorithm = DFS(self.grid, self.event_queue)
        elif self.algorithm_type == AlgorithmType.DIJKSTRA:
            self.current_algorithm = DijkstraAlgorithm(self.grid, self.event_queue, diagonal)
        elif AlgorithmType.ASTAR in self.algorithm_type:
            # 根据选择的启发式函数创建A*算法
            if "曼哈顿" in self.algorithm_type:
                heuristic = HeuristicType.MANHATTAN
            elif "欧氏" in self.algorithm_type:
                heuristic = HeuristicType.EUCLIDEAN
            elif "对角线" in self.algorithm_type:
                heuristic = HeuristicType.DIAGONAL
            else:
                heuristic = HeuristicType.MANHATTAN
            
            self.current_algorithm = AStarAlgorithm(self.grid, self.event_queue, heuristic, diagonal)
        else:
            logger.error(f"未知的算法类型: {self.algorithm_type}")
            return
        
        # 设置起点和终点
        self.current_algorithm.set_start_end(self.grid.start_node, self.grid.end_node)
        
        # 重置网格显示
        self.grid.reset()
        self.canvas.update()
        
        # 禁用按钮
        self.control_panel.start_btn.setEnabled(False)
        self.is_searching = True
        
        # 执行搜索
        self.current_algorithm.search()
        
        # 处理事件队列中的所有事件
        self.event_queue.process_all()
        
        # 启动动画定时器以显示路径
        if self.current_algorithm.found:
            self.animation_timer.start(self.animation_speed)
        
        # 重新启用按钮
        self.control_panel.start_btn.setEnabled(True)
        self.is_searching = False
    
    def on_animation_update(self):
        """动画更新"""
        # 这里可以添加路径动画显示的逻辑
        # 目前只是单次显示整个结果
        if self.current_algorithm and self.current_algorithm.found:
            # 显示最终路径
            for node in self.current_algorithm.path:
                if node != self.current_algorithm.start_node and node != self.current_algorithm.end_node:
                    from config.constants import NodeState
                    node.state = NodeState.PATH
                    self.canvas.update_cell(node.x, node.y)
        
        self.animation_timer.stop()
    
    def on_reset_algorithm(self):
        """重置算法"""
        if self.current_algorithm:
            self.current_algorithm.reset()
        else:
            self.grid.reset()
        self.canvas.update()
    
    def on_clear_map(self):
        """清空地图"""
        self.grid.clear()
        self.grid.set_start(1, 1)
        self.grid.set_end(GRID_WIDTH - 2, GRID_HEIGHT - 2)
        self.canvas.update()
    
    def on_generate_maze(self, maze_type):
        """生成迷宫"""
        self.on_clear_map()
        
        if maze_type == "random":
            ratio = self.control_panel.ratio_spinbox.value() / 100.0
            MazeGenerator.generate_random_obstacles(self.grid, ratio)
        elif maze_type == "dfs":
            DFSMazeGenerator.generate(self.grid)
        
        # 重新设置起点和终点
        self.grid.set_start(1, 1)
        self.grid.set_end(GRID_WIDTH - 2, GRID_HEIGHT - 2)
        
        self.canvas.update()
    
    def on_speed_changed(self, value):
        """速度改变事件"""
        self.animation_speed = self.control_panel.get_animation_speed()
        if self.animation_timer.isActive():
            self.animation_timer.setInterval(self.animation_speed)
    
    def on_node_visited(self, event):
        """节点被访问事件"""
        x, y = event.data["x"], event.data["y"]
        node = self.grid.get_node(x, y)
        if node and node.state not in [2, 3]:  # 不覆盖起点和终点
            from config.constants import NodeState
            node.state = NodeState.OPEN
        self.canvas.update_cell(x, y)
    
    def on_node_expanded(self, event):
        """节点被扩展事件"""
        x, y = event.data["x"], event.data["y"]
        node = self.grid.get_node(x, y)
        if node and node.state not in [2, 3]:
            from config.constants import NodeState
            node.state = NodeState.CLOSED
        self.canvas.update_cell(x, y)
    
    def on_path_found(self, event):
        """路径找到事件"""
        logger.info(f"路径找到：{event.data}")
    
    def on_path_not_found(self, event):
        """路径未找到事件"""
        logger.warning("未找到路径")
    
    def on_stats_update(self, event):
        """统计更新事件"""
        self.control_panel.update_stats(event.data)
