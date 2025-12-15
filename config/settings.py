"""
项目设置和配置
"""

from config.constants import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

# 动画设置
ANIMATION_SPEED = 10  # 毫秒，越小越快
ANIMATION_SPEED_MAX = 100
ANIMATION_SPEED_MIN = 1

# 性能设置
MAX_ITERATIONS = 100000  # 最大迭代数，防止无限循环

# 启发式函数权重（仅供 A* 使用）
HEURISTIC_WEIGHT = 1.0  # 1.0为标准A*，>1.0为加权A*

# 日志设置
DEBUG_MODE = False  # 是否启用调试模式
LOG_LEVEL = "INFO"  # 日志级别

# 颜色方案
COLORS = {
    "background": "#FFFFFF",
    "grid_line": "#E0E0E0",
    "empty": "#FFFFFF",
    "obstacle": "#000000",
    "start": "#00FF00",
    "end": "#FF0000",
    "open": "#ADD8E6",  # 浅蓝色
    "closed": "#FFB6C1",  # 浅粉色
    "path": "#FFD700",  # 金黄色
}
