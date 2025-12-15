"""
Dijkstra最短路径算法实现
"""

import heapq
from core.base_algorithm import BaseAlgorithm, Node
from config.constants import NodeState


class DijkstraAlgorithm(BaseAlgorithm):
    
    def __init__(self, grid, event_queue=None, diagonal=False):
        super().__init__(grid, event_queue)
        self.diagonal = diagonal
    
    def search(self):

        if not self.start_node or not self.end_node:
            self.logger.error("起点或终点未设置")
            return []
        
        self.reset()
        self.timer.start()
        
        # 初始化起点
        self.start_node.g = 0
        self.start_node.parent = None
        
        # 创建优先队列（堆）
        open_heap = [(0, id(self.start_node), self.start_node)]
        open_set = {self.start_node}
        closed_set = set()
        
        self.post_node_visited(self.start_node)
        
        while open_heap:
            g_cost, _, current = heapq.heappop(open_heap)

            if g_cost > current.g:
                continue
            
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
                    f"Dijkstra找到路径，成本={current.g}，访问={self.visited_count}，扩展={self.expanded_count}"
                )
                return path
            
            # 扩展邻接节点（只走上下左右，不走对角线）
            for neighbor in self.grid.get_neighbors(current.x, current.y, diagonal=False):
                if neighbor in closed_set:
                    continue
                
                # 计算移动代价：基础代价1 + 地形额外代价
                move_cost = 1 + neighbor.terrain_cost
                new_g = current.g + move_cost

                if new_g < neighbor.g:
                    neighbor.g = new_g
                    neighbor.parent = current

                    heapq.heappush(open_heap, (new_g, id(neighbor), neighbor))

                    if neighbor not in open_set:
                        open_set.add(neighbor)
                        self.post_node_visited(neighbor)
        
        # 未找到路径
        self.timer.stop()
        self.elapsed_time = self.timer.elapsed()
        self.post_path_not_found()
        self.post_stats()
        self.logger.info(
            f"Dijkstra未找到路径，访问={self.visited_count}，扩展={self.expanded_count}"
        )
        return []
