/**
 * 多算法路径规划可视化系统 - 前端应用
 */

// ============ 配置 ============
const CELL_SIZE = 20;
const COLORS = {
    empty: 'rgba(255, 250, 240, 0.3)',     // 半透明奶油白
    obstacle: '#8B4513',  // 巧克力棕
    start: '#90EE90',     // 薄荷绿（饼干人的起点）
    end: '#FF6B6B',       // 草莓红（饼干人的终点）
    honey: '#FFB84D',     // 金黄色蜂蜜
    // 饼干主题配色 - 降低透明度让蜂蜜地更明显
    open: 'rgba(152, 216, 200, 0.35)',      // 薄荷绿 - 降低透明度
    closed: 'rgba(222, 184, 135, 0.35)',    // 焦糖色 - 降低透明度
    path: 'rgba(255, 215, 0, 0.35)',      // 金黄色（饼干路径）- 降低透明度
    pathOnHoney: 'rgba(255, 140, 0, 0.6)',  // 橙红色（路径在蜂蜜地上）- 更明显的颜色
    grid: 'rgba(245, 222, 179, 0.3)'       // 半透明小麦色网格
};

const NODE_STATES = {
    EMPTY: 0,
    OBSTACLE: 1,
    START: 2,
    END: 3,
    OPEN: 4,
    CLOSED: 5,
    PATH: 6,
    HONEY: 7
};

// ============ 全局变量 ============
let canvas;
let ctx;
let gridWidth = 200;
let gridHeight = 200;
let gridData = null;
let currentMode = null;  // 'start', 'end', 'obstacle'
let animationActive = false;
let personPos = null; // {x: pixel, y: pixel}
let personRadius = 6;
let showExplorationColors = true; // 控制是否显示探索颜色（动画结束后设为false）

// ============ 初始化 ============
document.addEventListener('DOMContentLoaded', function() {
    canvas = document.getElementById('gridCanvas');
    ctx = canvas.getContext('2d');
    
    // 初始化画布大小
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    // 绑定事件
    setupEventListeners();
    
    // 初始化网格
    loadGrid();
    
    // 绘制初始状态
    draw();
});

// ============ 画布管理 ============
function resizeCanvas() {
    const container = document.querySelector('.canvas-container');
    const maxWidth = container.clientWidth - 20;
    const maxHeight = container.clientHeight - 20;
    
    // 计算适应大小
    const w = Math.min(maxWidth, gridWidth * CELL_SIZE);
    const h = Math.min(maxHeight, gridHeight * CELL_SIZE);
    
    canvas.width = w;
    canvas.height = h;
    
    draw();
}

function draw() {
    if (!gridData) return;
    
    ctx.fillStyle = COLORS.empty;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // 绘制网格线
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 0.5;
    
    for (let i = 0; i <= gridWidth; i++) {
        const x = (i * canvas.width) / gridWidth;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
    }
    
    for (let i = 0; i <= gridHeight; i++) {
        const y = (i * canvas.height) / gridHeight;
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }
    
    // 绘制节点
    for (let y = 0; y < gridHeight; y++) {
        for (let x = 0; x < gridWidth; x++) {
            const node = gridData[y][x];
            drawNode(node);
        }
    }
}

