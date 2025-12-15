A 同学：算法 + 迷宫生成 + 后端主流程

1.核心算法模块（Core Algorithms）

负责以下 2 个路径算法的实现与调试：

search_bfs.py — 广度优先搜索 BFS

dijkstra.py — Dijkstra 算法

2.迷宫核心支撑

maze/maze_generator.py — 迷宫生成器

maze/utils.py — Grid 网格类（包含对迷宫结构的基础支持）

3.后端主逻辑

app.py — Flask 主应用逻辑
（A 负责实现算法调用、前后端接口、事件推送）

4.配置相关

config/constants.py — 常量

config/settings.py — 配置加载



現存需要改進地方：
1.算法都有時間計算，但是在頁面中沒有顯示計時器（可以幫助對比各個算法計算時間
2.顯示的格子顏色很醜
3.隨機迷宮障礙物生成器，不能保證起點和重點中有一條順利的通路，雖然目前測試時發現均有通路，但這裡是一個需要討論的地方


可以寫進去的地方：
1.dfs迷宮和隨機迷宮的對比