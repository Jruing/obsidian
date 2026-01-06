---
tags:
  - Python
---
## 官网
```
https://docs.astral.sh/uv/
```
## windows安装
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
## Linux安装
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```
## 安装Python
```
uv python install 3.10 3.11 3.12
```
## 设定默认Python版本
```
uv python pin 3.12
```
## 初始化项目
```bash
uv init 项目名
```
## 添加第三方
```
cd 项目目录
uv add 包名
```
## 导出项目依赖
```
uv export --format requirements.txt
uv export --format pylock.toml
```
## 同步依赖
```
uv sync
```
## 安装工具
```
uv tool install ruff
```
## 构建包
```
uv build
```
