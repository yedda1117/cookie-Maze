"""
地形代价系统演示脚本
快速设置一个展示场景，对比BFS和Dijkstra的路径选择差异
"""

from core.maze.utils import Grid
from core.search_bfs import BFSAlgorithm
from core.dijkstra import DijkstraAlgorithm
from config.constants import NodeState

def create_demo_scenario():
    """创建演示场景：中间有蜂蜜地带，两侧有绕路通道"""
    grid = Grid(25, 25)
    
    # 设置起点和终点
    grid.set_start(2, 12)
    grid.set_end(22, 12)
    
    # 在中间创建蜂蜜地带（垂直方向）
    for y in range(5, 20):
        node = grid.get_node(12, y)
        if node:
            node.state = NodeState.HONEY
            node.terrain_cost = 1
    
    # 添加一些障碍物，强制选择路径
    for x in range(8, 17):
        if x != 12:  # 保留中间通道
            grid.set_obstacle(x, 4)
            grid.set_obstacle(x, 20)
    
    return grid

def run_comparison():
    """运行BFS和Dijkstra对比"""
    print("=" * 60)
    print("🍪 地形代价系统演示 - BFS vs Dijkstra")
    print("=" * 60)
    print()
    
    # 创建场景
    print("📍 场景设置：")
    print("  - 起点: (2, 12)")
    print("  - 终点: (22, 12)")
    print("  - 中间有一条蜂蜜地带（代价+1）")
    print("  - 可以选择直接穿过或绕路")
    print()
    
    grid = create_demo_scenario()
    
    # 测试BFS
    print("🔵 运行 BFS 算法...")
    bfs = BFSAlgorithm(grid)
    bfs.set_start_end(grid.start_node, grid.end_node)
    bfs_path = bfs.search()
    
    # 计算BFS的总代价
    bfs_cost = 0
    for node in bfs_path:
        bfs_cost += 1 + node.terrain_cost
    
    print(f"  ✓ 路径长度: {len(bfs_path) - 1} 步")
    print(f"  ✓ 总代价: {bfs_cost}")
    print(f"  ✓ 访问节点: {bfs.visited_count}")
    print(f"  ✓ 扩展节点: {bfs.expanded_count}")
    print()
    
    # 重置网格
    grid.reset()
    
    # 测试Dijkstra
    print("🟢 运行 Dijkstra 算法...")
    dijkstra = DijkstraAlgorithm(grid)
    dijkstra.set_start_end(grid.start_node, grid.end_node)
    dijkstra_path = dijkstra.search()
    
    dijkstra_cost = grid.end_node.g
    
    print(f"  ✓ 路径长度: {len(dijkstra_path) - 1} 步")
    print(f"  ✓ 总代价: {dijkstra_cost}")
    print(f"  ✓ 访问节点: {dijkstra.visited_count}")
    print(f"  ✓ 扩展节点: {dijkstra.expanded_count}")
    print()
    
    # 对比结果
    print("=" * 60)
    print("📊 对比结果：")
    print("=" * 60)
    
    if len(bfs_path) < len(dijkstra_path):
        print(f"✅ BFS 找到了更短的路径（{len(bfs_path)-1} vs {len(dijkstra_path)-1} 步）")
    elif len(bfs_path) > len(dijkstra_path):
        print(f"✅ Dijkstra 找到了更短的路径（{len(dijkstra_path)-1} vs {len(bfs_path)-1} 步）")
    else:
        print(f"⚖️  两个算法找到了相同长度的路径（{len(bfs_path)-1} 步）")
    
    print()
    
    if bfs_cost < dijkstra_cost:
        print(f"💰 BFS 的总代价更低（{bfs_cost} vs {dijkstra_cost}）")
        print("   ⚠️  这不应该发生！Dijkstra应该找到最低代价路径")
    elif bfs_cost > dijkstra_cost:
        print(f"💰 Dijkstra 的总代价更低（{dijkstra_cost} vs {bfs_cost}）")
        print(f"   ✨ 节省了 {bfs_cost - dijkstra_cost} 点代价！")
    else:
        print(f"⚖️  两个算法的总代价相同（{bfs_cost}）")
    
    print()
    print("=" * 60)
    print("💡 结论：")
    print("=" * 60)
    print("• BFS 只考虑步数，可能会选择穿过蜂蜜地的路径")
    print("• Dijkstra 考虑代价，会选择绕路避开蜂蜜地")
    print("• 在有代价地形的场景中，Dijkstra/A* 更适合！")
    print()
    print("🌐 在Web界面中可以看到更直观的可视化效果：")
    print("   python app.py")
    print("   然后访问 http://127.0.0.1:5000")
    print()

if __name__ == "__main__":
    run_comparison()
