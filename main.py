"""
多算法路径规划可视化系统 - 主程序入口（Web版本）
可通过浏览器访问：http://localhost:5000
可通过VS Code Live Share共享
"""

from app import run_server

if __name__ == '__main__':
    run_server(debug=True, port=5000)
