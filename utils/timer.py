"""
计时器工具
"""

import time

class Timer:
    """简单计时器类"""
    
    def __init__(self, name="Timer"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def start(self):
        """开始计时"""
        self.start_time = time.time()
    
    def stop(self):
        """停止计时"""
        self.end_time = time.time()
        return self.elapsed()
    
    def elapsed(self):
        """获取已耗时（毫秒）"""
        if self.start_time is None:
            return 0
        end = self.end_time if self.end_time else time.time()
        return (end - self.start_time) * 1000
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, *args):
        self.stop()
