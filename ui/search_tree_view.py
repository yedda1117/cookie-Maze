"""
搜索树视图 - 用于展示算法的搜索树结构（扩展功能）
"""

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt


class SearchTreeView(QTreeWidget):
    """搜索树视图"""
    
    def __init__(self, parent=None):
        """初始化搜索树视图"""
        super().__init__(parent)
        self.setHeaderLabels(["节点", "g值", "h值", "f值"])
        self.setColumnCount(4)
    
    def add_node(self, x, y, g, h, f, parent_item=None):
        """添加节点到树中"""
        item = QTreeWidgetItem()
        item.setText(0, f"({x}, {y})")
        item.setText(1, f"{g:.2f}")
        item.setText(2, f"{h:.2f}")
        item.setText(3, f"{f:.2f}")
        
        if parent_item:
            parent_item.addChild(item)
        else:
            self.addTopLevelItem(item)
        
        return item
    
    def clear_tree(self):
        """清空树"""
        self.clear()
