<a id="top"></a>

<div align="center">

<div style="
  max-width: 980px;
  padding: 26px 18px;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(255,250,240,0.98), rgba(255,228,196,0.90));
  border: 1px solid rgba(139,69,19,0.22);
  box-shadow: 0 12px 34px rgba(139,69,19,0.16);
">
  <h1 style="margin: 0; color:#8B4513; letter-spacing:.4px;">
    🍪 饼干迷宫冒险 <span style="color:#B8860B;">Cookie Maze Quest</span>
  </h1>

  <p style="margin: 10px 0 0; font-size: 15px; color:#5C4033;">
    在甜蜜的饼干世界里，用算法找到通往礼物的最佳路径！
    <span style="color:#FF6B6B; font-weight:900;">✨</span>
  </p>

  <div style="margin-top: 14px;">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.8+-8B4513.svg?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Flask" src="https://img.shields.io/badge/Flask-3.0.0-DEB887.svg?style=for-the-badge&logo=flask&logoColor=white" />
    <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-ES6+-FFD700.svg?style=for-the-badge&logo=javascript&logoColor=black" />
    <img alt="Status" src="https://img.shields.io/badge/Status-Active-90EE90.svg?style=for-the-badge" />
  </div>

  <div style="margin-top: 14px; font-size: 14px;">
    <a href="#-快速开始" style="text-decoration:none; font-weight:900; color:#8B4513;">快速开始</a>
    <span style="color:#C19A6B;"> • </span>
    <a href="#-使用指南" style="text-decoration:none; font-weight:900; color:#8B4513;">使用指南</a>
    <span style="color:#C19A6B;"> • </span>
    <a href="#-四大算法" style="text-decoration:none; font-weight:900; color:#8B4513;">四大算法</a>
    <span style="color:#C19A6B;"> • </span>
    <a href="#-项目结构" style="text-decoration:none; font-weight:900; color:#8B4513;">项目结构</a>
    <span style="color:#C19A6B;"> • </span>
    <a href="#-live-share-协作" style="text-decoration:none; font-weight:900; color:#8B4513;">Live Share</a>
  </div>
</div>

<br/>

<div style="max-width: 980px; display:flex; flex-wrap: wrap; gap:10px; justify-content:center;">
  <span style="padding:7px 12px; border-radius:999px; background:rgba(144,238,144,.24); border:1px solid rgba(144,238,144,.55); color:#2f6f2f; font-weight:900;">🏠 起点：姜饼屋</span>
  <span style="padding:7px 12px; border-radius:999px; background:rgba(255,107,107,.18); border:1px solid rgba(255,107,107,.45); color:#B22222; font-weight:900;">🎁 终点：礼物</span>
  <span style="padding:7px 12px; border-radius:999px; background:rgba(139,69,19,.12); border:1px solid rgba(139,69,19,.35); color:#8B4513; font-weight:900;">🍫 障碍：巧克力墙</span>
  <span style="padding:7px 12px; border-radius:999px; background:rgba(255,179,71,.22); border:1px solid rgba(255,179,71,.52); color:#8B5A00; font-weight:900;">🍯 地形：蜂蜜</span>
</div>

</div>

<br/>

<div style="
  max-width:980px;
  margin: 0 auto;
  padding: 14px 16px;
  border-radius: 16px;
  background: rgba(255,250,240,0.55);
  border: 1px dashed rgba(139,69,19,0.25);
">
  <b style="color:#8B4513;">📸 演示截图 / 动图（可选）</b>
  <div style="color:#5C4033; margin-top:6px;">
    把截图/动图放到 <code>docs/assets/</code>，然后在这里引用：<code>![demo](docs/assets/demo.gif)</code>
  </div>
</div>

<hr/>

## 🌟 项目简介

<div style="display:flex; flex-wrap:wrap; gap:14px; margin-top:10px;">

<div style="flex:1; min-width:280px; padding:14px 16px; border-radius:14px; background:rgba(255,250,240,.70); border:1px solid rgba(139,69,19,.18);">
  <h3 style="margin:0 0 8px; color:#8B4513;">🍪 甜点世界设定</h3>
  <ul style="margin:0; padding-left:18px; color:#5C4033;">
    <li><b style="color:#2f6f2f;">🏠 从姜饼屋出发</b>（薄荷绿起点）</li>
    <li><b style="color:#B22222;">🎁 寻找圣诞礼物</b>（草莓红终点）</li>
    <li><b style="color:#8B4513;">🍫 避开巧克力墙</b>（深棕色障碍）</li>
    <li><b style="color:#8B5A00;">🍯 穿越蜂蜜地</b>（更高代价/体力消耗）</li>
    <li><b style="color:#B8860B;">🍪 饼干地面</b>（普通通行）</li>
  </ul>
