# 👁️ 眼动塔防 (Eye Tower Defense)

一个基于 WebGazer.js 眼动追踪 + HTML5 Canvas 的竖屏塔防小游戏。

## 🎮 游戏特色

- **眼动瞄准**：通过摄像头追踪眼球位置，用眼神控制激光瞄准方向
- **竖屏游玩**：专为手机竖屏设计，随时随地可玩
- **变身系统**：击中敌人积累能量，满能量后变身巨型红猫，发射横扫激光
- **Boss 战**：第 5 波起登场狗头 Boss，具备远程投掷、近战冲撞、击退眩晕等机制
- **自动攻击**：瞄准即自动射击，无需手动点击

## 🚀 在线试玩

👉 [https://你的用户名.github.io/eye-tower-defense](https://你的用户名.github.io/eye-tower-defense)

## 🏠 本地运行

如果你不想部署，也可以在本地通过 `localhost` 运行（眼动追踪需要安全上下文，`file://` 直接打开无效）：

### Windows
双击 `start-server.bat`，脚本会自动在浏览器打开 `http://localhost:8000`。

### 手动
```bash
python start-server.py
```

## 📝 操作方式

1. 进入游戏后，允许浏览器访问摄像头以启用眼动追踪
2. 拒绝或环境不支持时，会自动降级为 **触摸 / 鼠标** 控制
3. 用眼神/手指瞄准敌人，激光自动发射
4. 击中心形道具可恢复血量

## ⚠️ 注意事项

- **必须使用手机或电脑的摄像头**，且需要在 **HTTPS 或 localhost** 环境下运行
- 直接双击 `index.html` 用 `file://` 协议打开时，浏览器会**拒绝摄像头权限**

## 🛠️ 技术栈

- HTML5 Canvas
- 原生 JavaScript (ES6+)
- WebGazer.js 3.0
- GitHub Pages

## 📄 License

MIT
