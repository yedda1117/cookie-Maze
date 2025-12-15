"""
事件队列模块
"""

from collections import deque
from threading import Lock
from events.event_types import EventType

class EventQueue:
    """事件队列，用于存储和分发事件"""
    
    def __init__(self):
        """初始化事件队列"""
        self._queue = deque()
        self._lock = Lock()
        self._listeners = {}  # {event_type: [callback1, callback2, ...]}
    
    def subscribe(self, event_type, callback):
        """
        订阅事件
        
        Args:
            event_type: EventType 事件类型
            callback: 回调函数，接收Event对象作为参数
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)
    
    def unsubscribe(self, event_type, callback):
        """
        取消订阅事件
        
        Args:
            event_type: EventType 事件类型
            callback: 要移除的回调函数
        """
        if event_type in self._listeners:
            try:
                self._listeners[event_type].remove(callback)
            except ValueError:
                pass
    
    def post(self, event):
        """
        发布事件
        
        Args:
            event: Event 事件对象
        """
        with self._lock:
            self._queue.append(event)
    
    def process_all(self):
        """处理队列中的所有事件"""
        with self._lock:
            while self._queue:
                event = self._queue.popleft()
                self._dispatch(event)
    
    def _dispatch(self, event):
        """
        分发事件给所有监听者
        
        Args:
            event: Event 事件对象
        """
        if event.event_type in self._listeners:
            for callback in self._listeners[event.event_type]:
                try:
                    callback(event)
                except Exception as e:
                    print(f"Error in event callback: {e}")
    
    def clear(self):
        """清空事件队列"""
        with self._lock:
            self._queue.clear()