// 在画布上绘制“人”覆盖层（在绘制完网格后调用）
function drawPerson() {
    if (!personPos) return;
    ctx.save();
    
    // 绘制小人身体
    const x = personPos.x;
    const y = personPos.y;
    const size = personRadius;
    
    // 阴影
    ctx.shadowColor = 'rgba(0,0,0,0.4)';
    ctx.shadowBlur = 8;
    ctx.shadowOffsetY = 2;
    
    // 身体（圆形）
    ctx.beginPath();
    ctx.fillStyle = '#FF6B35';
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();
    
    // 眼睛
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(x - size * 0.3, y - size * 0.2, size * 0.2, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.arc(x + size * 0.3, y - size * 0.2, size * 0.2, 0, Math.PI * 2);
    ctx.fill();
    
    // 瞳孔
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.arc(x - size * 0.3, y - size * 0.2, size * 0.1, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.arc(x + size * 0.3, y - size * 0.2, size * 0.1, 0, Math.PI * 2);
    ctx.fill();
    
    // 嘴巴
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(x, y + size * 0.2, size * 0.3, 0, Math.PI);
    ctx.stroke();
    
    // 小帽子
    ctx.fillStyle = '#4169E1';
    ctx.beginPath();
    ctx.arc(x, y - size * 0.8, size * 0.4, 0, Math.PI * 2);
    ctx.fill();
    
    ctx.restore();
}

function drawNode(node) {
    const x = (node.x * canvas.width) / gridWidth;
    const y = (node.y * canvas.height) / gridHeight;
    const w = canvas.width / gridWidth;
    const h = canvas.height / gridHeight;
    
    // 检查是否有蜂蜜地形（通过 terrain_cost 判断，而不是 state）
    const hasHoney = node.terrain_cost > 0;
    
    // 辅助函数：绘制蜂蜜地形
    function drawHoney() {
        const honeyGradient = ctx.createRadialGradient(x + w/2, y + h/2, 0, x + w/2, y + h/2, w/2);
        honeyGradient.addColorStop(0, '#FFD700');
        honeyGradient.addColorStop(0.5, '#FFB84D');
        honeyGradient.addColorStop(1, '#FFA500');
        ctx.fillStyle = honeyGradient;
        ctx.fillRect(x + 0.5, y + 0.5, w - 1, h - 1);
        
        // 添加蜂蜜光泽效果
        ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.beginPath();
        ctx.arc(x + w * 0.3, y + h * 0.3, w * 0.15, 0, Math.PI * 2);
        ctx.fill();
        
        // 添加小水珠效果
        ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
        ctx.beginPath();
        ctx.arc(x + w * 0.7, y + h * 0.6, w * 0.1, 0, Math.PI * 2);
        ctx.fill();
        
        // 蜂蜜边框
        ctx.strokeStyle = 'rgba(255, 165, 0, 0.6)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1);
    }
    
    let color = COLORS.empty;
    let shouldDrawOverlay = false; // 是否需要在蜂蜜地上绘制覆盖层
    
    // 处理障碍物（优先级最高）
    if (node.state === NODE_STATES.OBSTACLE) {
        const gradient = ctx.createLinearGradient(x, y, x + w, y + h);
        gradient.addColorStop(0, '#A0522D');
        gradient.addColorStop(0.5, '#8B4513');
        gradient.addColorStop(1, '#654321');
        ctx.fillStyle = gradient;
        ctx.fillRect(x + 0.5, y + 0.5, w - 1, h - 1);
        
        // 添加高光效果（巧克力光泽）
        ctx.fillStyle = 'rgba(210, 180, 140, 0.3)';
        ctx.fillRect(x + 1, y + 1, w * 0.4, h * 0.4);
        
        // 添加边框阴影
        ctx.strokeStyle = 'rgba(101, 67, 33, 0.5)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1);
        return;
    }
    
    // 先绘制蜂蜜地形（如果有）
    if (hasHoney) {
        drawHoney();
    }
    
    // 然后根据状态决定是否绘制覆盖层
    switch (node.state) {
        case NODE_STATES.HONEY:
            // 蜂蜜地已经绘制，直接返回
            return;
            
        case NODE_STATES.START:
            color = COLORS.start;
            shouldDrawOverlay = true;
            break;
            
        case NODE_STATES.END:
            color = COLORS.end;
            shouldDrawOverlay = true;
            break;
            
        case NODE_STATES.OPEN:
            // 只在显示探索颜色时绘制
            if (showExplorationColors) {
                color = COLORS.open;
                shouldDrawOverlay = true;
            }
            break;
            
        case NODE_STATES.CLOSED:
            // 只在显示探索颜色时绘制
            if (showExplorationColors) {
                color = COLORS.closed;
                shouldDrawOverlay = true;
            }
            break;
            
        case NODE_STATES.PATH:
            // 路径在蜂蜜地上用不同颜色
            color = hasHoney ? COLORS.pathOnHoney : COLORS.path;
            shouldDrawOverlay = true;
            break;
            
        case NODE_STATES.EMPTY:
        default:
            // 空格子，如果有蜂蜜地已经绘制了，否则绘制空格子
            if (!hasHoney) {
                ctx.fillStyle = COLORS.empty;
                ctx.fillRect(x + 0.5, y + 0.5, w - 1, h - 1);
            }
            return;
    }
    
    // 绘制覆盖层（如果需要）
    if (shouldDrawOverlay) {
        ctx.fillStyle = color;
        ctx.fillRect(x + 0.5, y + 0.5, w - 1, h - 1);
    }
    
    // 为 OPEN/CLOSED 添加额外标记（仅在显示探索颜色时）
    if (showExplorationColors) {
        const markerSize = Math.min(w, h) * 0.18;
        if (node.state === NODE_STATES.OPEN) {
            // 小圆点（深蓝）
            ctx.beginPath();
            ctx.fillStyle = '#0057A6';
            ctx.arc(x + w/2, y + h/2, markerSize, 0, Math.PI * 2);
            ctx.fill();
        } else if (node.state === NODE_STATES.CLOSED) {
            // 叉号（深粉/紫）
            ctx.strokeStyle = '#A60055';
            ctx.lineWidth = Math.max(1, Math.floor(Math.min(w, h) * 0.07));
            ctx.beginPath();
            ctx.moveTo(x + w*0.27, y + h*0.27);
            ctx.lineTo(x + w*0.73, y + h*0.73);
            ctx.moveTo(x + w*0.73, y + h*0.27);
            ctx.lineTo(x + w*0.27, y + h*0.73);
            ctx.stroke();
        }
    }
}

// 修改 draw 在末尾绘制人物
const _origDraw = draw;
draw = function() {
    if (!gridData) return;
    // 原始绘制逻辑
    ctx.fillStyle = COLORS.empty;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 0.5;
    for (let i = 0; i <= gridWidth; i++) {
        const x = (i * canvas.width) / gridWidth;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
    }
    for (let i = 0; i <= gridHeight; i++) {
        const y = (i * canvas.height) / gridHeight;
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }
    for (let y = 0; y < gridHeight; y++) {
        for (let x = 0; x < gridWidth; x++) {
            const node = gridData[y][x];
            drawNode(node);
        }
    }
    // 绘制人物覆盖层（不改变节点状态颜色）
    drawPerson();
}

// ============ 事件处理 ============
function setupEventListeners() {
    // 地图操作按钮
    document.getElementById('setStartBtn').addEventListener('click', () => setMode('start'));
    document.getElementById('setEndBtn').addEventListener('click', () => setMode('end'));
    document.getElementById('setObstacleBtn').addEventListener('click', () => setMode('obstacle'));
    document.getElementById('setHoneyBtn').addEventListener('click', () => setMode('honey'));
    document.getElementById('clearObstaclesBtn').addEventListener('click', () => setMode('clear'));
    
    // 迷宫生成按钮
    document.getElementById('generateRandomBtn').addEventListener('click', () => generateMaze('random'));
    document.getElementById('generateDFSBtn').addEventListener('click', () => generateMaze('dfs'));
    
    // 搜索按钮
    document.getElementById('searchBtn').addEventListener('click', search);
    document.getElementById('resetBtn').addEventListener('click', resetSearch);
    document.getElementById('clearBtn').addEventListener('click', clearMap);
    
    // 算法选择（不再需要启发式函数选择器）
    
    // 画布点击事件
    canvas.addEventListener('click', handleCanvasClick);
    // 探索速度滑块显示值
    const exploreSpeed = document.getElementById('exploreSpeed');
    const exploreSpeedVal = document.getElementById('exploreSpeedVal');
    if (exploreSpeed && exploreSpeedVal) {
        exploreSpeed.addEventListener('input', (e) => {
            exploreSpeedVal.textContent = e.target.value;
        });
    }
}

function setMode(mode) {
    currentMode = mode;
    
    // 更新按钮状态
    document.getElementById('setStartBtn').classList.toggle('active', mode === 'start');
    document.getElementById('setEndBtn').classList.toggle('active', mode === 'end');
    document.getElementById('setObstacleBtn').classList.toggle('active', mode === 'obstacle');
    document.getElementById('setHoneyBtn').classList.toggle('active', mode === 'honey');
    document.getElementById('clearObstaclesBtn').classList.toggle('active', mode === 'clear');
    
    showNotification(`模式: ${getModeLabel(mode)}`, 'info');
}

function getModeLabel(mode) {
    switch(mode) {
        case 'start': return '设置起点';
        case 'end': return '设置终点';
        case 'obstacle': return '设置障碍物';
        case 'clear': return '清除障碍/蜂蜜地';
        case 'honey': return '设置蜂蜜地';
        default: return '未知';
    }
}

function handleCanvasClick(event) {
    console.log('Canvas clicked, currentMode:', currentMode);
    
    if (!currentMode) {
        showNotification('请先选择操作模式', 'info');
        return;
    }
    
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    const gridX = Math.floor((x / canvas.width) * gridWidth);
    const gridY = Math.floor((y / canvas.height) * gridHeight);
    
    console.log('Click position:', { x, y, gridX, gridY, canvasWidth: canvas.width, canvasHeight: canvas.height });
    
    if (gridX < 0 || gridX >= gridWidth || gridY < 0 || gridY >= gridHeight) {
        console.log('Click outside grid bounds');
        return;
    }
    
    console.log('Sending set-point request:', { x: gridX, y: gridY, type: currentMode });
    
    // 发送请求到后端
    fetch('/api/set-point', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            x: gridX,
            y: gridY,
            type: currentMode
        })
    })
    .then(response => {
        console.log('Set-point response:', response);
        return response.json();
    })
    .then(data => {
        console.log('Set-point data:', data);
        loadGrid();
        draw();
    })
    .catch(err => console.error('Error:', err));
}

