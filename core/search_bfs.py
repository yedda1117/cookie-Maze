"""BFS（广度优先搜索算法实现"""

from collections import deque
from core.base_algorithm import BaseAlgorithm, Node
from config.constants import NodeState


class BFSAlgorithm(BaseAlgorithm):
    
    
    def search(self):

        if not self.start_node or not self.end_node:
            self.logger.error("起点或终点未设置")
            return []
        
        self.reset()
        self.timer.start()
        
        # 初始化起点
        self.start_node.g = 0
        self.start_node.parent = None
        
        # 创建队列
        queue = deque([self.start_node])
        visited = {self.start_node}
        self.post_node_visited(self.start_node)
        
        while queue:
            current = queue.popleft()
            self.post_node_expanded(current)
            
            if current == self.end_node:
                self.timer.stop()
                self.elapsed_time = self.timer.elapsed()
                path = self.reconstruct_path(current)
                self.post_path_found(path, len(path) - 1)
                self.post_stats()
                self.logger.info(f"BFS找到路径，长度={len(path)-1}，访问={self.visited_count}，扩展={self.expanded_count}")
                return path
            
            for neighbor in self.grid.get_neighbors(current.x, current.y, diagonal=False):
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbor.parent = current
                    neighbor.g = current.g + 1
                    queue.append(neighbor)
                    self.post_node_visited(neighbor)

        self.timer.stop()
        self.elapsed_time = self.timer.elapsed()
        self.post_path_not_found()
        self.post_stats()
        self.logger.info(f"BFS未找到路径，访问={self.visited_count}，扩展={self.expanded_count}")
        return []