</div>

<div style="flex:1; min-width:280px; padding:14px 16px; border-radius:14px; background:rgba(255,228,196,.55); border:1px solid rgba(184,134,11,.18);">
  <h3 style="margin:0 0 8px; color:#8B4513;">🎓 适合人群</h3>
  <ul style="margin:0; padding-left:18px; color:#5C4033;">
    <li><b style="color:#8B4513;">算法学习者</b>：可视化理解搜索过程</li>
    <li><b style="color:#8B4513;">教师</b>：课堂演示与对比实验</li>
    <li><b style="color:#8B4513;">开发者</b>：理解路径规划在游戏/导航中的落地</li>
    <li><b style="color:#8B4513;">玩家</b>：迷宫本身也很有趣</li>
  </ul>
</div>

</div>

---

## ✨ 核心特性

### 🎯 四大算法

<table>
<tr>
<td width="25%" align="center" style="border-radius:14px; background:rgba(144,238,144,.14); border:1px solid rgba(144,238,144,.25); padding:12px;">
<b style="color:#8B4513;">BFS 🌊</b><br/>
<span style="color:#5C4033;">像水波扩散，层层推进</span><br/>
<sub style="color:#2f6f2f;">无权图最短路径</sub>
</td>

<td width="25%" align="center" style="border-radius:14px; background:rgba(222,184,135,.16); border:1px solid rgba(222,184,135,.28); padding:12px;">
<b style="color:#8B4513;">DFS 🧭</b><br/>
<span style="color:#5C4033;">一条路走到底，遇墙回头</span><br/>
<sub style="color:#8B4513;">迷宫探索 / 生成</sub>
</td>

<td width="25%" align="center" style="border-radius:14px; background:rgba(255,179,71,.18); border:1px solid rgba(255,179,71,.30); padding:12px;">
<b style="color:#8B4513;">Dijkstra 🎯</b><br/>
<span style="color:#5C4033;">精打细算，总代价最小</span><br/>
<sub style="color:#8B5A00;">加权图最短路径</sub>
</td>

<td width="25%" align="center" style="border-radius:14px; background:rgba(255,215,0,.14); border:1px solid rgba(255,215,0,.25); padding:12px;">
<b style="color:#8B4513;">A* ⭐</b><br/>
<span style="color:#5C4033;">启发式搜索，直奔目标</span><br/>
<sub style="color:#B8860B;">游戏 AI 首选</sub>
</td>
</tr>
</table>

### 🎨 甜点主题配色

| 元素 | 颜色 | 说明 |
|------|------|------|
| 🍪 饼干地面 | `rgba(255, 250, 240, 0.3)` | 普通通行，无额外代价 |
| 🍫 巧克力墙 | `#8B4513` | 不可通行障碍（带渐变光泽） |
| 🍯 蜂蜜地形 | `#FFB347` | 粘稠地形，消耗 1 点体力 |
| 🏠 姜饼屋 | `#90EE90` | 冒险起点 |
| 🎁 圣诞礼物 | `#FF6B6B` | 胜利终点 |
| 🔵 探索中 | `#98D8C8` | 正在访问节点 |
| 🟤 已完成 | `#DEB887` | 已处理节点 |
| 🟡 最终路径 | `#FFD700` | 找到的最佳路径 |

### 🎬 动画系统

- <span style="color:#FF6B6B;"><b>✨ 实时探索动画</b></span>：看算法如何一步步找路  
- <span style="color:#B8860B;"><b>🏃 姜饼人行走</b></span>：沿最终路径移动  
- <span style="color:#2f6f2f;"><b>⚡ 可调速度</b></span>：适合快速演示或慢速学习  
- <span style="color:#8B4513;"><b>🧾 保留探索轨迹</b></span>：可选择保留搜索过程颜色  

### 📊 详细统计

