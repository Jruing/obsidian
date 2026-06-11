---
title: "caddy手册"
date: 2026-06-09
tags:
  - 运维
  - Caddy
---

## 1. 什么是 Caddy？

**Caddy** 是一个现代化、高性能的 Web 服务器，支持自动 HTTPS、HTTP/2、IPv6、反向代理等功能。它由 Go 编写，易于部署和管理，特别适合用于现代 Web 应用和服务。

---

## 2. Caddy 的特点

| 特性 | 描述 |
|------|------|
| ✅ 自动 HTTPS | 使用 Let's Encrypt 自动生成并续签证书 |
| ⚡ 高性能 | 基于 Go，原生并发处理能力强 |
| 📄 简洁配置 | Caddyfile 配置语法简单易懂 |
| 🔌 插件系统 | 支持多种插件扩展功能 |
| 🔄 实时热加载 | 修改配置无需重启服务 |
| 🧱 多种部署方式 | 可作为静态二进制、Docker 容器、Kubernetes Ingress 控制器等运行 |

---

## 3. 安装 Caddy

### Linux/macOS（推荐方式）：

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo apt-key add -
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

### Docker 启动：

```bash
docker run -d -p 80:80 -p 443:443 \
    -v $(pwd)/Caddyfile:/etc/caddy/Caddyfile \
    -v caddy_data:/data \
    caddy:latest
```

---

## 4. 基本配置语法

Caddy 使用 `Caddyfile` 进行配置，默认位置：`/etc/caddy/Caddyfile`

### 示例：

```caddy
example.com {
    reverse_proxy http://localhost:3000
}
```

### 多站点配置：

```caddy
example.com {
    root * /var/www/html
    file_server
}

api.example.com {
    reverse_proxy localhost:8080
}
```

---

## 5. 常见功能与模块介绍

| 模块 | 功能说明 |
|------|----------|
| `reverse_proxy` | 反向代理 |
| `file_server` | 静态文件服务 |
| `encode` | 压缩传输（gzip, zstd） |
| `log` | 请求日志记录 |
| `redir` | URL 重定向 |
| `rewrite` | URL 重写 |
| `auth` | 认证中间件（如 basic auth） |
| `headers` | 设置 HTTP 头信息 |
| `tls` | 自定义 TLS 配置 |
| `templates` | 支持 HTML 模板渲染 |

---

## 6. 反向代理配置

### 最简反向代理：

```caddy
example.com {
    reverse_proxy http://localhost:3000
}
```

### 带路径的反向代理：

```caddy
example.com/api {
    reverse_proxy http://localhost:8080
}
```

### 转发请求头：

```caddy
example.com {
    reverse_proxy http://localhost:3000 {
        header_up Host {host}
        header_up X-Real-IP {remote_host}
    }
}
```

---

## 7. HTTPS 自动化

默认情况下，只要域名能解析到你的服务器 IP，Caddy 就会自动申请 Let's Encrypt 证书并启用 HTTPS。

```caddy
example.com {
    reverse_proxy http://localhost:3000
}
```

### 手动指定证书路径：

```caddy
example.com {
    tls /etc/ssl/example.com.crt /etc/ssl/example.com.key
    reverse_proxy http://localhost:3000
}
```

### 强制跳转 HTTPS：

```caddy
http://example.com {
    redir https://{host}{uri} 301
}
```

---

## 8. 静态文件服务

```caddy
example.com {
    root * /var/www/html
    file_server
}
```

### 启用目录浏览：

```caddy
example.com {
    root * /var/www/files
    file_server browse
}
```

### 自定义错误页面：

```caddy
example.com {
    root * /var/www/html
    file_server

    handle_errors {
        @notfound status 404
        rewrite @notfound /404.html
        file_server
    }
}
```

---

## 9. 中间件使用

Caddy 支持多种中间件来增强功能。

### 添加响应头：

```caddy
example.com {
    headers {
        Strict-Transport-Security "max-age=31536000;"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "DENY"
    }

    reverse_proxy http://localhost:3000
}
```

### 压缩传输：

```caddy
example.com {
    encode zstd gzip

    reverse_proxy http://localhost:3000
}
```

---

## 10. 重定向与重写

### 301 重定向：

```caddy
example.com/old-path {
    redir https://example.com/new-path 301
}
```

### URI 重写：

```caddy
example.com {
    rewrite /blog/* /index.php?path={path}

    php_fastcgi unix//run/php/php-fpm.sock
}
```

---

## 11. 负载均衡

```caddy
example.com {
    reverse_proxy lb_policy random http://backend1:3000 http://backend2:3000 {
        health_uri /health
        health_interval 10s
        health_timeout 2s
    }
}
```

支持的负载均衡策略：

- `random`
- `round_robin`
- `least_conn`
- `first`

---

## 12. 身份验证

### Basic Auth 示例：

```bash
# 生成密码
echo "user:$(caddy hash-password --plaintext mypassword)"
```

输出：
```
user:$2a$14$...
```

在配置中使用：

```caddy
example.com/admin {
    basicauth {
        user $2a$14$...
    }

    root * /var/www/admin
    file_server
}
```

---

## 13. 日志与监控

### 启用访问日志：

```caddy
example.com {
    log {
        output file /var/log/caddy/access.log
    }

    reverse_proxy http://localhost:3000
}
```

### 格式化日志字段：

```caddy
log {
    format single_field common_log
}
```

---

## 14. 高级用法

### 匹配器（Matchers）

可用于对特定请求执行操作：

```caddy
@images path *.jpg *.png *.gif
handle @images {
    expire 30d
    file_server
}
```

### 自定义监听地址和端口：

```caddy
:8080 {
    respond "Hello World" 200
}
```

### 多协议支持（HTTP/3）：

```caddy
example.com {
    protocols h1 h2 h3

    reverse_proxy http://localhost:3000
}
```

---

## 15. 完整示例配置

### 示例一：静态网站 + HTTPS + 自定义头

```caddy
example.com {
    root * /var/www/html
    file_server

    headers {
        Strict-Transport-Security "max-age=31536000;"
        X-Content-Type-Options "nosniff"
    }

    encode zstd gzip
}
```

### 示例二：反向代理 + 负载均衡 + 健康检查

```caddy
api.example.com {
    reverse_proxy lb_policy round_robin http://app1:3000 http://app2:3000 {
        health_uri /health
        health_interval 10s
        health_timeout 2s
    }

    headers {
        Access-Control-Allow-Origin "*"
    }
}
```

### 示例三：带 Basic Auth 的后台管理界面

```caddy
admin.example.com {
    basicauth {
        admin $2a$14$...
    }

    root * /var/www/admin
    file_server
}
```

---

## 16. 常见问题解答

### Q1：如何查看 Caddy 是否运行？

```bash
systemctl status caddy
journalctl -u caddy
```

### Q2：如何重新加载配置？

```bash
sudo systemctl reload caddy
```

或使用 API：

```bash
curl -X POST http://localhost:2019/load --data-binary @/etc/caddy/Caddyfile
```

### Q3：如何调试配置？

```bash
caddy validate --config /etc/caddy/Caddyfile
```

---

## 📚 推荐资源

- 官方文档：[https://caddyserver.com/docs/](https://caddyserver.com/docs/)
- Caddyfile 语法参考：[https://caddyserver.com/docs/caddyfile/](https://caddyserver.com/docs/caddyfile/)
- GitHub 仓库：[https://github.com/caddyserver/caddy](https://github.com/caddyserver/caddy)
- 社区论坛：[https://caddy.community/](https://caddy.community/)

---