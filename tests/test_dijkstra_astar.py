"""
Dijkstra和A*算法测试
"""

import unittest
from core.maze.utils import Grid
from core.dijkstra import DijkstraAlgorithm
from core.astar import AStarAlgorithm
from config.constants import HeuristicType


class TestDijkstra(unittest.TestCase):
    """Dijkstra算法测试"""
    
    def setUp(self):
        """测试前准备"""
        self.grid = Grid(10, 10)
        self.grid.set_start(0, 0)
        self.grid.set_end(9, 9)
    
    def test_simple_path(self):
        """测试简单路径搜索"""
        algorithm = DijkstraAlgorithm(self.grid)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[0], self.grid.start_node)
        self.assertEqual(path[-1], self.grid.end_node)


class TestAStar(unittest.TestCase):
    """A*算法测试"""
    
    def setUp(self):
        """测试前准备"""
        self.grid = Grid(10, 10)
        self.grid.set_start(0, 0)
        self.grid.set_end(9, 9)
    
    def test_manhattan_heuristic(self):
        """测试曼哈顿距离启发式"""
        algorithm = AStarAlgorithm(self.grid, heuristic=HeuristicType.MANHATTAN)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[0], self.grid.start_node)
        self.assertEqual(path[-1], self.grid.end_node)
    
    def test_euclidean_heuristic(self):
        """测试欧氏距离启发式"""
        algorithm = AStarAlgorithm(self.grid, heuristic=HeuristicType.EUCLIDEAN)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)
    
    def test_diagonal_heuristic(self):
        """测试对角线距离启发式"""
        algorithm = AStarAlgorithm(self.grid, heuristic=HeuristicType.DIAGONAL)
        path = algorithm.search()
        
        self.assertTrue(len(path) > 0)


if __name__ == "__main__":
    unittest.main()