- <b style="color:#8B4513;">📏 路径长度</b>：从起点到终点的格子数  
- <b style="color:#8B5A00;">💰 总代价</b>：考虑地形后的累计体力消耗  
- <b style="color:#2f6f2f;">👀 访问节点</b>：算法访问过的节点数  
- <b style="color:#8B4513;">🔍 扩展节点</b>：算法处理过的节点数  
- <b style="color:#B22222;">⏱️ 运行时间</b>：毫秒级计时 

---


## 🚀 快速开始

<div style="background: linear-gradient(135deg, rgba(144,238,144,0.2), rgba(152,216,200,0.2)); padding: 24px; border-radius: 16px; border: 2px solid #90EE90; margin: 20px 0;">

### 前置要求

<div style="display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0;">
  <span style="background: white; padding: 8px 16px; border-radius: 20px; border: 2px solid #8B4513; color: #8B4513; font-weight: 600;">🐍 Python 3.8+</span>
  <span style="background: white; padding: 8px 16px; border-radius: 20px; border: 2px solid #8B4513; color: #8B4513; font-weight: 600;">🌐 现代浏览器</span>
</div>

### 安装步骤

```bash
# 1. 克隆项目
git clone https://github.com/yedda1117/cookie-Maze.git
cd cookie-Maze

# 2. 创建虚拟环境（推荐）
python -m venv venv

# 3. 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安装依赖
pip install -r requirements.txt

# 5. 启动应用
python main.py
```

### 🎉 开始游戏

<div style="background: white; padding: 16px; border-radius: 12px; margin-top: 16px; border-left: 4px solid #FFD700;">
  <div style="font-size: 1.2em; font-weight: 600; color: #8B4513; margin-bottom: 8px;">
    打开浏览器访问：<code style="background: #FFF8DC; padding: 4px 12px; border-radius: 6px; color: #FF6B6B;">http://127.0.0.1:5000</code>
  </div>
  <div style="color: #5C4033;">你会看到一个超可爱的饼干迷宫界面！🍪✨</div>
</div>

</div>

---

## 🎮 使用指南

<div style="background: linear-gradient(135deg, rgba(255,239,213,0.5), rgba(255,228,196,0.5)); padding: 24px; border-radius: 16px; margin: 20px 0;">

### 基础操作

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 20px 0;">

<div style="background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2.5em; margin-bottom: 8px;">🏠</div>
  <div style="font-weight: 600; color: #2E8B57; margin-bottom: 8px; font-size: 1.1em;">1. 设置起点</div>
  <div style="color: #5C4033; font-size: 0.95em; line-height: 1.5;">
    点击底部"设置起点"按钮<br/>
    在地图上点击一个位置<br/>
    <span style="color: #90EE90; font-weight: 600;">✓ 薄荷绿姜饼屋出现</span>
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2.5em; margin-bottom: 8px;">🎁</div>
  <div style="font-weight: 600; color: #FF6B6B; margin-bottom: 8px; font-size: 1.1em;">2. 设置终点</div>
  <div style="color: #5C4033; font-size: 0.95em; line-height: 1.5;">
    点击"设置终点"按钮<br/>
    在地图上点击另一个位置<br/>
    <span style="color: #FF6B6B; font-weight: 600;">✓ 草莓红礼物出现</span>
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2.5em; margin-bottom: 8px;">🍫</div>
  <div style="font-weight: 600; color: #8B4513; margin-bottom: 8px; font-size: 1.1em;">3. 绘制障碍物</div>
  <div style="color: #5C4033; font-size: 0.95em; line-height: 1.5;">
    点击"设置障碍物"按钮<br/>
    在地图上点击创建巧克力墙<br/>
    <span style="color: #8B4513; font-weight: 600;">✓ 再次点击可清除</span>
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2.5em; margin-bottom: 8px;">🎯</div>
  <div style="font-weight: 600; color: #DAA520; margin-bottom: 8px; font-size: 1.1em;">4. 选择算法</div>
  <div style="color: #5C4033; font-size: 0.95em; line-height: 1.5;">
    在右侧面板选择算法<br/>
    BFS / DFS / Dijkstra / A*<br/>
    <span style="color: #DAA520; font-weight: 600;">✓ A*可选启发式函数</span>
  </div>
</div>

