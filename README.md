# 多算法路径规划可视化系统 - Web版本

这是一个基于Flask + HTML5 Canvas的网页版本的迷宫路径规划可视化系统。支持多种搜索算法和通过VS Code Live Share共享。

## 🎯 功能特性

### 🍪 新增：地形代价系统
- **饼干主题设计** - 可爱的姜饼人冒险主题
- **蜂蜜地形 🍯** - 金黄色粘稠地形，增加移动代价
- **体力值系统** - 实时显示姜饼人体力消耗
- **算法对比** - 直观展示Dijkstra/A*与BFS在代价地形上的差异

### 支持的算法
- **BFS** (广度优先搜索) - 无权图最短路径，不考虑地形代价
- **DFS** (深度优先搜索) - 递归/回溯思想
- **Dijkstra** (单源最短路) - 加权图，贪心策略，考虑地形代价
- **A*** (启发式搜索) - 支持多种启发式函数，考虑地形代价

### 启发式函数（A*专用）
- 曼哈顿距离 (Manhattan)
- 欧氏距离 (Euclidean)
- 对角线距离 (Diagonal/Chebyshev)

### 迷宫生成
- 随机障碍物生成
- DFS递归迷宫生成

### 可视化效果
- 网格绘制（支持缩放）
- 开放列表/关闭列表着色
- 最终路径高亮
- 实时统计信息展示

## 📋 项目结构

```
MazeVisualizer/
├── app.py                      # Flask应用主文件
├── main.py                     # 启动脚本
├── requirements.txt            # 依赖库
├── README.md                   # 本文件
│ 
├── config/                     # 配置模块
│   ├── __init__.py
│   ├── constants.py           # 常量定义
│   └── settings.py            # 配置文件
│
├── core/                       # 核心算法模块
│   ├── __init__.py
│   ├── base_algorithm.py      # 基础算法框架
│   ├── search_bfs.py          # BFS实现
│   ├── search_dfs.py          # DFS实现
│   ├── dijkstra.py            # Dijkstra实现
│   ├── astar.py               # A*实现
│   └── maze/
│       ├── __init__.py
│       ├── utils.py           # Grid网格类
│       └── maze_generator.py  # 迷宫生成器
│
├── events/                     # 事件系统
│   ├── __init__.py
│   ├── event.py               # 事件类定义
│   ├── event_types.py         # 事件类型枚举
│   └── event_queue.py         # 事件队列
│
├── utils/                      # 工具模块
│   ├── __init__.py
│   ├── logger.py              # 日志
│   ├── timer.py               # 计时器
│   └── color.py               # 颜色管理
│
├── templates/                  # HTML模板
│   └── index.html             # 主页面
│
└── static/                     # 静态资源
    ├── css/
    │   └── style.css          # 样式表
    └── js/
        └── app.js             # 前端脚本
```

## 🚀 快速开始

### 1. 环境准备

#### Windows
```powershell
# 创建虚拟环境
python -m venv venv
.\venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt
```

#### macOS / Linux
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 启动应用

```bash
python main.py
```

应用将在 `http://127.0.0.1:5000` 启动

### 3. 使用方法

1. **设置地图**
   - 点击"设置起点"按钮，在地图上点击绿色区域设置起点
   - 点击"设置终点"按钮，在地图上点击红色区域设置终点
   - 点击"设置障碍物"按钮，在地图上点击黑色区域设置障碍物

2. **生成迷宫**
   - 点击"随机迷宫"生成随机障碍物
   - 点击"DFS迷宫"生成结构化迷宫

3. **执行搜索**
   - 从"搜索算法"下拉菜单选择算法
   - 如果选择A*，可选择启发式函数
   - 点击"执行搜索"按钮

4. **查看结果**
   - 蓝色表示开放列表（待访问）
   - 粉红色表示关闭列表（已访问）
   - 金黄色表示最终路径
   - 右侧面板显示统计信息

## 🌐 VS Code Live Share 共享

### 方法1：直接共享端口

1. **启动应用**
   ```bash
   python main.py
   ```

2. **打开VS Code命令面板**
   - 按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac)

3. **搜索Live Share**
   - 输入 `Live Share: Share Server`
   - 选择要共享的端口 `5000`

4. **分享链接**
   - VS Code会生成一个共享链接
   - 复制链接发送给其他人
   - 他人可以通过链接在浏览器中访问

### 方法2：完整Live Share会话

1. **启动Live Share**
   - 按 `Ctrl+Shift+P`，选择 `Live Share: Start Collaboration Session`
   
