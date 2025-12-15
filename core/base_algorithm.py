"""
基础算法框架
"""

from abc import ABC, abstractmethod
from config.constants import NodeState
from events.event import Event, NodeEvent, PathEvent, StatsEvent
from events.event_types import EventType
from events.event_queue import EventQueue
from utils.timer import Timer
from utils.logger import get_logger

logger = get_logger(__name__)


class Node:
    """网格中的节点"""
    
    def __init__(self, x, y):
        """
        初始化节点
        
        Args:
            x: 节点的x坐标
            y: 节点的y坐标
        """
        self.x = x
        self.y = y
        self.state = NodeState.EMPTY  # 节点状态
        self.terrain_cost = 0  # 地形额外代价（0=普通地面，1=蜂蜜地）
        
        # 算法相关属性
        self.g = float('inf')  # 从起点到当前节点的距离
        self.h = 0  # 启发式估计距离
        self.f = float('inf')  # f = g + h
        self.parent = None  # 父节点，用于路径回溯
        self.visited = False  # 是否已访问
        self.closed = False  # 是否在关闭列表中
    
    def __eq__(self, other):
        """比较两个节点是否相同"""
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        """节点哈希值，用于集合和字典"""
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        """比较节点（用于优先队列），按f值排序"""
        return self.f < other.f
    
    def distance_to(self, other):
        """计算到另一个节点的欧氏距离"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def reset(self):
        """重置节点算法属性"""
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None
        self.visited = False
        self.closed = False
    
    def __repr__(self):
        return f"Node({self.x}, {self.y})"


class BaseAlgorithm(ABC):
    """所有搜索算法的基类"""
    
    def __init__(self, grid, event_queue=None):
        """
        初始化算法
        
        Args:
            grid: 网格对象（包含节点和障碍物信息）
            event_queue: 事件队列，用于通知UI更新
        """
        self.grid = grid
        self.event_queue = event_queue or EventQueue()
        self.start_node = None
        self.end_node = None
        self.path = []
        self.expanded_count = 0  # 扩展的节点数
        self.visited_count = 0  # 访问的节点数
        # 记录访问与扩展的顺序，用于前端回放
        self.visited_order = []
        self.expanded_order = []
        # 统一的探索步骤序列，按真实执行顺序记录
        # 每个步骤为 {'type': 'open'/'close', 'x': ..., 'y': ...}
        self.exploration_steps = []
        self.elapsed_time = 0  # 执行时间（毫秒）
        self.found = False  # 是否找到路径
        self.timer = Timer()
        self.logger = get_logger(self.__class__.__name__)
    
    def set_start_end(self, start_node, end_node):
        """
        设置起点和终点
        
        Args:
            start_node: 起点节点
            end_node: 终点节点
        """
        self.start_node = start_node
        self.end_node = end_node
    
    def reset(self):
        """重置算法状态"""
        self.path = []
        self.expanded_count = 0
        self.visited_count = 0
        self.visited_order = []
        self.expanded_order = []
        self.exploration_steps = []
        self.elapsed_time = 0
        self.found = False
        
        # 重置所有节点
        for row in self.grid.nodes:
            for node in row:
                if node.state not in [NodeState.START, NodeState.END, NodeState.OBSTACLE]:
                    node.state = NodeState.EMPTY
                node.reset()
        
        self.event_queue.post(Event(EventType.ALGORITHM_RESET))
    
    @abstractmethod
    def search(self):
        """
        执行搜索算法
        
        Returns:
            list: 找到的路径（节点列表），如果未找到则返回空列表
        """
        pass
    
    def reconstruct_path(self, node):
        """
        从终点回溯重构路径
        
        Args:
            node: 终点节点
            
        Returns:
            list: 从起点到终点的路径节点列表
        """
        path = []
        current = node
        while current:
            path.append(current)
            current = current.parent
        path.reverse()
        return path
    
    def post_node_visited(self, node):
        """发布节点被访问事件"""
        self.visited_count += 1
        node.visited = True
        # 记录访问顺序
        try:
            self.visited_order.append({'x': node.x, 'y': node.y})
        except Exception:
            pass
        # 记录探索步骤（打开节点）
        self.exploration_steps.append({'type': 'open', 'x': node.x, 'y': node.y})
        self.event_queue.post(NodeEvent(EventType.NODE_VISITED, node.x, node.y))
    
    def post_node_expanded(self, node):
        """发布节点被扩展事件"""
        self.expanded_count += 1
        node.closed = True
        # 记录扩展顺序
        try:
            self.expanded_order.append({'x': node.x, 'y': node.y})
        except Exception:
            pass
        # 记录探索步骤（关闭节点）
        self.exploration_steps.append({'type': 'close', 'x': node.x, 'y': node.y})
        self.event_queue.post(NodeEvent(EventType.NODE_EXPANDED, node.x, node.y))
    
    def post_path_found(self, path, length=0):
        """发布路径找到事件"""
        self.found = True
        self.path = path
        self.event_queue.post(PathEvent(EventType.PATH_FOUND, path, length))
    
    def post_path_not_found(self):
        """发布未找到路径事件"""
        self.found = False
        self.event_queue.post(Event(EventType.PATH_NOT_FOUND))
    
    def post_stats(self):
        """发布统计信息更新事件"""
        self.event_queue.post(
            StatsEvent(
                expanded_count=self.expanded_count,
                visited_count=self.visited_count,
                elapsed_time=self.elapsed_time
            )
        )
    
    def get_exploration_steps_for_visualization(self):
        """
        获取用于动画的探索步骤序列
        直接返回原始顺序（DFS 真实执行顺序：访问→蓝，弹出→粉，交错出现）
        
        Returns:
            list: 按真实执行顺序的步骤序列
        """
        return self.exploration_steps
    
    def get_stats(self):
        """
        获取算法执行统计信息
        
        Returns:
            dict: 包含统计信息的字典
        """
        return {
            "expanded_count": self.expanded_count,
            "visited_count": self.visited_count,
            "elapsed_time": self.elapsed_time,
            "path_length": len(self.path),
            "found": self.found,
        }
