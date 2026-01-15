---
tags:
  - 私有化部署
---
## 介绍

> RustDesk 是一款轻量、开源且完全免费的远程桌面控制软件，功能强大且易于使用。

## 先决条件

在部署 RustDesk 服务器前，请确保满足以下条件：

- 已安装 Docker。
- 防火墙已开放所需端口。

### 端口说明

#### hbbs（信令服务器）
- 21114/TCP：用于 Web 控制台（仅 Pro 版本支持）。
- 21115/TCP：用于 NAT 类型检测。
- 21116/TCP & UDP：
  - UDP：用于客户端 ID 注册与心跳服务。
  - TCP：用于 TCP 打洞及连接建立。
- 21118/TCP：用于支持 Web 客户端。

#### hbbr（中继服务器）
- 21117/TCP：用于中继数据传输。
- 21119/TCP：用于支持 Web 客户端。

> 💡 如果您不需要 Web 客户端功能，可选择性关闭端口 `21118` 和 `21119`。

## 使用 Docker 部署

```bash
sudo docker image pull rustdesk/rustdesk-server

sudo docker run --name hbbs \
  -v ./data:/root \
  -td \
  --net=host \
  --restart unless-stopped \
  rustdesk/rustdesk-server hbbs

sudo docker run --name hbbr \
  -v ./data:/root \
  -td \
  --net=host \
  --restart unless-stopped \
  rustdesk/rustdesk-server hbbr
```

## 使用 Docker Compose 部署

```yaml
services:
  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    volumes:
      - ./data:/root
    network_mode: "host"
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: "host"
    restart: unless-stopped
```

> ⚠️ 注意：由于使用了 `host` 网络模式，容器将直接使用主机网络，因此请确保端口未被其他服务占用。

## 客户端配置

在 RustDesk 客户端中，依次进入：

**设置 → 网络 → 中继服务器**

并填写以下信息：

- **ID 服务器**：`<您的服务器 IP 地址>`
- **中继服务器**：`<您的服务器 IP 地址>`
- **Key**：填写服务器启动后日志中输出的密钥（Key）

> 🔑 该 Key 用于客户端与服务器之间的身份验证，确保通信安全。