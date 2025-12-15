"""
动画播放器 - 用于控制搜索过程的逐步动画显示（扩展功能）
"""

from PyQt5.QtCore import QTimer, pyqtSignal


class AnimationPlayer:
    """动画播放器"""
    
    def __init__(self):
        """初始化动画播放器"""
        self.timer = QTimer()
        self.steps = []
        self.current_step = 0
        self.is_playing = False
        self.speed = 100  # 毫秒
    
    def add_step(self, step_data):
        """添加动画步骤"""
        self.steps.append(step_data)
    
    def play(self):
        """播放动画"""
        if not self.is_playing and len(self.steps) > 0:
            self.is_playing = True
            self.current_step = 0
            self.timer.timeout.connect(self.next_step)
            self.timer.start(self.speed)
    
    def pause(self):
        """暂停动画"""
        if self.is_playing:
            self.is_playing = False
            self.timer.stop()
    
    def next_step(self):
        """下一步"""
        if self.current_step < len(self.steps):
            self.current_step += 1
        else:
            self.pause()
    
    def reset(self):
        """重置动画"""
        self.pause()
        self.current_step = 0
        self.steps = []
    
    def set_speed(self, speed):
        """设置播放速度"""
        self.speed = speed
        if self.is_playing:
            self.timer.setInterval(speed)
