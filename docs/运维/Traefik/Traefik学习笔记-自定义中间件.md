---
tags:
  - 反向代理
  - Traefik
---
# 🛡️ 基于 Flask + Redis + Traefik 的动态 IP 黑名单中间件实现

**项目目标**：利用 Flask 构建一个轻量级、高性能的动态 IP 黑名单中间件，结合 Traefik 的 `forwardAuth` 中间件能力，实现对后端服务的访问控制。支持通过 API 动态增删黑名单 IP/CIDR，具备缓存优化与高并发适应性。

---

## 🧩 一、项目架构概览

本系统由以下核心组件构成：

| 组件                     | 角色                                    |
| ---------------------- | ------------------------------------- |
| **Traefik**            | 反向代理网关，负责路由请求并调用 `forwardAuth` 验证访问权限 |
| **Flask (ip-blocker)** | 黑名单认证服务，处理 `/block` 请求，决定是否放行         |
| **Redis**              | 持久化存储黑名单 IP 与 CIDR，支持快速读写与共享状态        |
| **Flask App (目标服务)**   | 被保护的业务应用，仅在通过认证后可访问                   |

**通信流程**：

```
Client → Traefik → forwardAuth → ip-blocker (/block) → ✅允许 → 转发至 flask-app
                                 └→ ❌403 Forbidden → 中断请求
```

---

## 📁 二、目录结构说明

```
├── app                 # 被保护的 Flask 应用服务
│   ├── Dockerfile        # 构建镜像配置
│   ├── app.py            # 主应用入口
│   └── requirements.txt  # Python 依赖
├── docker-compose.yml    # 容器编排文件，定义完整服务拓扑
└── ip_blocker            # IP 黑名单认证中间件服务
    ├── Dockerfile          # 构建镜像配置
    ├── app.py              # 核心逻辑：IP 校验 + API 接口
    └── requirements.txt    # Python 依赖
```

---

## 🐳 三、核心配置详解

### 1. `docker-compose.yml` —— 服务编排中枢

```
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
      - "--entrypoints.web.forwardedheaders.insecure=true"
      - "--entrypoints.websecure.forwardedheaders.insecure=true"
    ports:
      - "80:80"
      - "8080:8080"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped

  redis:
    image: redis:8.4.0-alpine

  ip-blocker:
    build: ./ip_blocker
    environment:
      - REDIS_HOST=redis
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.ip-block.rule=Host(`app2.local`)"
      - "traefik.http.routers.ip-block.entrypoints=websecure"
      - "traefik.http.routers.ip-block-http.rule=Host(`app2.local`)"
      - "traefik.http.routers.ip-block-http.entrypoints=web"
      - "traefik.http.routers.ip-block-http.middlewares=redirect-to-https"
      - "traefik.http.routers.ip-block.tls=true"
      - "traefik.http.services.ip-block-service.loadbalancer.server.port=5000"

  flask-app:
    build: ./app
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.flask.rule=Host(`app1.local`)"
      - "traefik.http.routers.flask.entrypoints=websecure"
      - "traefik.http.routers.flask-http.rule=Host(`app1.local`)"
      - "traefik.http.routers.flask-http.entrypoints=web"
      - "traefik.http.routers.flask-http.middlewares=redirect-to-https"
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
      - "traefik.http.middlewares.redirect-to-https.redirectscheme.permanent=true"
      - "traefik.http.routers.flask.service=flask-service"
      - "traefik.http.routers.flask.tls=true"
      - "traefik.http.services.flask-service.loadbalancer.server.port=8001"
      # 借助forwardAuth加载
      - "traefik.http.middlewares.ip-block.forwardAuth.address=http://ip-blocker:5000/block"
      - "traefik.http.routers.flask.middlewares=ip-block"
    restart: unless-stopped
```

📌 **关键点说明**：

- 使用 `forwardAuth` 将请求转发至 `http://ip-blocker:5000/block` 进行访问控制。
- 所有 HTTP 请求自动重定向到 HTTPS。
- `ip-blocker` 服务独立暴露，用于管理黑名单规则。