2. **启动应用**
   - 在VS Code终端中运行 `python main.py`

3. **分享给他人**
   - 复制Live Share会话链接
   - 邀请其他人加入

## 📊 API文档

### 获取网格数据
```
GET /api/grid
返回: 完整的网格节点数据
```

### 设置点
```
POST /api/set-point
请求体: { x: int, y: int, type: 'start'|'end'|'obstacle'|'clear' }
```

### 清除障碍物
```
POST /api/clear-obstacles
```

### 生成迷宫
```
POST /api/generate-maze
请求体: { type: 'random'|'dfs' }
```

### 执行搜索
```
POST /api/search
请求体: { algorithm: 'bfs'|'dfs'|'dijkstra'|'astar', heuristic: 'manhattan'|'euclidean'|'diagonal' }
返回: { found: bool, path_length: int, stats: {...} }
```

### 重置/清空
```
POST /api/reset      # 重置搜索结果
POST /api/clear      # 清空整个地图
```

## 🎓 算法说明

### BFS (广度优先搜索)
- **时间复杂度**: O(V + E)
- **空间复杂度**: O(V)
- **特点**: 找到的路径长度最短（对于无权图）
- **适用**: 无权图最短路径

### DFS (深度优先搜索)
- **时间复杂度**: O(V + E)
- **空间复杂度**: O(V)
- **特点**: 使用栈实现，展示递归回溯思想
- **适用**: 路径探索、迷宫遍历

### Dijkstra
- **时间复杂度**: O((V+E)logV) - 使用优先队列
- **空间复杂度**: O(V)
- **特点**: 贪心策略，找到最短路径
- **适用**: 加权图单源最短路径

### A*
- **时间复杂度**: O((V+E)logV)
- **空间复杂度**: O(V)
- **特点**: 使用启发式函数指导搜索，比Dijkstra更高效
- **适用**: 加权图最短路径，导航系统

## 🔧 自定义配置

编辑 `config/constants.py` 和 `config/settings.py` 修改：
- 网格大小: `GRID_WIDTH`, `GRID_HEIGHT`
- 颜色方案: `COLORS` 字典
- 日志级别: `LOG_LEVEL`
- 动画速度: `ANIMATION_SPEED`

## 🐛 故障排除

### 1. 端口已被占用
```bash
# 修改启动脚本中的端口
python main.py  # 编辑app.py中的端口号
```

### 2. 无法访问网页
- 确保防火墙允许5000端口访问
- 尝试访问 `http://127.0.0.1:5000` 或 `http://localhost:5000`

### 3. Live Share连接问题
- 确保VS Code已更新
- 检查网络连接
- 在终端中手动启用Live Share: `Ctrl+Shift+P` → `Live Share: Sign In`

## 📝 项目文件说明

| 文件 | 用途 |
|------|------|
| `app.py` | Flask应用，定义API接口和路由 |
| `main.py` | 应用启动入口 |
| `core/base_algorithm.py` | Node类和BaseAlgorithm基类 |
| `core/search_bfs.py` | BFS算法实现 |
| `core/search_dfs.py` | DFS算法实现 |
| `core/dijkstra.py` | Dijkstra算法实现 |
| `core/astar.py` | A*算法实现 |
| `core/maze/utils.py` | Grid网格类 |
| `core/maze/maze_generator.py` | 迷宫生成器 |
| `events/` | 事件系统（用于UI更新） |
| `utils/` | 日志、计时、颜色工具 |
| `templates/index.html` | 主页面HTML |
| `static/css/style.css` | 页面样式 |
| `static/js/app.js` | 前端交互逻辑 |

## 💡 扩展建议

### 可以添加的功能
1. 双向BFS搜索
2. IDA*算法
3. ThetA*（对角线路径优化）
4. 保存/加载地图
5. 多个起点/终点
6. 权重编辑（不同格子不同通行成本）
7. 动画速度调节
8. 搜索步骤回放

### 性能优化
1. 使用WebWorker处理算法计算
2. 增量绘制优化
3. 缓存网格数据
4. 实现路径平滑化

## 📄 许可证

自选项目 - 数据结构与算法综合实训

## 👨‍💻 作者

综合实训小组

---

**问题反馈或建议？** 欢迎提出Issue或Pull Request！

## 核心功能

