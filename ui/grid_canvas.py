"""
网格画布组件 - 使用PyQt5绘制网格
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, pyqtSignal
from config.constants import NodeState, CELL_SIZE
from utils.color import ColorScheme


class GridCanvas(QWidget):
    """网格画布，负责绘制网格和节点"""
    
    # 信号定义
    cell_clicked = pyqtSignal(int, int)  # 单元格点击事件
    cell_right_clicked = pyqtSignal(int, int)  # 右键单击事件
    
    def __init__(self, grid, parent=None):
        """
        初始化画布
        
        Args:
            grid: Grid对象
            parent: 父窗口
        """
        super().__init__(parent)
        self.grid = grid
        self.cell_size = CELL_SIZE
        self.dragging = False  # 是否正在拖动
        self.drag_mode = None  # 拖动模式（'start', 'end', 'obstacle'）
        
        # 设置窗口大小
        width = grid.width * self.cell_size
        height = grid.height * self.cell_size
        self.setFixedSize(width, height)
        
        # 设置样式
        self.setStyleSheet("background-color: white; border: 1px solid #ccc;")
    
    def paintEvent(self, event):
        """绘制事件处理"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制网格和节点
        for row in self.grid.nodes:
            for node in row:
                self.draw_cell(painter, node)
        
        # 绘制网格线
        self.draw_grid_lines(painter)
    
    def draw_cell(self, painter, node):
        """绘制单个单元格"""
        x = node.x * self.cell_size
        y = node.y * self.cell_size
        
        # 根据节点状态选择颜色
        if node.state == NodeState.START:
            color = QColor("#00FF00")  # 绿色
        elif node.state == NodeState.END:
            color = QColor("#FF0000")  # 红色
        elif node.state == NodeState.OBSTACLE:
            color = QColor("#000000")  # 黑色
        elif node.state == NodeState.PATH:
            color = QColor("#FFD700")  # 金黄色
        elif node.state == NodeState.CLOSED:
            color = QColor("#FFB6C1")  # 浅粉色
        elif node.state == NodeState.OPEN:
            color = QColor("#ADD8E6")  # 浅蓝色
        else:
            color = QColor("#FFFFFF")  # 白色
        
        painter.fillRect(x, y, self.cell_size, self.cell_size, color)
    
    def draw_grid_lines(self, painter):
        """绘制网格线"""
        pen = QPen(QColor("#E0E0E0"))
        pen.setWidth(1)
        painter.setPen(pen)
        
        # 竖线
        for x in range(self.grid.width + 1):
            painter.drawLine(
                x * self.cell_size, 0,
                x * self.cell_size, self.grid.height * self.cell_size
            )
        
        # 横线
        for y in range(self.grid.height + 1):
            painter.drawLine(
                0, y * self.cell_size,
                self.grid.width * self.cell_size, y * self.cell_size
            )
    
    def get_cell_from_pos(self, x, y):
        """从像素坐标获取网格坐标"""
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size
        
        if 0 <= grid_x < self.grid.width and 0 <= grid_y < self.grid.height:
            return grid_x, grid_y
        return None, None
    
    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            grid_x, grid_y = self.get_cell_from_pos(event.x(), event.y())
            if grid_x is not None:
                self.cell_clicked.emit(grid_x, grid_y)
                self.dragging = True
        elif event.button() == Qt.RightButton:
            grid_x, grid_y = self.get_cell_from_pos(event.x(), event.y())
            if grid_x is not None:
                self.cell_right_clicked.emit(grid_x, grid_y)
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        if self.dragging and event.buttons() == Qt.LeftButton:
            grid_x, grid_y = self.get_cell_from_pos(event.x(), event.y())
            if grid_x is not None:
                self.cell_clicked.emit(grid_x, grid_y)
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
    
    def update_cell(self, x, y):
        """更新单个单元格的显示"""
        update_x = x * self.cell_size
        update_y = y * self.cell_size
        self.update(update_x, update_y, self.cell_size, self.cell_size)
    
    def clear_canvas(self):
        """清空画布"""
        self.grid.clear()
        self.update()
