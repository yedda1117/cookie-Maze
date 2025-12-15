"""
BFS和DFS算法测试
"""

import unittest
from core.maze.utils import Grid
from core.search_bfs import BFSAlgorithm
from core.search_dfs import DFS


class TestBFS(unittest.TestCase):
    """BFS算法测试"""
    
    def setUp(self):
        """测试前准备"""
        self.grid = Grid(10, 10)
        self.grid.set_start(0, 0)
        self.grid.set_end(9, 9)
    
    def test_simple_path(self):
        """测试简单路径搜索"""
        algorithm = BFSAlgorithm(self.grid)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[0], self.grid.start_node)
        self.assertEqual(path[-1], self.grid.end_node)
    
    def test_with_obstacles(self):
        """测试有障碍物的情况"""
        # 添加一些障碍物
        for i in range(5):
            self.grid.set_obstacle(5, i)
        
        algorithm = BFSAlgorithm(self.grid)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)


class TestDFS(unittest.TestCase):
    """DFS算法测试"""
    
    def setUp(self):
        """测试前准备"""
        self.grid = Grid(10, 10)
        self.grid.set_start(0, 0)
        self.grid.set_end(9, 9)
    
    def test_simple_path(self):
        """测试简单路径搜索"""
        algorithm = DFS(self.grid)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[0], self.grid.start_node)
        self.assertEqual(path[-1], self.grid.end_node)
    
    def test_with_obstacles(self):
        """测试有障碍物的情况"""
        # 添加一些障碍物
        for i in range(5):
            self.grid.set_obstacle(5, i)
        
        algorithm = DFS(self.grid)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)


if __name__ == "__main__":
    unittest.main()