<div style="background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2.5em; margin-bottom: 8px;">⚡</div>
  <div style="font-weight: 600; color: #FF8C00; margin-bottom: 8px; font-size: 1.1em;">5. 执行搜索</div>
  <div style="color: #5C4033; font-size: 0.95em; line-height: 1.5;">
    点击"执行搜索"按钮<br/>
    观看探索动画<br/>
    <span style="color: #FFD700; font-weight: 600;">✓ 姜饼人沿金黄路径前进</span>
  </div>
</div>

</div>

### 进阶功能

<div style="margin-top: 20px;">

#### 🎲 迷宫生成

<div style="display: flex; gap: 12px; margin: 12px 0;">
  <span style="background: linear-gradient(135deg, #98D8C8, #90EE90); color: white; padding: 10px 20px; border-radius: 10px; font-weight: 600;">随机迷宫</span>
  <span style="color: #5C4033;">生成25%密度的随机障碍物</span>
</div>

<div style="display: flex; gap: 12px; margin: 12px 0;">
  <span style="background: linear-gradient(135deg, #FFB347, #FFD700); color: white; padding: 10px 20px; border-radius: 10px; font-weight: 600;">DFS迷宫</span>
  <span style="color: #5C4033;">生成完美迷宫（保证有唯一解）</span>
</div>

#### 🔄 算法对比

<div style="background: rgba(255,255,255,0.6); padding: 16px; border-radius: 12px; margin: 12px 0;">
  <ol style="color: #5C4033; line-height: 1.8; margin: 0; padding-left: 20px;">
    <li>生成一个迷宫</li>
    <li>选择BFS，点击"执行搜索"，记录统计数据</li>
    <li>点击"重置搜索"（保留地图）</li>
    <li>选择A*，再次搜索</li>
    <li><span style="color: #FF6B6B; font-weight: 600;">对比两个算法的性能差异！</span></li>
  </ol>
</div>

</div>

</div>

---



## 📁 项目结构

<div style="background: linear-gradient(135deg, rgba(222,184,135,0.2), rgba(210,180,140,0.2)); padding: 24px; border-radius: 16px; margin: 20px 0;">

```
cookie-Maze/
├── 🎯 app.py                    # Flask主应用，API路由
├── 🚀 main.py                   # 启动入口
├── 📦 requirements.txt          # Python依赖
│
├── 🎨 templates/
│   └── index.html              # 主页面HTML
│
├── 💅 static/
│   ├── css/
│   │   └── style.css           # 饼干主题样式（超可爱！）
│   └── js/
│       └── app.js              # 前端逻辑和动画
│
├── 🧠 core/                     # 核心算法实现
│   ├── base_algorithm.py       # 算法基类
│   ├── search_bfs.py           # BFS广度优先搜索
│   ├── search_dfs.py           # DFS深度优先搜索
│   ├── dijkstra.py             # Dijkstra最短路径
│   ├── astar.py                # A*启发式搜索
│   └── maze/
│       ├── utils.py            # 网格和节点类
│       └── maze_generator.py  # 迷宫生成器
│
├── ⚙️ config/
│   ├── constants.py            # 常量定义（颜色、状态等）
│   └── settings.py             # 系统配置
│
├── 🎪 events/                   # 事件系统
│   ├── event.py
│   ├── event_queue.py
│   └── event_types.py
│
├── 🛠️ utils/                    # 工具函数
│   └── logger.py
│
└── 📚 docs/                     # 文档
    ├── 快速开始.md
    ├── 实现总结.md
    └── LIVESHARE_GUIDE.md
```

</div>

---


## 🛠️ 技术栈

<div style="background: linear-gradient(135deg, rgba(255,250,240,0.8), rgba(255,239,213,0.8)); padding: 24px; border-radius: 16px; margin: 20px 0;">

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2em; margin-bottom: 12px;">🐍</div>
  <div style="font-weight: 600; color: #8B4513; font-size: 1.2em; margin-bottom: 12px;">后端技术</div>
  <ul style="color: #5C4033; line-height: 1.8; margin: 0; padding-left: 20px;">
    <li><strong>Python 3.8+</strong> - 主要编程语言</li>
    <li><strong>Flask 3.0</strong> - 轻量级Web框架</li>
    <li><strong>Flask-CORS</strong> - 跨域资源共享</li>
  </ul>