### 1. **多种路径规划算法**
- **BFS (广度优先搜索)**：无权图最短路径搜索，展示层级化搜索过程
- **DFS (深度优先搜索)**：深度优先搜索，体现递归与回溯思想
- **Dijkstra 算法**：加权图单源最短路径，采用贪心策略
- **A* 算法**：启发式搜索，支持多种启发式函数
  - 曼哈顿距离 (Manhattan Distance)
  - 欧氏距离 (Euclidean Distance)
  - 对角线距离 (Diagonal Distance)

### 2. **可视化展示**
- **动态网格地图**：50×50的可交互网格，支持自定义障碍物
- **节点状态颜色编码**：
  - 🟩 绿色：起点 (Start)
  - 🔴 红色：终点 (End)
  - 🍫 巧克力棕：障碍物 (Obstacle)
  - 🍯 金黄色：蜂蜜地 (Honey Terrain) - 新增！
  - 🔵 浅蓝色：开放列表 (Open List)
  - 🟥 浅粉色：关闭列表 (Closed List)
  - 🟨 金黄色：最终路径 (Path)
- **实时动画**：展示算法搜索过程，支持速度调节
- **体力值显示**：姜饼人体力条实时更新 - 新增！

### 3. **迷宫生成**
- **随机迷宫生成**：可调节障碍物比例（0%-100%）
- **DFS迷宫生成**：基于深度优先搜索的完美迷宫生成算法

### 4. **交互功能**
- **起点/终点设置**：点击按钮后在地图上点击设置
- **障碍物绘制**：点击按钮后在地图上点击设置
- **蜂蜜地形设置**：点击按钮后在地图上点击设置 - 新增！
- **地图清空**：一键清空所有障碍物和搜索结果
- **实时统计**：显示路径长度、总代价、访问节点数、扩展节点数、运行时间等

## 项目结构

```
MazeVisualizer/
├── main.py                          # 主程序入口
├── requirements.txt                 # 项目依赖
├── README.md                        # 项目说明文档
│
├── config/                          # 配置模块
│   ├── constants.py                 # 常量定义
│   └── settings.py                  # 设置和配置
│
├── core/                            # 核心算法模块
│   ├── base_algorithm.py            # 基础算法类和Node节点类
│   ├── search_bfs.py                # BFS算法实现
│   ├── search_dfs.py                # DFS算法实现
│   ├── dijkstra.py                  # Dijkstra算法实现
│   ├── astar.py                     # A*算法实现
│   └── maze/
│       ├── utils.py                 # Grid网格类
│       └── maze_generator.py        # 迷宫生成算法
│
├── events/                          # 事件系统模块
│   ├── event_types.py               # 事件类型定义
│   ├── event.py                     # 事件类定义
│   └── event_queue.py               # 事件队列实现
│
├── ui/                              # UI用户界面模块
│   ├── main_window.py               # 主窗口
│   ├── grid_canvas.py               # 网格画布组件
│   ├── controls.py                  # 控制面板组件
│   ├── search_tree_view.py          # 搜索树视图（扩展功能）
│   ├── dp_table_view.py             # DP表格视图（扩展功能）
│   └── animation_player.py          # 动画播放器（扩展功能）
│
├── utils/                           # 工具模块
│   ├── logger.py                    # 日志记录
│   ├── timer.py                     # 计时器
│   └── color.py                     # 颜色管理
│
└── tests/                           # 测试模块
    ├── test_bfs_dfs.py              # BFS/DFS测试
    ├── test_dijkstra_astar.py       # Dijkstra/A*测试
    ├── test_dp.py                   # 动态规划测试
    ├── test_event_flow.py           # 事件流测试
    └── test_maze_generation.py      # 迷宫生成测试
```

## 各文件的作用

### 配置模块 (config/)
| 文件 | 作用 |
|------|------|
| `constants.py` | 定义常量：网格大小、节点状态、算法类型等 |
| `settings.py` | 定义运行时设置：动画速度、颜色方案、日志级别等 |

### 核心算法模块 (core/)
| 文件 | 作用 |
|------|------|
| `base_algorithm.py` | 定义Node节点类和BaseAlgorithm基类，提供算法框架 |
| `search_bfs.py` | BFS算法实现（广度优先搜索） |
| `search_dfs.py` | DFS算法实现（深度优先搜索） |
| `dijkstra.py` | Dijkstra算法实现（加权最短路径） |
| `astar.py` | A*算法实现（启发式搜索） |
| `maze/utils.py` | Grid网格类，管理节点和障碍物 |
| `maze/maze_generator.py` | 迷宫生成算法（随机和DFS） |

