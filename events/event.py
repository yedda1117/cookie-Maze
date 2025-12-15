"""
事件类定义
"""

from events.event_types import EventType

class Event:
    """基础事件类"""
    
    def __init__(self, event_type, data=None):
        """
        初始化事件
        
        Args:
            event_type: EventType 事件类型
            data: 事件数据
        """
        self.event_type = event_type
        self.data = data or {}
    
    def __repr__(self):
        return f"Event({self.event_type}, {self.data})"


class NodeEvent(Event):
    """节点事件"""
    
    def __init__(self, event_type, x, y, **kwargs):
        super().__init__(event_type, {"x": x, "y": y, **kwargs})


class PathEvent(Event):
    """路径事件"""
    
    def __init__(self, event_type, path=None, length=0):
        super().__init__(event_type, {"path": path, "length": length})


class StatsEvent(Event):
    """统计事件"""
    
    def __init__(self, expanded_count=0, visited_count=0, elapsed_time=0):
        super().__init__(
            EventType.STATS_UPDATE,
            {
                "expanded_count": expanded_count,
                "visited_count": visited_count,
                "elapsed_time": elapsed_time,
            }
        )