</div>

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2em; margin-bottom: 12px;">🎨</div>
  <div style="font-weight: 600; color: #FF6B6B; font-size: 1.2em; margin-bottom: 12px;">前端技术</div>
  <ul style="color: #5C4033; line-height: 1.8; margin: 0; padding-left: 20px;">
    <li><strong>HTML5</strong> - 页面结构</li>
    <li><strong>CSS3</strong> - 饼干主题样式</li>
    <li><strong>JavaScript ES6+</strong> - 原生JS</li>
    <li><strong>Canvas API</strong> - 网格绘制</li>
  </ul>
</div>

<div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1);">
  <div style="font-size: 2em; margin-bottom: 12px;">✨</div>
  <div style="font-weight: 600; color: #FFD700; font-size: 1.2em; margin-bottom: 12px;">特色技术</div>
  <ul style="color: #5C4033; line-height: 1.8; margin: 0; padding-left: 20px;">
    <li><strong>事件驱动架构</strong> - 解耦设计</li>
    <li><strong>动画系统</strong> - 流畅动画</li>
    <li><strong>Live Share</strong> - 远程协作</li>
  </ul>
</div>

</div>

</div>

---

## 🤝 贡献者

<div style="background: linear-gradient(135deg, rgba(255,192,203,0.2), rgba(255,182,193,0.2)); padding: 24px; border-radius: 16px; margin: 20px 0; text-align: center;">

<div style="font-size: 1.3em; font-weight: 600; color: #8B4513; margin-bottom: 20px;">
  感谢所有为这个项目付出努力的小伙伴们！❤️
</div>

<table align="center">
  <tr>
    <td align="center" style="padding: 20px;">
      <a href="https://github.com/yedda1117">
        <img src="https://github.com/yedda1117.png" width="120px;" style="border-radius: 50%; border: 4px solid #90EE90; box-shadow: 0 4px 12px rgba(144,238,144,0.3);" alt="Yedda"/>
        <br />
        <div style="margin-top: 12px; font-weight: 600; font-size: 1.1em; color: #2E8B57;">Yedda</div>
      </a>
      <br />
      <div style="background: linear-gradient(135deg, #90EE90, #98D8C8); color: white; padding: 6px 16px; border-radius: 20px; font-size: 0.9em; font-weight: 600; margin-top: 8px;">🧠 算法实现 & 后端开发</div>
    </td>
    <td align="center" style="padding: 20px;">
      <a href="https://github.com/civet0921">
        <img src="https://github.com/civet0921.png" width="120px;" style="border-radius: 50%; border: 4px solid #FFB347; box-shadow: 0 4px 12px rgba(255,179,71,0.3);" alt="Civet"/>
        <br />
        <div style="margin-top: 12px; font-weight: 600; font-size: 1.1em; color: #FF8C00;">Civet</div>
      </a>
      <br />
      <div style="background: linear-gradient(135deg, #FFB347, #FFD700); color: white; padding: 6px 16px; border-radius: 20px; font-size: 0.9em; font-weight: 600; margin-top: 8px;">🎨 前端开发 & UI设计</div>
    </td>
  </tr>
</table>

<div style="margin-top: 20px; padding: 16px; background: rgba(255,255,255,0.6); border-radius: 12px;">
  <div style="font-weight: 600; color: #8B4513; margin-bottom: 8px;">🌟 如何贡献</div>
  <div style="color: #5C4033; font-size: 0.95em;">
    欢迎 Fork 本仓库，提交 Pull Request，或报告 Bug！
  </div>
</div>

</div>

---

## 🐛 常见问题

<div style="background: linear-gradient(135deg, rgba(255,228,196,0.5), rgba(255,218,185,0.5)); padding: 24px; border-radius: 16px; margin: 20px 0;">

<details>
<summary style="font-weight: 600; color: #8B4513; font-size: 1.1em; cursor: pointer; padding: 12px; background: white; border-radius: 8px; margin-bottom: 12px;">
  ❓ 启动时提示端口被占用？
</summary>
<div style="padding: 16px; background: rgba(255,255,255,0.6); border-radius: 8px; margin-top: 8px;">
  <div style="color: #5C4033; margin-bottom: 12px;">有其他程序占用了5000端口</div>
  <div style="background: #2d2d2d; color: #f8f8f2; padding: 12px; border-radius: 6px; font-family: monospace;">
    <div style="color: #6A9955;"># 使用其他端口启动</div>
    <div>python run.py --port 8080</div>
    <div style="color: #6A9955;"># 然后访问 http://127.0.0.1:8080</div>
  </div>
</div>
</details>