### 事件系统模块 (events/)
| 文件 | 作用 |
|------|------|
| `event_types.py` | 定义所有事件类型枚举 |
| `event.py` | 定义Event事件类及其子类 |
| `event_queue.py` | 实现事件队列，支持事件订阅和分发 |

### UI模块 (ui/)
| 文件 | 作用 |
|------|------|
| `main_window.py` | 主窗口类，整合所有UI组件和事件处理 |
| `grid_canvas.py` | 网格画布，负责绘制网格和节点 |
| `controls.py` | 控制面板，包含算法选择、按钮、滑块等控件 |

### 工具模块 (utils/)
| 文件 | 作用 |
|------|------|
| `logger.py` | 日志记录功能 |
| `timer.py` | 计时器，用于统计算法执行时间 |
| `color.py` | 颜色管理，定义和转换颜色值 |

## 运行方式

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行程序
```bash
python main.py
```

### 3. 程序启动
- 系统自动创建50×50的网格
- 默认起点：左上角 (1, 1)
- 默认终点：右下角 (48, 48)

## 使用说明

### 基本操作

1. **设置障碍物**
   - 左键点击网格单元格：切换障碍物状态
   - 可拖动鼠标快速绘制多个障碍物

2. **设置起点和终点**
   - 右键点击空白单元格：设置为起点（如果还没有起点）或终点
   - 右键点击起点或终点：可以移动或移除

3. **生成迷宫**
   - 点击"随机迷宫"按钮：随机生成障碍物
   - 点击"DFS迷宫"按钮：使用DFS算法生成完美迷宫
   - 调节"障碍物比例"滑块控制随机迷宫的密度

4. **运行算法**
   - 从下拉菜单选择算法（BFS、DFS、Dijkstra、A*）
   - 对于A*算法，可选择不同的启发式函数
   - 点击"开始搜索"按钮执行搜索
   - 右侧面板显示算法执行的统计信息

5. **控制动画**
   - "速度"滑块：调节动画播放速度（快→慢）
   - "允许对角线移动"复选框：控制是否允许对角线移动
   - 点击"重置"按钮：重置当前搜索结果
   - 点击"清空地图"按钮：清除所有障碍物和搜索结果

### 统计信息
- **路径长度**：最短路径包含的节点数
- **访问节点数**：算法访问过的节点总数
- **扩展节点数**：算法扩展过的节点总数
- **运行时间**：算法执行耗时（毫秒）
- **是否找到**：算法是否找到有效路径

## 算法说明

### BFS (Breadth-First Search)
- **特点**：层级搜索，保证找到最短路径（无权图）
- **复杂度**：O(V + E)，其中V为节点数，E为边数
- **适用**：无权图，需要找最短路径

### DFS (Depth-First Search)
- **特点**：深度优先，用栈实现，体现回溯思想
- **复杂度**：O(V + E)
- **适用**：路径探索，迷宫求解

### Dijkstra
- **特点**：加权图最短路径，采用贪心策略
- **复杂度**：O((V + E) log V)，使用优先队列
- **适用**：权值非负的加权图

### A*
- **特点**：启发式搜索，结合成本和估计距离
- **公式**：f(n) = g(n) + h(n)
  - g(n)：实际成本
  - h(n)：启发式估计
- **复杂度**：O(b^d)，取决于启发式函数质量
- **适用**：已知目标位置的路径规划

## 功能扩展点

系统设计考虑了以下扩展功能，在时间允许下可以实现：

1. **更多算法**
   - 双向BFS：从起点和终点同时搜索
   - IDA*：迭代加深的A*算法
   - JPS (Jump Point Search)：优化的路径搜索

2. **高级功能**
   - 路径回放：单步展示搜索过程
   - 多算法对比：同时运行多个算法进行比较
   - 地图保存/加载：保存迷宫配置以便重复测试
   - 性能图表：绘制不同算法的效率对比图

3. **UI增强**
   - 搜索树可视化：展示算法的搜索树结构
   - 节点信息面板：显示选中节点的g、h、f值
   - 实时算法步骤显示：显示当前执行的算法步骤

4. **算法优化**
   - 更多启发式函数（如勒让德距离）
   - 路径平滑化：对搜索结果进行平滑处理
   - 权值地图：支持不同区域的移动成本不同

## 系统需求

- **Python版本**：3.7+
- **操作系统**：Windows、macOS、Linux
- **依赖库**：PyQt5

## 代码质量

项目采用以下设计原则：

1. **模块化设计**
   - 清晰的模块划分（config、core、events、ui、utils）
   - 低耦合高内聚
   - 易于维护和扩展

