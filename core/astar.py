"""
A*启发式搜索算法实现
"""

import heapq
import math
from core.base_algorithm import BaseAlgorithm, Node
from config.constants import NodeState, HeuristicType


class AStarAlgorithm(BaseAlgorithm):
    """A*启发式搜索算法"""
    
    def __init__(self, grid, event_queue=None, heuristic=HeuristicType.MANHATTAN, diagonal=False):
        """
        初始化A*算法
        
        Args:
            grid: 网格对象
            event_queue: 事件队列
            heuristic: 启发式函数类型
            diagonal: 是否允许对角线移动
        """
        super().__init__(grid, event_queue)
        self.heuristic = heuristic
        self.diagonal = False
    
    def heuristic_cost(self, node1, node2):
        """
        计算启发式成本（估计距离）
        
        Args:
            node1: 起点
            node2: 终点
            
        Returns:
            float: 估计距离
        """
        dx = abs(node2.x - node1.x)
        dy = abs(node2.y - node1.y)
        
        if self.heuristic == HeuristicType.MANHATTAN:
            # 曼哈顿距离
            return dx + dy
        elif self.heuristic == HeuristicType.EUCLIDEAN:
            # 欧氏距离
            return math.sqrt(dx * dx + dy * dy)
        elif self.heuristic == HeuristicType.DIAGONAL:
            # 对角线距离（Chebyshev）
            return max(dx, dy)
        else:
            # 默认使用曼哈顿距离
            return dx + dy
    
    def get_distance(self, x1, y1, x2, y2):
        """
        计算实际移动距离
        
        Args:
            x1, y1: 起点坐标
            x2, y2: 终点坐标
            
        Returns:
            float: 实际距离
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        if self.diagonal:
            # 对角线移动：斜线移动cost为sqrt(2)≈1.414，水平/垂直为1
            if dx > 0 and dy > 0:
                return 1.414  # 对角线
            else:
                return 1  # 水平或垂直
        else:
            return 1
    
    def search(self):
        """
        执行A*搜索
        
        Returns:
            list: 找到的路径节点列表
        """
        if not self.start_node or not self.end_node:
            self.logger.error("起点或终点未设置")
            return []
        
        self.reset()
        self.timer.start()
        
        # 初始化起点
        self.start_node.g = 0
        self.start_node.h = self.heuristic_cost(self.start_node, self.end_node)
        self.start_node.f = self.start_node.g + self.start_node.h
        self.start_node.parent = None
        
        # 创建优先队列（堆）
        open_heap = [(self.start_node.f, id(self.start_node), self.start_node)]
        open_set = {self.start_node}
        closed_set = set()
        
        self.post_node_visited(self.start_node)
        
        while open_heap:
            f_cost, _, current = heapq.heappop(open_heap)
            
            if current in closed_set:
                continue
            
            open_set.discard(current)
            closed_set.add(current)
            self.post_node_expanded(current)
            
            # 检查是否到达终点
            if current == self.end_node:
                self.timer.stop()
                self.elapsed_time = self.timer.elapsed()
                path = self.reconstruct_path(current)
                self.post_path_found(path, current.g)
                self.post_stats()
                self.logger.info(
                    f"A*找到路径，g={current.g:.1f}，h={current.h:.1f}，f={current.f:.1f}，"
                    f"访问={self.visited_count}，扩展={self.expanded_count}"
                )
                return path
            
            # 扩展邻接节点
            for neighbor in self.grid.get_neighbors(current.x, current.y, diagonal=self.diagonal):
                if neighbor in closed_set:
                    continue
                
                # 计算新的g值：基础移动代价 + 地形额外代价
                base_cost = self.get_distance(current.x, current.y, neighbor.x, neighbor.y)
                terrain_cost = neighbor.terrain_cost
                new_g = current.g + base_cost + terrain_cost
                
                # 如果找到更好的路径，更新邻接节点
                if new_g < neighbor.g:
                    neighbor.g = new_g
                    neighbor.h = self.heuristic_cost(neighbor, self.end_node)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                    
                    if neighbor not in open_set:
                        open_set.add(neighbor)
                        heapq.heappush(open_heap, (neighbor.f, id(neighbor), neighbor))
                        self.post_node_visited(neighbor)
        
        # 未找到路径
        self.timer.stop()
        self.elapsed_time = self.timer.elapsed()
        self.post_path_not_found()
        self.post_stats()
        self.logger.info(f"A*未找到路径，访问={self.visited_count}，扩展={self.expanded_count}")
        return []