<details>
<summary style="font-weight: 600; color: #8B4513; font-size: 1.1em; cursor: pointer; padding: 12px; background: white; border-radius: 8px; margin-bottom: 12px;">
  ❓ 网页打开是空白的？
</summary>
<div style="padding: 16px; background: rgba(255,255,255,0.6); border-radius: 8px; margin-top: 8px;">
  <div style="color: #5C4033;">检查浏览器控制台（F12）</div>
  <ul style="color: #5C4033; line-height: 1.8;">
    <li>确认Flask服务器运行正常</li>
    <li>尝试刷新页面（Ctrl+R）</li>
    <li>检查静态文件路径</li>
  </ul>
</div>
</details>

<details>
<summary style="font-weight: 600; color: #8B4513; font-size: 1.1em; cursor: pointer; padding: 12px; background: white; border-radius: 8px; margin-bottom: 12px;">
  ❓ 算法找不到路径？
</summary>
<div style="padding: 16px; background: rgba(255,255,255,0.6); border-radius: 8px; margin-top: 8px;">
  <div style="color: #5C4033; margin-bottom: 8px;">这是正常的！</div>
  <ul style="color: #5C4033; line-height: 1.8;">
    <li>起点和终点之间被障碍物完全隔开</li>
    <li>点击"清除障碍物"重试</li>
    <li>或使用"DFS迷宫"生成保证有解的迷宫</li>
  </ul>
</div>
</details>

<details>
<summary style="font-weight: 600; color: #8B4513; font-size: 1.1em; cursor: pointer; padding: 12px; background: white; border-radius: 8px; margin-bottom: 12px;">
  ❓ 姜饼人不动？
</summary>
<div style="padding: 16px; background: rgba(255,255,255,0.6); border-radius: 8px; margin-top: 8px;">
  <div style="color: #5C4033;">检查是否找到了路径</div>
  <ul style="color: #5C4033; line-height: 1.8;">
    <li>确保起点和终点之间有通路</li>
    <li>查看右侧统计信息的"状态"</li>
    <li>尝试重新设置起点和终点</li>
  </ul>
</div>
</details>

<div style="margin-top: 20px; padding: 16px; background: rgba(255,255,255,0.8); border-radius: 12px; border-left: 4px solid #90EE90;">
  <div style="font-weight: 600; color: #2E8B57; margin-bottom: 8px;">📖 更多问题</div>
  <div style="color: #5C4033;">查看 <a href="docs/快速开始.md" style="color: #8B4513; font-weight: 600;">快速开始指南</a> 了解更多</div>
</div>

</div>

---


## 📝 开发日志

<div style="background: linear-gradient(135deg, rgba(152,216,200,0.2), rgba(144,238,144,0.2)); padding: 24px; border-radius: 16px; margin: 20px 0;">

### ✅ 已完成

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 四种核心算法
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 饼干主题UI
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 实时探索动画
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 姜饼人行走
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 地形系统
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 迷宫生成器
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> 详细统计
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #90EE90;">
    <span style="color: #2E8B57; font-weight: 600;">✓</span> Live Share支持
  </div>
</div>

### 🚧 进行中

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #FFB347;">
    <span style="color: #FF8C00; font-weight: 600;">⏳</span> 更多算法
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #FFB347;">
    <span style="color: #FF8C00; font-weight: 600;">⏳</span> 3D可视化
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #FFB347;">
    <span style="color: #FF8C00; font-weight: 600;">⏳</span> 移动端优化
  </div>
</div>

### 💡 未来计划

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; margin: 16px 0;">
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #DEB887;">
    <span style="color: #8B4513; font-weight: 600;">💭</span> 性能对比图表
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #DEB887;">
    <span style="color: #8B4513; font-weight: 600;">💭</span> 地图导入/导出
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #DEB887;">
    <span style="color: #8B4513; font-weight: 600;">💭</span> 多人协作模式
  </div>
  <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #DEB887;">
    <span style="color: #8B4513; font-weight: 600;">💭</span> 成就系统
  </div>
</div>

</div>

---

## 📄 许可证

<div style="background: linear-gradient(135deg, rgba(255,215,0,0.2), rgba(255,193,7,0.2)); padding: 20px; border-radius: 16px; text-align: center; margin: 20px 0;">
  <div style="font-size: 1.2em; font-weight: 600; color: #8B4513; margin-bottom: 8px;">
    MIT License
  </div>
  <div style="color: #5C4033;">
    本项目采用 MIT 许可证 - 详见 LICENSE 文件
  </div>