2. **面向对象**
   - Node类：表示网格节点
   - Grid类：表示网格地图
   - BaseAlgorithm：算法基类
   - 具体算法类：BFS、DFS、Dijkstra、A*

3. **事件驱动**
   - EventQueue：事件队列
   - EventType：事件类型枚举
   - 观察者模式：UI订阅算法事件

4. **规范编码**
   - 遵循PEP 8风格指南
   - 完整的文档字符串
   - 清晰的变量命名

## 常见问题

**Q1: 如何修改网格大小？**
A: 编辑`config/constants.py`中的`GRID_WIDTH`和`GRID_HEIGHT`常量。

**Q2: 如何修改颜色方案？**
A: 编辑`config/settings.py`中的`COLORS`字典。

**Q3: A*算法为什么比其他算法快？**
A: A*使用启发式函数指导搜索方向，减少搜索的节点数。选择好的启发式函数（如曼哈顿距离）效果最好。

**Q4: 为什么DFS找到的路径可能不是最短的？**
A: DFS是深度优先的，不保证找到最短路径。如果需要最短路径，应使用BFS或Dijkstra。

**Q5: 如何在命令行运行而不是GUI？**
A: 可以直接导入相关模块进行命令行测试，例如：
```python
from core.maze.utils import Grid
from core.search_bfs import BFSAlgorithm

grid = Grid(50, 50)
grid.set_start(1, 1)
grid.set_end(48, 48)

algorithm = BFSAlgorithm(grid)
path = algorithm.search()
print(f"Path length: {len(path)}")
```

## 测试

项目包含多个测试模块（在`tests/`目录下），用于验证各个组件的功能：

```bash
# 运行单个测试
python -m pytest tests/test_bfs_dfs.py

# 运行所有测试
python -m pytest tests/
```

## 许可证

本项目为学习项目，自由使用。

## 致谢

项目参考了多个开源路径规划项目的设计思路，在此致谢。

## 🍯 地形代价系统详解

### 设计理念

为了更好地展示Dijkstra和A*算法与BFS的区别，我们引入了**地形代价系统**，采用可爱的饼干主题：

- **主角**: 姜饼人 🍪
- **普通地面**: 奶油色，代价为0
- **蜂蜜地**: 金黄色粘稠地形，额外代价为1
- **体力值**: 初始100点，经过蜂蜜地会消耗10点

### 算法行为差异

#### BFS (广度优先搜索)
- ❌ **不考虑地形代价**
- ✅ 只保证**步数最少**
- 可能会直接穿过大量蜂蜜地
- 适合：只关心最短距离的场景

#### Dijkstra / A* 算法
- ✅ **考虑地形代价**
- ✅ 找到**总代价最低**的路径
- 会尽量避开蜂蜜地，选择绕路
- 适合：需要节省资源（体力）的场景

### 使用示例

**场景设置**：
```
起点 ━━━━━━━━━━━━━━━━━━━━ 终点
      ↓ (蜂蜜地带)
      🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯
      
绕路选项：从上方或下方绕过蜂蜜地
```

**测试步骤**：
1. 设置起点和终点
2. 在中间放置一排蜂蜜地
3. 分别用BFS和Dijkstra执行搜索
4. 对比路径选择和总代价

**预期结果**：
- BFS: 直接穿过蜂蜜地（步数少，代价高）
- Dijkstra/A*: 绕路避开蜂蜜地（步数多，代价低）

### 视觉效果

- **蜂蜜地**: 金黄色径向渐变，带有光泽高光和水珠装饰
- **体力条**: 
  - 绿色/黄色渐变：体力充足
  - 红色闪烁：体力不足（<30%）
  - 实时动画：路径播放时同步更新
- **统计面板**: 显示"总代价 🍯"指标

### 技术实现

**代价计算公式**：
```
移动代价 = 基础代价(1) + 地形额外代价(terrain_cost)
```

**Dijkstra算法**：
```python
move_cost = 1 + neighbor.terrain_cost
new_g = current.g + move_cost
```

**A*算法**：
```python
base_cost = get_distance(current, neighbor)
terrain_cost = neighbor.terrain_cost
new_g = current.g + base_cost + terrain_cost
```

### 更多信息

详细说明请参考：
- `docs/地形代价系统说明.md` - 完整功能说明
- `TEST_TERRAIN_SYSTEM.md` - 测试指南

---

**最后更新**: 2024年12月
**开发版本**: 2.0 (新增地形代价系统)
