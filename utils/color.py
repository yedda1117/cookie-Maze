"""
颜色管理模块
"""

from config.settings import COLORS

class ColorScheme:
    """颜色方案管理"""
    
    @staticmethod
    def get_color(key):
        """获取颜色值"""
        return COLORS.get(key, "#FFFFFF")
    
    @staticmethod
    def hex_to_rgb(hex_color):
        """将十六进制颜色转换为RGB元组"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(rgb):
        """将RGB元组转换为十六进制颜色"""
        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

# 预定义颜色
COLOR_BACKGROUND = ColorScheme.get_color("background")
COLOR_OBSTACLE = ColorScheme.get_color("obstacle")
COLOR_START = ColorScheme.get_color("start")
COLOR_END = ColorScheme.get_color("end")
COLOR_OPEN = ColorScheme.get_color("open")
COLOR_CLOSED = ColorScheme.get_color("closed")
COLOR_PATH = ColorScheme.get_color("path")
COLOR_GRID_LINE = ColorScheme.get_color("grid_line")
