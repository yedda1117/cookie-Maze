"""DFS算法实现"""

from core.base_algorithm import BaseAlgorithm, Node
from config.constants import NodeState


class DFS(BaseAlgorithm):
    
    def search(self):
        
        if not self.start_node or not self.end_node:
            self.logger.error("起点或终点未设置")
            return []
        
        self.reset()
        self.timer.start()
        
        # 初始化起点
        self.start_node.g = 0
        self.start_node.parent = None
        
        # 使用栈实现迭代DFS，记录每个节点是否已经扩展过
        stack = [self.start_node]
        visited = {self.start_node}
        expanded = set()  # 记录已经扩展（close）的节点
        self.post_node_visited(self.start_node)  # open S
        
        while stack:
            current = stack[-1]  # 查看栈顶但不弹出
            
            if current == self.end_node:
                self.timer.stop()
                self.elapsed_time = self.timer.elapsed()
                path = self.reconstruct_path(current)
                self.post_path_found(path, len(path) - 1)
                self.post_stats()
                self.logger.info(f"DFS找到路径，长度={len(path)-1}，访问={self.visited_count}，扩展={self.expanded_count}")
                return path
            
            # 获取未访问的邻居
            neighbors = self.grid.get_neighbors(current.x, current.y, diagonal=False)
            unvisited_neighbors = [n for n in neighbors if n not in visited]
            
            if unvisited_neighbors:
                # 有未访问的邻居，选择第一个（深度优先）
                neighbor = unvisited_neighbors[0]
                visited.add(neighbor)
                neighbor.parent = current
                neighbor.g = current.g + 1
                stack.append(neighbor)
                self.post_node_visited(neighbor)  # open neighbor
            else:
                # 没有未访问的邻居，回退（close 当前节点）
                stack.pop()
                if current not in expanded:
                    expanded.add(current)
                    self.post_node_expanded(current)  # close current（回退时才 close）
        
        self.timer.stop()
        self.elapsed_time = self.timer.elapsed()
        self.post_path_not_found()
        self.post_stats()
        self.logger.info(f"DFS未找到路径，访问={self.visited_count}，扩展={self.expanded_count}")
        return []
