---
title: "Traefik学习笔记-概念详解（基于 Docker Labels 配置）"
date: 2026-06-09
tags:
  - 运维
  - Traefik
  - Docker
  - Label
---

> 本文档假设你已启用 Traefik 的 Docker Provider，并设置 `exposedByDefault: false`（即容器默认不暴露，需显式打标签）。

```yaml
# traefik.yaml（静态配置）
providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
    exposedByDefault: false
entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"
certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: /etc/traefik/acme.json
      httpChallenge:
        entryPoint: web
```

---

## 1. Provider（提供者）

**作用不变**：Traefik 通过 Docker Provider 监听容器事件。

✅ **关键点**：所有动态配置（Router、Service、Middleware）均通过容器的 **labels** 声明。

---

## 2. Router（路由器）

### 定义
根据规则将请求路由到指定 Service。

### Docker Labels 示例

```yaml
labels:
  # 启用 Traefik
  - "traefik.enable=true"

  # 定义 Router
  - "traefik.http.routers.myapp.rule=Host(`myapp.example.com`) && PathPrefix(`/api`)"
  - "traefik.http.routers.myapp.entrypoints=websecure"
  - "traefik.http.routers.myapp.service=myapp-service"
  - "traefik.http.routers.myapp.middlewares=auth@docker,compress@docker"
```

> ⚠️ 注意：
> - `@docker` 表示该 Middleware 是在 Docker Provider 下定义的（非文件或 Kubernetes）。
> - 多个条件用 `&&` 或 `||` 组合（注意反引号包裹字符串）。
### 其他匹配器
Traefik 的 `rule` 支持多种匹配条件，可单独使用，也可通过逻辑运算符 `&&`（AND）、`||`（OR）和括号 `()` 组合。

> 📌 所有规则必须写在 `traefik.http.routers.<name>.rule` 标签下，字符串需用反引号 `` ` `` 包裹。

#### 1. `Host`
匹配请求的 Host 头（域名）。

```yaml
labels:
  - "traefik.http.routers.app.rule=Host(`app.example.com`)"
```

支持多个域名（OR）：
```yaml
- "traefik.http.routers.app.rule=Host(`app.example.com`) || Host(`www.example.com`)"
```

#### 2. `Path`
精确匹配请求路径（区分大小写，必须完全相等）。

```yaml
- "traefik.http.routers.api.rule=Path(`/health`)"
```

> ✅ 只有 `/health` 能匹配，`/health/` 或 `/healthz` 不行。

#### 3. `PathPrefix`
前缀匹配（最常用），匹配以指定路径开头的请求。

```yaml
- "traefik.http.routers.frontend.rule=PathPrefix(`/static`)"
```

> ✅ 匹配：`/static`, `/static/css/app.css`, `/static/`

#### 4. `Method`
匹配 HTTP 方法（GET、POST、PUT 等）。

```yaml
- "traefik.http.routers.submit.rule=Method(`POST`) && Path(`/submit`)"
```

#### 5. `Header`
检查请求头是否存在且值匹配（精确匹配）。

```yaml
- "traefik.http.routers.admin.rule=Header(`X-Role`, `admin`)"
```

> ✅ 只有当请求包含 `X-Role: admin` 时才匹配。

#### 6. `HeaderRegexp`
使用正则表达式匹配请求头值。

```yaml
- "traefik.http.routers.beta.rule=HeaderRegexp(`User-Agent`, `^Mozilla.*Firefox`)"
```

> ✅ 匹配 Firefox 浏览器的 User-Agent。

#### 7. `Query`
匹配 URL 查询参数（key=value 形式）。

```yaml
- "traefik.http.routers.debug.rule=Query(`debug`, `true`)"
```

> ✅ 匹配：`/page?debug=true`，但不匹配 `?debug=1`。

#### 8. `ClientIP`
匹配客户端 IP 地址（支持 CIDR）。

```yaml
- "traefik.http.routers.internal.rule=ClientIP(`192.168.0.0/16`) || ClientIP(`10.0.0.5`)"
```

> ⚠️ 注意：若 Traefik 前有代理（如 CDN、Nginx），需启用 `forwardedHeaders` 或 `trustedIPs` 才能获取真实 IP。

#### 9. 组合示例（复杂规则）

```yaml
labels:
  - "traefik.http.routers.api-v2.rule=Host(`api.example.com`) && PathPrefix(`/v2`) && Method(`GET`, `POST`) && Header(`Authorization`, ``)"