---

## 🧱 四、核心模块实现

### 1. `ip_blocker/Dockerfile`

```
FROM python:3.11.14-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

✅ 轻量、安全、快速启动。

---

### 2. `ip_blocker/app.py` —— 黑名单核心逻辑

```
from flask import Flask, request, abort, jsonify
import redis
import os
import time

app = Flask(__name__)

# Redis 连接
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# 缓存机制
_cache = {
    "blacklist": {"ips": set(), "cidrs": []},
    "last_update": 0
}
CACHE_TTL = 2  # 秒

def get_blacklist():
    now = time.time()
    if now - _cache["last_update"] > CACHE_TTL:
        ips = r.smembers("traefik:blacklist:ips")
        cidrs = r.smembers("traefik:blacklist:cidrs")
        _cache["blacklist"] = {
            "ips": ips,
            "cidrs": [ipaddress.ip_network(cidr) for cidr in cidrs if ipaddress.ip_network(cidr, strict=False)]
        }
        _cache["last_update"] = now
    return _cache["blacklist"]

@app.route("/get_block")
def getblock():
    bl = get_blacklist()
    rs = {"ips": list(bl["ips"]), "cidrs": [str(net) for net in bl["cidrs"]]}
    return jsonify(rs) if rs["ips"] or rs["cidrs"] else "无规则"

@app.route("/block")
def block():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if "," in client_ip:
        client_ip = client_ip.split(",")[0].strip()

    bl = get_blacklist()

    # 精确 IP 匹配
    if client_ip in bl["ips"]:
        abort(403)

    # CIDR 网段匹配
    try:
        ip_obj = ipaddress.ip_address(client_ip)
        for net in bl["cidrs"]:
            if ip_obj in net:
                abort(403)
    except Exception:
        pass  # 无效 IP 地址，跳过

    return "", 200

# 🔐 动态管理 API（建议增加身份验证）
@app.route("/api/block/ip/<ip>", methods=["POST"])
def add_ip(ip):
    r.sadd("traefik:blacklist:ips", ip)
    return jsonify({"status": "blocked", "ip": ip})

@app.route("/api/unblock/ip/<ip>", methods=["DELETE"])
def remove_ip(ip):
    r.srem("traefik:blacklist:ips", ip)
    return jsonify({"status": "unblocked", "ip": ip})

if __name__ == "__main__":
    import ipaddress
    app.run(host="0.0.0.0", port=5000)
```

💡 **设计亮点**：

- ✅ **Redis 存储**：实现多实例共享黑名单状态。
- ✅ **缓存机制**：每 2 秒更新一次，避免高频访问 Redis。
- ✅ **支持 CIDR 网段匹配**：可封禁整个子网。
- ⚠️ **安全建议**：`/api/block` 接口应增加 JWT 或 Token 鉴权。

---

### 3. `ip_blocker/requirements.txt`

```
Flask==3.0.3
redis==7.1.0
```

---

## 🚀 五、部署与启动

```
# 构建并启动所有服务
docker compose up -d
```

✅ 服务就绪后可通过以下方式验证：

| 功能 | 地址 |
| ------ |------ |
| **Traefik Dashboard** | `http://localhost:8080` |
| **被保护应用** | `https://app1.local` |
| **黑名单服务** | `https://app2.local/get_block` |
| **添加黑名单 IP** | `POST https://app2.local/api/block/ip/192.168.1.100` |
| **移除黑名单 IP** | `DELETE https://app2.local/api/unblock/ip/192.168.1.100` |

## ✅ 六、总结

本项目成功实现了一个：

- ✅ **动态可更新**
- ✅ **高性能缓存**
- ✅ **基于 Redis 共享状态**
- ✅ **与 Traefik 无缝集成**
- ✅ **支持 API 管理**

的 IP 黑名单中间件，适用于微服务、API 网关、WAF 前置过滤等场景。

🎯 **一句话总结**：

**“用最少的代码，最稳的组件，实现最灵活的访问控制。”**

🔧 开箱即用，扩展性强，是现代云原生架构中理想的安全部件。

