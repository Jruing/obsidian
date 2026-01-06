---
tags:
  - Traefik
  - 反向代理
---
## 简介
> Traefik 是一个现代化的反向代理和负载均衡器, 特别适合微服务和容器化环境（如 Docker、Kubernetes）。它的一大特点是“自动发现”后端服务，并能动态更新路由规则，而无需手动重启
## 准备工作
- Docker
- Docker Compose
## 安装
```sh
docker pull traefik:v3.6.6
```
## 样例
### 项目目录
```plantext
traefik-flask-demo/
├── docker-compose.yml
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
```
### 创建 `app/requirements.txt`
```plantext
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
    # 必须监听 0.0.0.0，否则容器外无法访问（包括 Traefik）
    app.run(host='0.0.0.0', port=8001, debug=True)
```
### 编写Dockerfile
```dockerfile
# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# 声明容器监听 8001（非必须，但好习惯）
EXPOSE 8001

CMD ["python", "app.py"]
```
### 编写DockerCompose.yaml
```yaml
# docker-compose.yml
version: '3.8'

services:
  traefik:
    image: traefik:v3.6.6
    command:
	  # 生产环境建议禁用
      - "--api.insecure=true"
      # 允许Traefik自动发现并路由到 Docker 容器中的服务
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
	  # 使用https则必须有该配置,websecure与上面一行中的web都是定义，可以换成http/https这种，如果修改，则在下方的入口定义也需要进行修改
      - "--entrypoints.websecure.address=:443"
    ports:
      - "80:80"        # HTTP 入口
      - "8080:8080"    # Dashboard
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped

  flask-app:
    # 使用Dockerfile构建镜像
    build: ./app
    labels:
      # 启用traefix
      - "traefik.enable=true"
      # 指定路由匹配规则
      - "traefik.http.routers.flask.rule=Host(`app1.local`)"
      # 指定入口点（websecure为443，web为80，根据上面定义选择相应的入口，此处必须和上面定义的保持一致）
      - "traefik.http.routers.flask.entrypoints=websecure"
      # 显式指定服务名称
      - "traefik.http.routers.flask.service=flask-service"
      # 启用https
      - "traefik.http.routers.flask.tls=true"
      # 指定服务端口
      - "traefik.http.services.flask-service.loadbalancer.server.port=8001"
    # 注意：没有 ports: 映射！
    restart: unless-stopped
```
### 修改本地hosts文件
```
# 添加下面的内容
127.0.0.1 app1.local
```
### 启动项目
```sh
docker compose up -d --build
```
### 访问
```
http://app1.local
# 若启用https则访问
https://app1.local
```