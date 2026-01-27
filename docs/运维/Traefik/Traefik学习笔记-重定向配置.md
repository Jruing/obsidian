---
tags:
  - 反向代理
  - Traefik
---
# 🌐 基于 Traefik 中间件实现 HTTP 到 HTTPS 重定向

**核心机制**：利用 Traefik 的 `redirectScheme` 中间件，实现从 HTTP 到 HTTPS 的自动跳转，确保服务访问的安全性与一致性。

## 🧩 架构概览

本方案通过 Docker Compose 部署 Traefik 作为反向代理网关，并结合其内置中间件能力，在不修改后端应用逻辑的前提下，实现对指定服务的透明重定向。后端 Flask 应用仅需关注业务逻辑，由 Traefik 统一处理路由与安全策略。

---

## 📁 `docker-compose.yml` 配置详解

```
# docker-compose.yml
version: '3.8'

services:
  traefik:
    image: traefik:v3.6.6
    command:
      - "--api.insecure=true"                    # 启用不安全模式，开放 Dashboard 调试接口
      - "--providers.docker=true"                # 启用 Docker 服务发现
      - "--providers.docker.exposedbydefault=false" # 不自动暴露所有容器，需显式声明
      - "--entrypoints.web.address=:80"          # 定义 HTTP 入口（端口 80）
      - "--entrypoints.websecure.address=:443"   # 定义 HTTPS 入口（端口 443）
    ports:
      - "80:80"        # HTTP 流量入口
      - "8080:8080"    # Traefik Dashboard（便于监控与调试）
      - "443:443"      # HTTPS 流量入口
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro  # 挂载 Docker 套接字，用于动态发现容器
    restart: unless-stopped

  flask-app:
    build: ./app  # 基于本地 Dockerfile 构建镜像
    labels:
      # 启用 Traefik 代理
      - "traefik.enable=true"

      # 配置 HTTPS 路由：匹配主机名 app1.local，入口为 websecure（443）
      - "traefik.http.routers.flask.rule=Host(`app1.local`)"
      - "traefik.http.routers.flask.entrypoints=websecure"

      # 启用 HTTPS 支持
      - "traefik.http.routers.flask.tls=true"

      # 指定后端服务名称与端口
      - "traefik.http.services.flask-service.loadbalancer.server.port=8001"

      # 显式绑定服务到路由
      - "traefik.http.routers.flask.service=flask-service"

      # 配置 HTTP 到 HTTPS 的重定向
      - "traefik.http.routers.flask-http.rule=Host(`app1.local`)"         # 匹配相同域名
      - "traefik.http.routers.flask-http.entrypoints=web"               # 使用 HTTP 入口
      - "traefik.http.routers.flask-http.middlewares=redirect-to-https"   # 应用重定向中间件

      # 定义重定向策略：跳转至 HTTPS
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
      # 定义重定向中间件,permanent: true 表示返回 301 永久重定向；设为 false 则是 302 临时重定向
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.permanent=true"  # 返回 301 永久重定向

    restart: unless-stopped
```

---

## 🔍 关键配置说明

| 配置项 | 说明 |
| ------ |------ |
| `traefik.http.routers.flask-http.middlewares=redirect-to-https` | 将 HTTP 请求交由 `redirect-to-https` 中间件处理 |
| `redirectscheme.scheme=https` | 指定重定向目标协议为 HTTPS |
| `permanent=true` | 返回 **301 Moved Permanently**，有利于 SEO 且浏览器会缓存跳转 |
| `entrypoints.web` / `websecure` | 分别对应 HTTP 与 HTTPS 入口，需在 Traefik 启动参数中定义 |

⚠️ **注意**：后端服务无需暴露 `ports`，所有流量均由 Traefik 统一入口进入，提升安全性与管理灵活性。

---

## ✅ 实现效果

- 当用户访问 `http://app1.local` → 自动重定向至 `https://app1.local`
- HTTPS 请求由 Traefik 接收并转发至后端 `flask-app:8001`
- 整个过程对应用透明，无需在 Flask 中编写任何路由或重定向逻辑

---

## 📌 总结

通过 Traefik 的 **中间件机制** 与 **Docker 服务发现**，我们实现了：

- **零代码侵入** 的安全重定向
- **动态配置管理**，支持多域名扩展
- **高可维护性**，所有策略集中于 `docker-compose.yml`

该方案适用于生产环境中对安全性与自动化部署有较高要求的微服务架构，是现代云原生应用网关控制的典范实践。

---

📚 *提示：如需启用 Let's Encrypt 自动签发证书，可进一步扩展 *`tls`* 配置块，结合 *`certResolver`* 实现免费 HTTPS。
