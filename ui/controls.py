"""
控制面板 - 包含算法选择、参数设置等
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QSlider, QSpinBox, QGroupBox, QTableWidget, QTableWidgetItem,
    QCheckBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from config.constants import AlgorithmType, HeuristicType


class ControlPanel(QWidget):
    """控制面板"""
    
    # 信号定义
    algorithm_changed = pyqtSignal(str)  # 算法改变
    heuristic_changed = pyqtSignal(str)  # 启发式函数改变
    start_search = pyqtSignal()  # 开始搜索
    reset_algorithm = pyqtSignal()  # 重置算法
    clear_map = pyqtSignal()  # 清空地图
    generate_maze = pyqtSignal(str)  # 生成迷宫
    speed_changed = pyqtSignal(int)  # 动画速度改变
    obstacle_ratio_changed = pyqtSignal(float)  # 障碍物比例改变
    
    def __init__(self, parent=None):
        """初始化控制面板"""
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        layout = QVBoxLayout()
        
        # 算法选择
        algo_group = QGroupBox("算法选择")
        algo_layout = QVBoxLayout()
        
        algo_label = QLabel("选择算法:")
        self.algo_combo = QComboBox()
        self.algo_combo.addItems([
            AlgorithmType.BFS,
            AlgorithmType.DFS,
            AlgorithmType.DIJKSTRA,
            AlgorithmType.ASTAR_MANHATTAN,
            AlgorithmType.ASTAR_EUCLIDEAN,
            AlgorithmType.ASTAR_DIAGONAL,
        ])
        self.algo_combo.currentTextChanged.connect(self.on_algorithm_changed)
        
        algo_layout.addWidget(algo_label)
        algo_layout.addWidget(self.algo_combo)
        algo_group.setLayout(algo_layout)
        layout.addWidget(algo_group)
        
        # 搜索控制
        search_group = QGroupBox("搜索控制")
        search_layout = QVBoxLayout()
        
        self.start_btn = QPushButton("开始搜索")
        self.start_btn.clicked.connect(self.start_search.emit)
        
        self.reset_btn = QPushButton("重置")
        self.reset_btn.clicked.connect(self.reset_algorithm.emit)
        
        self.clear_btn = QPushButton("清空地图")
        self.clear_btn.clicked.connect(self.clear_map.emit)
        
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.reset_btn)
        btn_layout.addWidget(self.clear_btn)
        
        search_layout.addLayout(btn_layout)
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)
        
        # 迷宫生成
        maze_group = QGroupBox("迷宫生成")
        maze_layout = QVBoxLayout()
        
        maze_btn_layout = QHBoxLayout()
        
        self.random_maze_btn = QPushButton("随机迷宫")
        self.random_maze_btn.clicked.connect(
            lambda: self.generate_maze.emit("random")
        )
        
        self.dfs_maze_btn = QPushButton("DFS迷宫")
        self.dfs_maze_btn.clicked.connect(
            lambda: self.generate_maze.emit("dfs")
        )
        
        maze_btn_layout.addWidget(self.random_maze_btn)
        maze_btn_layout.addWidget(self.dfs_maze_btn)
        
        # 障碍物比例
        ratio_layout = QHBoxLayout()
        ratio_label = QLabel("障碍物比例:")
        self.ratio_spinbox = QSpinBox()
        self.ratio_spinbox.setRange(0, 100)
        self.ratio_spinbox.setValue(20)
        self.ratio_spinbox.setSuffix("%")
        self.ratio_spinbox.valueChanged.connect(
            lambda v: self.obstacle_ratio_changed.emit(v / 100.0)
        )
        ratio_layout.addWidget(ratio_label)
        ratio_layout.addWidget(self.ratio_spinbox)
        
        maze_layout.addLayout(maze_btn_layout)
        maze_layout.addLayout(ratio_layout)
        maze_group.setLayout(maze_layout)
        layout.addWidget(maze_group)
        
        # 动画速度
        speed_group = QGroupBox("动画速度")
        speed_layout = QVBoxLayout()
        
        speed_label = QLabel("速度 (快 → 慢):")
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setValue(50)
        self.speed_slider.valueChanged.connect(self.speed_changed.emit)
        
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_slider)
        speed_group.setLayout(speed_layout)
        layout.addWidget(speed_group)
        
        # 对角线选项
        self.diagonal_check = QCheckBox("允许对角线移动")
        self.diagonal_check.setChecked(True)
        layout.addWidget(self.diagonal_check)
        
        # 统计信息表格
        stats_group = QGroupBox("统计信息")
        stats_layout = QVBoxLayout()
        
        self.stats_table = QTableWidget()
        self.stats_table.setRowCount(5)
        self.stats_table.setColumnCount(2)
        self.stats_table.setHorizontalHeaderLabels(["指标", "值"])
        self.stats_table.setColumnWidth(0, 100)
        self.stats_table.setColumnWidth(1, 100)
        
        # 设置行标签
        labels = ["路径长度", "访问节点数", "扩展节点数", "运行时间(ms)", "是否找到"]
        for i, label in enumerate(labels):
            item = QTableWidgetItem(label)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.stats_table.setItem(i, 0, item)
        
        # 初始化值
        for i in range(5):
            item = QTableWidgetItem("0")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.stats_table.setItem(i, 1, item)
        
        stats_layout.addWidget(self.stats_table)
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        layout.addStretch()
        self.setLayout(layout)
        self.setMaximumWidth(300)
    
    def on_algorithm_changed(self, text):
        """算法改变事件处理"""
        self.algorithm_changed.emit(text)
    
    def update_stats(self, stats):
        """更新统计信息"""
        if "path_length" in stats:
            self.stats_table.item(0, 1).setText(str(stats["path_length"]))
        if "visited_count" in stats:
            self.stats_table.item(1, 1).setText(str(stats["visited_count"]))
        if "expanded_count" in stats:
            self.stats_table.item(2, 1).setText(str(stats["expanded_count"]))
        if "elapsed_time" in stats:
            self.stats_table.item(3, 1).setText(f"{stats['elapsed_time']:.2f}")
        if "found" in stats:
            self.stats_table.item(4, 1).setText("是" if stats["found"] else "否")
    
    def get_animation_speed(self):
        """获取动画速度（毫秒）"""
        # 反向映射：slider值越大，速度越慢（延迟越长）
        return (101 - self.speed_slider.value()) * 2
    
    def get_diagonal_allowed(self):
        """是否允许对角线移动"""
        return self.diagonal_check.isChecked()
