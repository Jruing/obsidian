---
tags:
  - 反向代理
  - Traefik
---
```yaml
# docker-compose.yml
version: '3.8'

services:
  traefik:
    image: traefik:v3.6.6
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
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
      # 指定入口点
      - "traefik.http.routers.flask.entrypoints=websecure"
        
    
      # 为http入口创建重定向
      - "traefik.http.routers.flask-http.rule=Host(`app1.local`)"
      - "traefik.http.routers.flask-http.entrypoints=web"
      - "traefik.http.routers.flask-http.middlewares=redirect-to-https"
      # 定义重定向中间件,permanent: true 表示返回 301 永久重定向；设为 false 则是 302 临时重定向
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.permanent=true"
      # 显式指定服务名称
      - "traefik.http.routers.flask.service=flask-service"
      #启用https
      - "traefik.http.routers.flask.tls=true"
      # 指定服务端口
      - "traefik.http.services.flask-service.loadbalancer.server.port=8001"
    # 注意：没有 ports: 映射！
    restart: unless-stopped
```