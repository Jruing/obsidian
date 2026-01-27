---
tags:
  - Traefik
  - 反向代理
---
## 简介

> Traefik 是一款现代化的反向代理与负载均衡器，专为微服务和容器化环境（如 Docker、Kubernetes）设计。其核心优势在于能够**自动发现后端服务**并**动态更新路由规则**，无需手动重启即可生效。

## 准备工作

请确保已安装以下工具：
- Docker
- Docker Compose

## 安装 Traefik 镜像

```sh
docker pull traefik:v3.6.6
```
## 示例项目：Traefik + Flask

### 项目目录结构

```plaintext
traefik-flask-demo/
├── docker-compose.yml
└── app/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```
### 创建 `app/requirements.txt`

```plaintext
Flask==3.0.3
```
### 创建 `app/app.py`

```python
# app/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "Hello from Flask behind Traefik!", "port": 8001}

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    # 必须监听 0.0.0.0，否则容器外部（包括 Traefik）无法访问
    app.run(host='0.0.0.0', port=8001, debug=True)
```
### 编写 `app/Dockerfile`

```dockerfile
# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# 声明容器监听端口（非强制，但属于良好实践）
EXPOSE 8001

CMD ["python", "app.py"]
```
### 编写 `docker-compose.yml`

```yaml
# docker-compose.yml
version: '3.8'

services:
  traefik:
    image: traefik:v3.6.6
    command:
      # ⚠️ 开启 Dashboard（生产环境建议禁用或添加认证）
      - "--api.insecure=true"
      # 启用 Docker 服务发现
      - "--providers.docker=true"
      # 默认不暴露服务，需通过 label 显式启用
      - "--providers.docker.exposedbydefault=false"
      # 定义 HTTP 入口点
      - "--entrypoints.web.address=:80"
      # 定义 HTTPS 入口点（名称 `websecure` 可自定义，但需与下方一致）
      - "--entrypoints.websecure.address=:443"
    ports:
      - "80:80"     # HTTP 流量
      - "443:443"   # HTTPS 流量
      - "8080:8080" # Traefik Dashboard
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped

  flask-app:
    build: ./app
    labels:
      # 启用 Traefik 路由
      - "traefik.enable=true"
      # 路由规则：匹配 Host(app1.local)
      - "traefik.http.routers.flask.rule=Host(`app1.local`)"
      # 指定入口点（必须与上方 entrypoints 名称一致）
      - "traefik.http.routers.flask.entrypoints=websecure"
      # 关联到自定义服务
      - "traefik.http.routers.flask.service=flask-service"
      # 启用 TLS（HTTPS）
      - "traefik.http.routers.flask.tls=true"
      # 指定后端服务端口
      - "traefik.http.services.flask-service.loadbalancer.server.port=8001"
    # 注意：无需手动映射端口！Traefik 通过 Docker 网络直接通信
    restart: unless-stopped
```
> 💡 **提示**：  
> - `web` 和 `websecure` 是自定义的入口点名称，可根据需要改为 `http`/`https`，但需确保 `routers` 中引用一致。  
> - 由于使用了 Docker 内部网络，`flask-app` 服务**不需要**在 `docker-compose.yml` 中声明 `ports`。
### 修改本地 hosts 文件

为使 `app1.local` 解析到本机，请在 `/etc/hosts`（Linux/macOS）或 `C:\Windows\System32\drivers\etc\hosts`（Windows）中添加：

```
127.0.0.1 app1.local
```
### 启动项目

```sh
docker compose up -d --build
```
### 访问服务

- 若使用 HTTPS（推荐）：
  ```
  https://app1.local
  ```

- 若仅测试 HTTP（需将 `entrypoints` 改为 `web` 并移除 TLS 相关配置）：
  ```
  http://app1.local
  ```

> 🔒 **安全提醒**：示例中启用了 `--api.insecure=true` 以便快速体验 Dashboard，**切勿在生产环境中使用**。生产部署应配置身份验证或限制 Dashboard 访问。