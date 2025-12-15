"""
网格及其操作
"""

from config.constants import NodeState
from core.base_algorithm import Node


class Grid:
    """网格类，表示迷宫/地图"""
    
    def __init__(self, width, height):
        """
        初始化网格
        
        Args:
            width: 网格宽度（列数）
            height: 网格高度（行数）
        """
        self.width = width
        self.height = height
        self.nodes = [[Node(x, y) for x in range(width)] for y in range(height)]
        self.start_node = None
        self.end_node = None
    
    def get_node(self, x, y):
        """获取指定坐标的节点"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.nodes[y][x]
        return None
    
    def set_obstacle(self, x, y):
        """设置障碍物"""
        node = self.get_node(x, y)
        if node:
            node.state = NodeState.OBSTACLE
            node.terrain_cost = 0
    
    def clear_obstacle(self, x, y):
        """清除障碍物或蜂蜜地"""
        node = self.get_node(x, y)
        if node:
            if node.state == NodeState.OBSTACLE or node.state == NodeState.HONEY:
                node.state = NodeState.EMPTY
                node.terrain_cost = 0
    
    def set_honey(self, x, y):
        """设置蜂蜜地（代价地形）"""
        node = self.get_node(x, y)
        if node and node.state not in [NodeState.START, NodeState.END, NodeState.OBSTACLE]:
            node.state = NodeState.HONEY
            node.terrain_cost = 2  # 蜂蜜地额外代价为2，总代价=1+2=3
    
    def clear_honey(self, x, y):
        """清除蜂蜜地"""
        node = self.get_node(x, y)
        if node and node.state == NodeState.HONEY:
            node.state = NodeState.EMPTY
            node.terrain_cost = 0
    
    def set_start(self, x, y):
        """设置起点"""
        # 清除旧的起点
        if self.start_node:
            self.start_node.state = NodeState.EMPTY
        
        node = self.get_node(x, y)
        if node:
            node.state = NodeState.START
            self.start_node = node
    
    def set_end(self, x, y):
        """设置终点"""
        # 清除旧的终点
        if self.end_node:
            self.end_node.state = NodeState.EMPTY
        
        node = self.get_node(x, y)
        if node:
            node.state = NodeState.END
            self.end_node = node
    
    def is_walkable(self, x, y):
        """判断节点是否可以行走（不是障碍物）"""
        node = self.get_node(x, y)
        if node is None:
            return False
        return node.state != NodeState.OBSTACLE
    
    def get_terrain_cost(self, x, y):
        """获取节点的地形代价"""
        node = self.get_node(x, y)
        if node is None:
            return 0
        return node.terrain_cost
    
    def get_neighbors(self, x, y, diagonal=True):
        """
        获取节点的邻接节点
        
        Args:
            x: 节点x坐标
            y: 节点y坐标
            diagonal: 是否包括对角线方向
            
        Returns:
            list: 邻接节点列表
        """
        neighbors = []
        
        # 4个方向（上下左右）
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        # 如果包括对角线，加入4个对角线方向
        if diagonal:
            directions.extend([(1, -1), (1, 1), (-1, 1), (-1, -1)])
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_walkable(nx, ny):
                neighbors.append(self.get_node(nx, ny))
        
        return neighbors
    
    def reset(self):
        """重置网格中的所有节点状态（保留障碍物和蜂蜜地）"""
        for row in self.nodes:
            for node in row:
                # 保留起点、终点、障碍物、蜂蜜地
                if node.state not in [NodeState.START, NodeState.END, NodeState.OBSTACLE, NodeState.HONEY]:
                    node.state = NodeState.EMPTY
                # 如果有地形代价但状态不是蜂蜜地，恢复为蜂蜜地
                elif node.terrain_cost > 0 and node.state not in [NodeState.OBSTACLE, NodeState.START, NodeState.END]:
                    node.state = NodeState.HONEY
                node.reset()
    
    def clear(self):
        """清空网格（包括障碍物和蜂蜜地）"""
        for row in self.nodes:
            for node in row:
                node.state = NodeState.EMPTY
                node.terrain_cost = 0  # 清除地形代价
                node.reset()
        self.start_node = None
        self.end_node = None