</div>

---

## 💌 联系我们

<div style="background: linear-gradient(135deg, rgba(255,192,203,0.3), rgba(255,182,193,0.3)); padding: 24px; border-radius: 16px; margin: 20px 0;">

<div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center;">

<a href="mailto:dd3292129627@163.com" style="text-decoration: none;">
  <div style="background: white; padding: 16px 24px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1); display: flex; align-items: center; gap: 12px;">
    <span style="font-size: 1.5em;">📧</span>
    <div>
      <div style="font-weight: 600; color: #8B4513;">Email</div>
      <div style="font-size: 0.9em; color: #5C4033;">dd3292129627@163.com</div>
    </div>
  </div>
</a>

<a href="https://github.com/yedda1117/cookie-Maze/issues" style="text-decoration: none;">
  <div style="background: white; padding: 16px 24px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1); display: flex; align-items: center; gap: 12px;">
    <span style="font-size: 1.5em;">🐛</span>
    <div>
      <div style="font-weight: 600; color: #8B4513;">Issues</div>
      <div style="font-size: 0.9em; color: #5C4033;">报告问题</div>
    </div>
  </div>
</a>

<a href="https://github.com/yedda1117/cookie-Maze/discussions" style="text-decoration: none;">
  <div style="background: white; padding: 16px 24px; border-radius: 12px; box-shadow: 0 4px 12px rgba(139,69,19,0.1); display: flex; align-items: center; gap: 12px;">
    <span style="font-size: 1.5em;">💬</span>
    <div>
      <div style="font-weight: 600; color: #8B4513;">Discussions</div>
      <div style="font-size: 0.9em; color: #5C4033;">讨论交流</div>
    </div>
  </div>
</a>

</div>

</div>

---

<div align="center">

<!-- 结尾横幅 -->
<div style="
  max-width: 800px;
  padding: 30px;
  border-radius: 20px;
  background: linear-gradient(135deg, 
    rgba(255,250,240,0.95) 0%, 
    rgba(255,239,213,0.92) 50%,
    rgba(255,228,196,0.95) 100%);
  border: 3px solid rgba(139,69,19,0.3);
  box-shadow: 0 15px 40px rgba(139,69,19,0.2);
  margin: 40px auto;
">
  
  <div style="font-size: 3em; margin-bottom: 16px;">🍪✨🎁</div>
  
  <div style="font-size: 1.5em; font-weight: 600; color: #8B4513; margin-bottom: 12px;">
    如果这个项目对你有帮助
  </div>
  
  <div style="font-size: 1.3em; color: #5C4033; margin-bottom: 20px;">
    请给个 <span style="color: #FFD700; font-size: 1.2em;">⭐</span> Star 吧！
  </div>
  
  <div style="
    background: linear-gradient(135deg, #FFD700, #FFA500);
    color: white;
    padding: 12px 32px;
    border-radius: 25px;
    display: inline-block;
    font-weight: 600;
    font-size: 1.1em;
    box-shadow: 0 6px 20px rgba(255,215,0,0.4);
  ">
    <a href="https://github.com/yedda1117/cookie-Maze" style="color: white; text-decoration: none;">
      ⭐ Star on GitHub
    </a>
  </div>
  
  <div style="margin-top: 24px; padding-top: 20px; border-top: 2px solid rgba(139,69,19,0.2);">
    <div style="color: #8B4513; font-size: 1.1em; font-weight: 600;">
      Made with 🍪 and ❤️
    </div>
    <div style="color: #5C4033; margin-top: 8px;">
      by <a href="https://github.com/yedda1117" style="color: #90EE90; font-weight: 600; text-decoration: none;">Yedda</a> & 
      <a href="https://github.com/civet0921" style="color: #FFB347; font-weight: 600; text-decoration: none;">Civet</a>
    </div>
  </div>

</div>

<div style="margin-top: 30px;">
  <a href="#top" style="
    color: #8B4513;
    text-decoration: none;
    font-weight: 600;
    padding: 10px 20px;
    background: rgba(255,250,240,0.8);
    border-radius: 20px;
    border: 2px solid rgba(139,69,19,0.3);
  ">
    ⬆️ 回到顶部
  </a>
</div>

</div>