// ============ API 调用 ============
function loadGrid() {
    return fetch('/api/grid')
        .then(response => response.json())
        .then(data => {
            gridWidth = data.width;
            gridHeight = data.height;
            gridData = data.nodes;
            // 清除人物位置（重新绘制时不保留上一动画位置）
            personPos = null;
            resizeCanvas();
            draw();
        })
        .catch(err => console.error('Error loading grid:', err));
}

// clearObstacles 函数已移除，现在通过点击模式来清除障碍物

function generateMaze(type) {
    animationActive = true;
    showNotification('正在生成迷宫...', 'info');
    
    fetch('/api/generate-maze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: type })
    })
    .then(() => {
        loadGrid();
        animationActive = false;
        showNotification('迷宫生成完成', 'success');
    })
    .catch(err => {
        animationActive = false;
        console.error('Error:', err);
        showNotification('生成失败', 'error');
    });
}

function search() {
    if (animationActive) {
        showNotification('搜索进行中，请稍候', 'info');
        return;
    }
    
    const algorithmValue = document.getElementById('algorithmSelect').value;
    
    // 解析算法和启发式函数
    let algorithm = algorithmValue;
    let heuristic = 'manhattan'; // 默认值
    
    if (algorithmValue.startsWith('astar-')) {
        algorithm = 'astar';
        heuristic = algorithmValue.replace('astar-', ''); // 'manhattan' 或 'euclidean'
    }
    
    animationActive = true;
    document.getElementById('searchBtn').disabled = true;
    document.getElementById('status').textContent = '搜索中...';
    
    fetch('/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            algorithm: algorithm,
            heuristic: heuristic
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.message || '搜索失败');
            });
        }
        return response.json();
    })
    .then(async data => {
        // 不立即重载整个网格，以保留开放/关闭颜色在动画播放期间不被覆盖
        if (data.found && data.path && data.path.length > 0) {
            // 更新统计信息，包括总代价
            const statsWithCost = {
                ...data.stats,
                total_cost: data.total_cost
            };
            updateStats(statsWithCost);
            document.getElementById('status').textContent = '搜索完成，播放探索动画...';

            // 获取步骤序列（后端已处理：先 open，后倒序 close）
            const steps = data.steps || [];
            console.log('收到数据:', { found: data.found, pathLength: data.path.length, stepsCount: steps.length });
            console.log('前5个步骤:', steps.slice(0, 5));

            // 从UI读取参数
            const msPerStep = parseInt(document.getElementById('exploreSpeed')?.value) || 60;
            const keepExploration = document.getElementById('keepExploration')?.checked === true;
            const msPerCell = 60; // 人物行走速度（ms/格），固定为用户提供值

            try {
                // 开始时显示探索颜色
                showExplorationColors = true;
                
                // 播放探索（蓝色前进，粉色倒着回退）
                await animateExploration(steps, msPerStep, keepExploration);
                document.getElementById('status').textContent = '播放路径动画...';
                await animatePerson(data.path, msPerCell);
                
                // 动画结束后根据用户选择决定是否隐藏探索颜色
                if (!keepExploration) {
                    showExplorationColors = false;
                }
            } catch (e) {
                console.error('动画出错:', e);
            }

            // 动画结束后在服务器端标记路径并刷新网格
            fetch('/api/mark-path', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ path: data.path })
            }).then(() => {
                // 加载网格并重绘
                loadGrid().then(() => {
                    // 如果保留探索颜色，需要重新应用探索状态
                    if (keepExploration) {
                        (steps || []).forEach(step => {
                            if (step.x >= 0 && step.x < gridWidth && step.y >= 0 && step.y < gridHeight) {
                                const node = gridData[step.y][step.x];
                                if (node && node.state !== NODE_STATES.START && node.state !== NODE_STATES.END && node.state !== NODE_STATES.PATH) {
                                    node.state = step.type === 'open' ? NODE_STATES.OPEN : NODE_STATES.CLOSED;
                                }
                            }
                        });
                    }
                    draw();
                });
            }).catch(() => loadGrid());

            document.getElementById('status').textContent = '✓ 找到路径';
            showNotification(`找到路径！长度: ${data.path_length}`, 'success');
        } else {
            // 未找到路径，刷新网格并显示提示
            loadGrid();
            document.getElementById('status').textContent = '✗ 未找到路径';
            showNotification('未找到通往终点的路径', 'error');
        }

        animationActive = false;
        document.getElementById('searchBtn').disabled = false;
    })
    .catch(err => {
        console.error('Error:', err);
        document.getElementById('status').textContent = '错误';
        showNotification(err.message || '搜索失败', 'error');
        animationActive = false;
        document.getElementById('searchBtn').disabled = false;
    });
}

