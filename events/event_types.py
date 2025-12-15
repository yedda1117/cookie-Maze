"""
事件类型定义
"""

from enum import Enum

class EventType(Enum):
    """事件类型枚举"""
    # 节点状态变化事件
    NODE_VISITED = "node_visited"  # 节点被访问（加入开放列表）
    NODE_EXPANDED = "node_expanded"  # 节点被扩展（加入关闭列表）
    NODE_CLOSED = "node_closed"  # 节点被关闭
    
    # 路径相关事件
    PATH_FOUND = "path_found"  # 找到路径
    PATH_NOT_FOUND = "path_not_found"  # 未找到路径
    
    # 算法执行事件
    ALGORITHM_START = "algorithm_start"  # 算法开始
    ALGORITHM_STEP = "algorithm_step"  # 算法单步执行
    ALGORITHM_COMPLETE = "algorithm_complete"  # 算法完成
    ALGORITHM_RESET = "algorithm_reset"  # 算法重置
    
    # 地图相关事件
    MAP_CHANGED = "map_changed"  # 地图改变
    MAP_CLEARED = "map_cleared"  # 地图清空
    
    # 统计事件
    STATS_UPDATE = "stats_update"  # 统计信息更新
