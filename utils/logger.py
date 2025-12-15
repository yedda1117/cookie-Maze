"""
日志模块
"""

import logging
from config.settings import LOG_LEVEL, DEBUG_MODE

# 配置日志
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_logger(name):
    """获取日志实例"""
    return logging.getLogger(name)

# 导出主日志实例
logger = get_logger("MazeVisualizer")