function resetSearch() {
    fetch('/api/reset', { method: 'POST' })
        .then(() => {
            showExplorationColors = true; // 重置时重新启用探索颜色
            loadGrid();
            clearStats();
            document.getElementById('status').textContent = '就绪';
            showNotification('已重置', 'info');
        })
        .catch(err => console.error('Error:', err));
}

function clearMap() {
    fetch('/api/clear', { method: 'POST' })
        .then(() => {
            showExplorationColors = true; // 清空时重新启用探索颜色
            loadGrid();
            clearStats();
            currentMode = null;
            document.getElementById('status').textContent = '就绪';
            showNotification('地图已清空', 'success');
        })
        .catch(err => console.error('Error:', err));
}

// ============ 统计信息 ============
/**
 * animatePerson(path)
 * path: [{x, y}, ...] (grid coordinates)
 * 返回 Promise，在动画完成后 resolve
 */
function animatePerson(path) {
    // msPerCell: 每格动画时间（毫秒），可选，默认 60
    return new Promise((resolve, reject) => {
        if (!path || path.length === 0) return resolve();

        // 计算每个格子的像素中心
        const centers = path.map(p => {
            const cx = (p.x + 0.5) * canvas.width / gridWidth;
            const cy = (p.y + 0.5) * canvas.height / gridHeight;
            return { x: cx, y: cy };
        });

        // 动画参数
        // 如果调用时传入第二个参数，将在 closure 的 arguments 中，可兼容旧调用
        const arg2 = (arguments && arguments[1]) ? arguments[1] : null;
        const msPerCell = arg2 || 60; // 每格持续时间（毫秒）
        personRadius = Math.min(canvas.width / gridWidth, canvas.height / gridHeight) * 0.35;

        // 初始化体力值
        let initialEnergy = 100;
        let currentEnergy = initialEnergy;
        updateEnergyBar(currentEnergy);

        let segIndex = 0;
        let startTime = null;

        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;

            // 总共需要的时间到当前段
            const totalSegs = centers.length - 1;
            if (totalSegs <= 0) {
                // 单点
                personPos = centers[0];
                draw();
                return resolve();
            }

            // 当前段的序号
            const newSegIndex = Math.min(Math.floor(elapsed / msPerCell), totalSegs - 1);
            
            // 检测是否进入新格子，更新体力值
            // 体力消耗 = (1 + terrain_cost) * 系数
            // 普通地形：1 * 5 = 5 体力
            // 蜂蜜地形：3 * 5 = 15 体力
            if (newSegIndex > segIndex && newSegIndex < path.length) {
                const node = gridData[path[newSegIndex].y][path[newSegIndex].x];
                if (node) {
                    const moveCost = 1 + (node.terrain_cost || 0);
                    currentEnergy = Math.max(0, currentEnergy - moveCost * 5);
                    updateEnergyBar(currentEnergy);
                }
            }
            segIndex = newSegIndex;
            
            const segStartTime = segIndex * msPerCell;
            const t = Math.min((elapsed - segStartTime) / msPerCell, 1);

            const a = centers[segIndex];
            const b = centers[segIndex + 1];
            personPos = { x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t };
            draw();

            if (elapsed >= msPerCell * totalSegs) {
                // 到达终点
                personPos = centers[centers.length - 1];
                draw();
                return resolve();
            }

            requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
    });
}

