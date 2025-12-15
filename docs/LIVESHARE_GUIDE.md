# VS Code Live Share 使用指南

本文档说明如何使用VS Code Live Share功能共享多算法路径规划可视化系统。

## 什么是Live Share?

VS Code Live Share是一个实时协作编程工具，允许多人同时编辑和调试代码。对于我们的项目，可以用来：

1. **共享应用** - 让其他人在浏览器中实时查看应用
2. **共享终端** - 让其他人看到或控制终端输出
3. **代码协作** - 多人同时编写和修改代码

## 前置条件

1. **VS Code已安装** - 最新版本
2. **Live Share扩展已安装** - 通常VS Code会自动安装
3. **Microsoft账户或GitHub账户** - 用于身份验证
4. **项目已准备** - `python main.py` 能成功运行

## 方法1: 共享端口（推荐）

这是最简单的方式，只需要共享Flask应用的端口。

### 步骤1：启动应用
```bash
python main.py
# 或
python run.py --port 5000
```

应用会在 `http://127.0.0.1:5000` 启动

### 步骤2：打开VS Code命令面板
- Windows/Linux: `Ctrl + Shift + P`
- macOS: `Cmd + Shift + P`

### 步骤3：搜索Live Share服务器
输入 `Live Share` 并选择：
```
Live Share: Share Server
```

### 步骤4：选择端口
弹出提示时选择 `5000` 端口

### 步骤5：分享链接
VS Code会生成一个类似以下的链接：
```
https://prod.liveshare.vsengsaas.visualstudio.com/join/?socketio=true&...
```

复制此链接，可以：
- 直接分享给朋友
- 通过QQ/WeChat发送
- 在课堂上展示（使用投影仪）

### 步骤6：访问者加入
访问者只需：
1. 点击链接（不需要安装任何工具）
2. 可选地在浏览器中登录Microsoft账户
3. 即可实时看到应用界面

## 方法2: 完整Live Share会话

这个方法允许完全的代码和终端共享。

### 步骤1：启动Live Share会话
命令面板输入 `Live Share`，选择：
```
Live Share: Start Collaboration Session
```

### 步骤2：选择邀请方式
VS Code会提示邀请方式，通常会生成一个链接

### 步骤3：启动应用
在VS Code终端中运行：
```bash
python main.py
```

### 步骤4：分享链接
复制生成的Live Share链接发送给他人

### 步骤5：访问者加入
访问者点击链接即可加入会话

## 方法3: 邀请朋友编辑代码和运行

如果你想邀请朋友一起编辑代码和运行应用：

### 主持者（Share Host）
1. 启动Live Share: `Live Share: Start Collaboration Session`
2. 生成链接后，在VS Code中打开项目文件夹
3. 在VS Code终端运行应用
4. 分享链接给朋友

### 访问者（Collaborator）
1. 点击接收到的Live Share链接
2. VS Code会自动打开，接收项目代码
3. 可以：
   - 查看代码
   - 在主持者允许的情况下编辑代码
   - 看到应用的实时运行效果
   - 共享终端（如果主持者允许）

## 实时演示场景

### 场景1：课堂演示（推荐）

**讲师：**
1. 打开项目，运行 `python main.py`
2. 使用"共享端口"方式共享
3. 复制链接，显示在屏幕上或通过QQ分享
4. 在地图上设置起点、终点、障碍物
5. 点击"执行搜索"演示不同算法

**学生：**
1. 点击链接进入应用
2. 在自己的浏览器中实时看到讲师的演示
3. 可以同时在自己的地图上操作

### 场景2：代码review会议

**代码主人：**
1. 启动完整Live Share会话：`Live Share: Start Collaboration Session`
2. 打开要演示的代码文件
3. 运行应用
4. 共享链接

**评审者：**
1. 加入Live Share会话
2. 可以同时看到代码和运行效果
3. 可以提出改进建议

### 场景3：协作开发

**开发者A：**
1. 启动Live Share会话
2. 邀请开发者B

**开发者B：**
1. 加入会话
2. 可以实时编辑代码
3. 共享终端，运行应用
4. 一起调试

## 常见问题

### Q: 访问者无法看到网页？
**A:** 
- 确保你的端口5000没有防火墙阻止
- 尝试在本地浏览器中访问 `http://localhost:5000` 验证应用运行
- 检查Live Share的链接是否正确

### Q: Live Share链接过期了怎么办？
**A:** 
- 每个Live Share会话有时间限制（通常几小时）
- 需要重新生成新链接
- 再次运行 `Live Share: Share Server`

### Q: 如何停止Live Share会话？
**A:**
- 命令面板输入 `Live Share: Stop Collaboration Session`
- 或关闭VS Code

### Q: 访问者可以编辑我的代码吗？
**A:**
- 使用"共享端口"方式时，访问者只能查看应用，不能编辑代码
- 使用"完整会话"方式时，可以设置访问权限

### Q: 可以录制演示吗？
**A:**
- 可以使用OBS或其他录屏工具录制浏览器窗口
- 或使用VS Code的扩展来录制演示

## 最佳实践

1. **清理地图** - 演示前清空地图，从干净状态开始
2. **放大浏览器** - 确保观众能看清网格和控件
3. **解释算法** - 在执行搜索时口头解释算法过程
4. **对比演示** - 在同一地图上演示不同算法，展示差异
5. **使用统计信息** - 指向右侧的统计面板，说明时间和节点数

## 技术细节

### 端口共享原理
- Live Share将你的本地端口映射到公网
- 生成的链接包含加密的隧道信息
- 访问者通过VS Code的代理访问本地服务

### 安全性
- Live Share链接是一次性的，分享后可以更新
- 建议只分享给信任的人
- 演示完成后可以停止会话

### 网络要求
- 需要稳定的网络连接
- 本地网络和远程访问者都需要互联网
- 推荐使用有线连接以获得更好的稳定性

## 相关链接

- [VS Code Live Share官方文档](https://docs.microsoft.com/en-us/visualstudio/liveshare/)
- [VS Code Live Share扩展](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

## 示例

### 快速演示命令序列
```bash
# 1. 启动应用
python main.py

# 2. 在VS Code中（Ctrl+Shift+P）
Live Share: Share Server

# 3. 选择5000端口

# 4. 复制生成的链接并分享

# 5. 访问者点击链接进入
```

---

**提示**: 第一次使用Live Share时，可能需要用Microsoft账户或GitHub账户登录一次。之后就会自动认证。
