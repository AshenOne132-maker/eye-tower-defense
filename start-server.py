#!/usr/bin/env python3
"""
一键启动本地 HTTP 服务器
访问地址：http://localhost:8000
注意：WebGazer 眼动追踪需要安全上下文。
在 localhost 下运行时浏览器会自动允许摄像头权限（需用户手动点击允许）。
如果需要通过外网 HTTPS 分享给他人测试，建议使用 ngrok：
    1. 安装 ngrok: https://ngrok.com/download
    2. 运行本脚本后，再执行: ngrok http 8000
    3. 把生成的 https://xxx.ngrok.io 链接发给朋友
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"\n✅ 服务器已启动: http://localhost:{PORT}")
    print("📱 请在同一台电脑的浏览器中打开上面的地址测试眼动追踪。")
    print("⚠️  不要直接用 file:// 打开 index.html，否则摄像头权限会被浏览器拒绝。\n")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()