```

> ✅ 匹配：
> - 域名：`api.example.com`
> - 路径以 `/v2` 开头
> - 方法为 GET 或 POST
> - 包含 `Authorization` 头（值任意，非空即可）

---

## 3. Service（服务）

### a) LoadBalancer（默认类型）

```yaml
labels:
  - "traefik.http.services.myapp-service.loadbalancer.server.port=8080"
  # 如果容器只暴露一个端口，可省略 port；否则必须指定
```

> ✅ Traefik 自动使用容器 IP + 指定端口作为后端地址。

### b) Weighted（蓝绿/金丝雀发布）

先定义两个子服务，再组合：

```yaml
labels:
  # 子服务 v1
  - "traefik.http.services.v1.loadbalancer.server.port=8080"
  # 子服务 v2
  - "traefik.http.services.v2.loadbalancer.server.port=8081"

  # 加权主服务
  - "traefik.http.services.weighted-app.weighted.services.v1.name=v1"
  - "traefik.http.services.weighted-app.weighted.services.v1.weight=90"
  - "traefik.http.services.weighted-app.weighted.services.v2.name=v2"
  - "traefik.http.services.weighted-app.weighted.services.v2.weight=10"

  # Router 指向加权服务
  - "traefik.http.routers.weighted-app.rule=Host(`app.example.com`)"
  - "traefik.http.routers.weighted-app.service=weighted-app"
```

### c) Mirroring（流量复制）

```yaml
labels:
  - "traefik.http.services.primary.loadbalancer.server.port=8080"
  - "traefik.http.services.canary.loadbalancer.server.port=8081"

  - "traefik.http.services.mirror-app.mirroring.service=primary"
  - "traefik.http.services.mirror-app.mirroring.mirrors[0].name=canary"
  - "traefik.http.services.mirror-app.mirroring.mirrors[0].percent=5"

  - "traefik.http.routers.mirror.rule=Host(`mirror.example.com`)"
  - "traefik.http.routers.mirror.service=mirror-app"
```

---

## 4. Middleware（中间件）

### 定义方式
Middleware 必须 **在某个容器上定义**（通常是 Traefik 自身容器，或专用配置容器），并通过 `@docker` 引用。

#### 示例：在 Traefik 容器上定义全局中间件

```yaml
# docker-compose.yml 中 traefik 服务的 labels
services:
  traefik:
    image: traefik:v3.0
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    labels:
      # 压缩中间件
      - "traefik.http.middlewares.compress.compress=true"

      # Basic Auth（密码需用 htpasswd 生成）
      - "traefik.http.middlewares.auth.basicauth.users=admin:$$apr1$$...hash..."

      # 强制 HTTPS 重定向
      - "traefik.http.middlewares.redirect-web-to-websecure.redirectscheme.scheme=https"
      - "traefik.http.middlewares.redirect-web-to-websecure.redirectscheme.permanent=true"

      # 安全头
      - "traefik.http.middlewares.secure-headers.headers.stsSeconds=31536000"
      - "traefik.http.middlewares.secure-headers.headers.forceSTSHeader=true"
      - "traefik.http.middlewares.secure-headers.headers.contentTypeNosniff=true"
```

> 🔒 注意：`$` 在 YAML 中需转义为 `$$`。

### 应用中间件到其他服务

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.app.rule=Host(`app.example.com`)"
  - "traefik.http.routers.app.middlewares=auth@docker,compress@docker,secure-headers@docker"
  - "traefik.http.routers.app.entrypoints=websecure"
  - "traefik.http.routers.app.service=app"
  - "traefik.http.services.app.loadbalancer.server.port=3000"
```
### 常用中间件
除了上述中提到的 `basicAuth`、`compress`、`rateLimiter` 等，以下是一些 **高频实用中间件**：

