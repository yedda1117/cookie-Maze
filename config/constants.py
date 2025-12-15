"""
项目常量定义
"""

# 网格参数
GRID_WIDTH = 25  # 网格宽度（格子数）
GRID_HEIGHT = 25  # 网格高度（格子数）
CELL_SIZE = 20  # 每个格子的像素大小

# 节点状态
class NodeState:
    EMPTY = 0  # 空格
    OBSTACLE = 1  # 障碍物
    START = 2  # 起点
    END = 3  # 终点
    OPEN = 4  # 开放列表
    CLOSED = 5  # 关闭列表
    PATH = 6  # 最终路径
    HONEY = 7  # 蜂蜜地（代价地形）

# 地形代价
class TerrainCost:
    EMPTY = 0  # 普通地面（无额外代价）
    HONEY = 1  # 蜂蜜地（额外代价1）

# 算法类型
class AlgorithmType:
    BFS = "BFS"
    DFS = "DFS"
    DIJKSTRA = "Dijkstra"
    ASTAR = "A*"
    ASTAR_MANHATTAN = "A* (曼哈顿)"
    ASTAR_EUCLIDEAN = "A* (欧氏)"
    ASTAR_DIAGONAL = "A* (对角线)"

# 启发式函数类型
class HeuristicType:
    MANHATTAN = "manhattan"
    EUCLIDEAN = "euclidean"
    DIAGONAL = "diagonal"

# UI 窗口参数
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800
