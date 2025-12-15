"""
迷宫生成测试
"""

import unittest
from core.maze.utils import Grid
from core.maze.maze_generator import MazeGenerator, DFSMazeGenerator
from config.constants import NodeState


class TestMazeGenerator(unittest.TestCase):
    """迷宫生成测试"""
    
    def setUp(self):
        """测试前准备"""
        self.grid = Grid(20, 20)
        self.grid.set_start(1, 1)
        self.grid.set_end(18, 18)
    
    def test_random_obstacles(self):
        """测试随机障碍物生成"""
        MazeGenerator.generate_random_obstacles(self.grid, obstacle_ratio=0.2)
        
        # 统计障碍物数量
        obstacle_count = 0
        for row in self.grid.nodes:
            for node in row:
                if node.state == NodeState.OBSTACLE:
                    obstacle_count += 1
        
        # 障碍物应该在期望数量附近
        expected_count = int(20 * 20 * 0.2)
        self.assertGreater(obstacle_count, 0)
        self.assertLess(obstacle_count, 20 * 20)
    
    def test_clear_obstacles(self):
        """测试清除障碍物"""
        MazeGenerator.generate_random_obstacles(self.grid, obstacle_ratio=0.3)
        MazeGenerator.clear_obstacles(self.grid)
        
        # 检查所有非起点终点的节点都不是障碍物
        for row in self.grid.nodes:
            for node in row:
                if node.state not in [NodeState.START, NodeState.END]:
                    self.assertNotEqual(node.state, NodeState.OBSTACLE)
    
    def test_dfs_maze(self):
        """测试DFS迷宫生成"""
        DFSMazeGenerator.generate(self.grid)
        
        # 检查迷宫中有障碍物和通路
        has_obstacle = False
        has_empty = False
        
        for row in self.grid.nodes:
            for node in row:
                if node.state == NodeState.OBSTACLE:
                    has_obstacle = True
                elif node.state == NodeState.EMPTY:
                    has_empty = True
        
        self.assertTrue(has_obstacle)
        self.assertTrue(has_empty)


if __name__ == "__main__":
    unittest.main()
