"""
事件流测试
"""

import unittest
from events.event import Event, NodeEvent, PathEvent, StatsEvent
from events.event_types import EventType
from events.event_queue import EventQueue


class TestEventQueue(unittest.TestCase):
    """事件队列测试"""
    
    def setUp(self):
        """测试前准备"""
        self.event_queue = EventQueue()
        self.received_events = []
    
    def callback(self, event):
        """事件回调"""
        self.received_events.append(event)
    
    def test_subscribe_and_post(self):
        """测试订阅和发布"""
        self.event_queue.subscribe(EventType.NODE_VISITED, self.callback)
        
        event = NodeEvent(EventType.NODE_VISITED, 1, 2)
        self.event_queue.post(event)
        self.event_queue.process_all()
        
        self.assertEqual(len(self.received_events), 1)
        self.assertEqual(self.received_events[0], event)
    
    def test_multiple_subscribers(self):
        """测试多个订阅者"""
        callbacks_called = []
        
        def callback1(event):
            callbacks_called.append(1)
        
        def callback2(event):
            callbacks_called.append(2)
        
        self.event_queue.subscribe(EventType.PATH_FOUND, callback1)
        self.event_queue.subscribe(EventType.PATH_FOUND, callback2)
        
        event = Event(EventType.PATH_FOUND)
        self.event_queue.post(event)
        self.event_queue.process_all()
        
        self.assertEqual(len(callbacks_called), 2)
        self.assertIn(1, callbacks_called)
        self.assertIn(2, callbacks_called)
    
    def test_unsubscribe(self):
        """测试取消订阅"""
        self.event_queue.subscribe(EventType.ALGORITHM_START, self.callback)
        self.event_queue.unsubscribe(EventType.ALGORITHM_START, self.callback)
        
        event = Event(EventType.ALGORITHM_START)
        self.event_queue.post(event)
        self.event_queue.process_all()
        
        self.assertEqual(len(self.received_events), 0)


if __name__ == "__main__":
    unittest.main()