/**
 * 更新体力值显示
 */
function updateEnergyBar(energy) {
    const energyBar = document.getElementById('energyBar');
    const energyText = document.getElementById('energyText');
    
    if (!energyBar || !energyText) return;
    
    const percentage = Math.max(0, Math.min(100, energy));
    energyBar.style.width = percentage + '%';
    energyText.textContent = Math.round(percentage);
    
    // 体力值低时添加警告效果
    if (percentage < 30) {
        energyBar.classList.add('low');
    } else {
        energyBar.classList.remove('low');
    }
}

/**
 * animateExploration(steps, msPerStep, keepAfterFinish)
 * steps: [{type: 'open'|'close', x, y}, ...]  统一的步骤序列，按真实执行顺序
 * msPerStep: 每步毫秒数
 * keepAfterFinish: 是否在动画结束后保留探索颜色
 * 
 * 交错播放：open -> 蓝色(OPEN)，close -> 粉色(CLOSED)
 * 完美还原 DFS 的真实递归栈行为（进入时蓝，回退时粉）
 */
function animateExploration(steps, msPerStep = 60, keepAfterFinish = true) {
    return new Promise(async (resolve) => {
        if (!steps || steps.length === 0) return resolve();

        const sleep = (ms) => new Promise(r => setTimeout(r, ms));
        const prevStates = new Map();

        // 安全设置节点状态（不会覆盖起点/终点/路径）
        function setStateSafe(x, y, state) {
            if (x < 0 || x >= gridWidth || y < 0 || y >= gridHeight) return;
            const node = gridData[y][x];
            if (!node) return;
            const key = `${x},${y}`;
            if (!prevStates.has(key)) prevStates.set(key, node.state);
            if (node.state !== NODE_STATES.START && node.state !== NODE_STATES.END && node.state !== NODE_STATES.PATH) {
                node.state = state;
            }
        }

        // 逐步播放（交错蓝粉）
        for (let i = 0; i < steps.length; i++) {
            const step = steps[i];
            const state = step.type === 'open' ? NODE_STATES.OPEN : NODE_STATES.CLOSED;
            setStateSafe(step.x, step.y, state);
            draw();
            await sleep(msPerStep);
        }

        // 如果不保留，恢复之前的状态
        if (!keepAfterFinish) {
            for (const [key, state] of prevStates.entries()) {
                const [sx, sy] = key.split(',').map(Number);
                if (sx >= 0 && sx < gridWidth && sy >= 0 && sy < gridHeight) {
                    const node = gridData[sy][sx];
                    if (node) node.state = state;
                }
            }
            draw();
        }

        resolve();
    });
}

function updateStats(stats) {
    document.getElementById('pathLength').textContent = stats.path_length || '-';
    document.getElementById('visitedCount').textContent = stats.visited_count || '-';
    document.getElementById('expandedCount').textContent = stats.expanded_count || '-';
    document.getElementById('elapsedTime').textContent = (stats.elapsed_time || 0).toFixed(2);
    document.getElementById('totalCost').textContent = stats.total_cost !== undefined ? stats.total_cost : '-';
}

function clearStats() {
    document.getElementById('pathLength').textContent = '-';
    document.getElementById('visitedCount').textContent = '-';
    document.getElementById('expandedCount').textContent = '-';
    document.getElementById('elapsedTime').textContent = '-';
    document.getElementById('totalCost').textContent = '-';
    updateEnergyBar(100); // 重置体力值
}

// ============ 通知系统 ============
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}
