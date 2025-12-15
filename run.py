#!/usr/bin/env python
"""
快速启动脚本 - 支持自定义端口
用法: python run.py [--port 5000]
"""

import sys
import argparse
from app import run_server

def main():
    parser = argparse.ArgumentParser(description='启动多算法路径规划可视化系统')
    parser.add_argument('--port', type=int, default=5000, help='服务器端口 (默认: 5000)')
    parser.add_argument('--debug', action='store_true', default=True, help='调试模式')
    parser.add_argument('--no-debug', dest='debug', action='store_false', help='禁用调试模式')
    
    args = parser.parse_args()
    
    print(f"🚀 启动多算法路径规划可视化系统")
    print(f"📍 访问地址: http://127.0.0.1:{args.port}")
    print(f"🌐 支持VS Code Live Share共享")
    print(f"⏹️  按 Ctrl+C 停止服务")
    print()
    
    run_server(debug=args.debug, port=args.port)

if __name__ == '__main__':
    main()