| 中间件 | 功能 | Docker Labels 示例 |
|-------|------|------------------|
| **`stripPrefix`** | 移除 URL 前缀后再转发给后端 | `- "traefik.http.middlewares.strip-api.stripprefix.prefixes=/api"` |
| **`addPrefix`** | 在路径前添加前缀 | `- "traefik.http.middlewares.add-v1.addprefix.prefix=/v1"` |
| **`replacePath`** | 完全替换请求路径 | `- "traefik.http.middlewares.to-root.replacepath.path=/"` |
| **`replacePathRegex`** | 用正则重写路径 | `- "traefik.http.middlewares.rewrite-api.replacepathregex.regex=^/old/(.*)"``- "traefik.http.middlewares.rewrite-api.replacepathregex.replacement=/new/$$1"` |
| **`ipWhiteList`** | 仅允许特定 IP 访问（类似防火墙） | `- "traefik.http.middlewares.ip-whitelist.ipwhitelist.sourceRange=192.168.1.0/24"``- "traefik.http.middlewares.ip-whitelist.ipwhitelist.sourceRange=203.0.113.42"` |
| **`errors`** | 自定义错误页面（如 500、404） | `- "traefik.http.middlewares.custom-errors.errors.status=500-599"``- "traefik.http.middlewares.custom-errors.errors.service=error-pages"``- "traefik.http.middlewares.custom-errors.errors.query=/error?status={status}"` |
| **`buffering`** | 缓冲请求/响应（防大文件压垮后端） | `- "traefik.http.middlewares.safe-buffer.buffering.maxrequestbytes=4096"``- "traefik.http.middlewares.safe-buffer.buffering.memrequestbytes=2048"` |
| **`inFlightReq`** | 限制并发请求数（防 DDoS） | `- "traefik.http.middlewares.limit-concurrent.inflightreq.amount=10"``- "traefik.http.middlewares.limit-concurrent.inflightreq.sourcecriterion.ipstrategy.depth=1"` |
| **`chain`** | 将多个中间件组合成一个复用单元 | `- "traefik.http.middlewares.secure-chain.chain.middlewares=compress,secure-headers,auth"` |

> 🔔 注意：
> - `$$` 在 YAML 中表示字面 `$`（如正则替换中的 `$1` 需写为 `$$1`）。
> - `ipWhiteList` 和 `inFlightReq` 对安全防护非常有用。
> - `chain` 可简化复杂路由的 middleware 引用。
---

## 5. EntryPoint（入口点）

EntryPoint **只能在静态配置中定义**（如 `traefik.yaml`），但可以在 Docker Labels 中 **引用**。

### 示例：HTTP 自动跳转 HTTPS

在 `traefik.yaml` 中：

```yaml
entryPoints:
  web:
    address: ":80"
    http:
      redirections:
        entryPoint:
          to: websecure
          scheme: https
  websecure:
    address: ":443"
```

然后应用服务只需监听 `websecure`：

```yaml
labels:
  - "traefik.http.routers.myapp.entrypoints=websecure"
```

---

## 6. TLS 与 ACME（Let's Encrypt）

### 自动申请证书（HTTP-01 挑战）

确保：
- `web` EntryPoint 开放（用于 ACME 验证）
- 配置了 `certificatesResolvers`

在应用容器上启用 TLS：

```yaml
labels:
  - "traefik.http.routers.myapp.tls.certresolver=letsencrypt"
  - "traefik.http.routers.myapp.tls.domains[0].main=myapp.example.com"
  # 如需泛域名，需使用 dns-01 挑战
```

> ✅ Traefik 会自动为匹配的 Host 申请并续期证书。

---

## 7. Static vs Dynamic Configuration（Docker 场景）

| 类型 | 内容 | 配置位置 |
|------|------|--------|
| **Static** | entryPoints, providers, log, metrics, ACME | `traefik.yaml` 或 CLI |
| **Dynamic** | routers, services, middlewares | **Docker 容器 labels** |

✅ 所有业务路由逻辑通过 labels 动态注入，无需重启 Traefik。

---

## 8. Dashboard 与 API（通过 Docker Labels 暴露）

### 步骤 1：在 `traefik.yaml` 中启用 API 和 Dashboard

```yaml
api:
  dashboard: true
entryPoints:
  traefik:
    address: ":8080"
```

### 步骤 2：在 Traefik 容器上定义 Dashboard 路由和认证

```yaml
labels:
  # 定义认证中间件（如前文）
  - "traefik.http.middlewares.dashboard-auth.basicauth.users=admin:$$apr1$$...hash..."

  # 创建指向内置 Dashboard 的 Router
  - "traefik.http.routers.dashboard.rule=Host(`traefik.example.com`)"
  - "traefik.http.routers.dashboard.service=api@internal"
  - "traefik.http.routers.dashboard.middlewares=dashboard-auth"
  - "traefik.http.routers.dashboard.entrypoints=traefik"
```

> 🛡️ `api@internal` 是 Traefik 内置服务，不可修改。

---

## 总结：Traefik 数据流（Docker 环境）

```
Client
   ↓
[EntryPoint: :80 / :443] ←─ (traefik.yaml)
   ↓
[Router] ←─ (traefik.http.routers.xxx.rule in labels)
   ↓
[Middleware Chain] ←─ (traefik.http.middlewares.xxx in labels)
   ↓
[Service] ←─ (traefik.http.services.xxx in labels → container IP:port)
   ↓
Your App Container
```


