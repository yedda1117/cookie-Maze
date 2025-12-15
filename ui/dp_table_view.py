"""
DP表格视图 - 用于展示动态规划表格（扩展功能）
"""

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class DPTableView(QTableWidget):
    """DP表格视图"""
    
    def __init__(self, rows=0, cols=0, parent=None):
        """初始化表格"""
        super().__init__(rows, cols, parent)
    
    def set_value(self, row, col, value):
        """设置表格值"""
        item = QTableWidgetItem(str(value))
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.setItem(row, col, item)
    
    def get_value(self, row, col):
        """获取表格值"""
        item = self.item(row, col)
        if item:
            return item.text()
        return None
