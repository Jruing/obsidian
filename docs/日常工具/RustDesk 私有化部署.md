---
title: "RustDesk 私有化部署"
date: 2026-06-09
tags:
  - 日常工具
  - RustDesk
  - 远程桌面
  - 私有化部署
  - Docker
  - Docker-Compose
  - 远程控制
  - 端口配置
  - 自托管
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
## 方式一
### 使用 Docker 部署

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

## 方式二
### 使用 Docker Compose 部署

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

## 方式二（优化版）
### 使用方式
```
mkdir rustdesk
touch docker-compose.yml
touch start.sh
chmod +x start.sh
```

### docker-compose.yml

```
version: '3'

services:
  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:1.1.14
    command: hbbr
    restart: always
    ports:
      - "21117:21117"
    volumes:
      - ./rust-desk:/root
    networks:
      - rustdesk-net

  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:1.1.14
    command: hbbs
    restart: always
    ports:
      - "21115:21115"
      - "21116:21116/tcp"
      - "21116:21116/udp"
    volumes:
      - ./rust-desk:/root
    depends_on:
      - hbbr
    networks:
      - rustdesk-net

networks:
  rustdesk-net:
    driver: bridge
```

### 启动脚本
```
#!/bin/bash

# RustDesk 远程桌面服务启动脚本
# 用于快速部署和管理 RustDesk 服务

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}[信息]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[成功]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[警告]${NC} $1"
}

print_error() {
    echo -e "${RED}[错误]${NC} $1"
}

# 检查 Docker 是否安装
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker 未安装，请先安装 Docker"
        exit 1
    fi
    
    if ! command -v docker compose &> /dev/null; then
        print_error "Docker Compose 未安装，请先安装 Docker Compose"
        exit 1
    fi
}

# 检查端口是否可用
check_ports() {
    print_info "检查端口占用情况..."
    
    local ports=(21115 21116 21117 21118 21119)
    local occupied_ports=()
    
    for port in "${ports[@]}"; do
        if netstat -tuln | grep -q ":$port "; then
            occupied_ports+=($port)
        fi
    done
    
    if [ ${#occupied_ports[@]} -gt 0 ]; then
        print_warning "以下端口已被占用: ${occupied_ports[*]}"
        print_warning "请确保这些端口可用或修改配置文件中的端口设置"
    else
        print_success "所需端口都可用"
    fi
}

# 创建数据目录
create_directories() {
    print_info "创建数据目录..."
    mkdir -p ./data/hbbs ./data/hbbr
    print_success "数据目录创建完成"
}

# 配置防火墙
configure_firewall() {
    print_info "配置防火墙规则..."
    
    # 检查是否有 ufw
    if command -v ufw &> /dev/null; then
        print_info "使用 ufw 配置防火墙..."
        ufw allow 21115/tcp >/dev/null 2>&1 || true
        ufw allow 21116/tcp >/dev/null 2>&1 || true
        ufw allow 21116/udp >/dev/null 2>&1 || true
        ufw allow 21117/tcp >/dev/null 2>&1 || true
        ufw allow 21118/tcp >/dev/null 2>&1 || true
        ufw allow 21119/tcp >/dev/null 2>&1 || true
        print_success "ufw 防火墙规则配置完成"
    elif command -v firewall-cmd &> /dev/null; then
        print_info "使用 firewall-cmd 配置防火墙..."
        firewall-cmd --permanent --add-port=21115/tcp >/dev/null 2>&1 || true
        firewall-cmd --permanent --add-port=21116/tcp >/dev/null 2>&1 || true
        firewall-cmd --permanent --add-port=21116/udp >/dev/null 2>&1 || true
        firewall-cmd --permanent --add-port=21117/tcp >/dev/null 2>&1 || true
        firewall-cmd --permanent --add-port=21118/tcp >/dev/null 2>&1 || true
        firewall-cmd --permanent --add-port=21119/tcp >/dev/null 2>&1 || true
        firewall-cmd --reload >/dev/null 2>&1 || true
        print_success "firewall-cmd 防火墙规则配置完成"
    else
        print_warning "未检测到支持的防火墙工具，请手动配置防火墙"
        print_warning "需要开放端口: 21115-21119 (TCP), 21116 (UDP)"
    fi
}

# 启动服务
start_services() {
    print_info "启动 RustDesk 服务..."
    
    # 拉取最新镜像
    print_info "拉取最新的 Docker 镜像..."
    docker compose pull
    
    # 启动服务
    docker compose up -d
    
    print_success "RustDesk 服务启动完成"
}

# 显示服务状态
show_status() {
    print_info "检查服务状态..."
    sleep 5
    
    echo ""
    print_info "容器状态:"
    docker compose ps
    
    echo ""
    print_info "服务日志 (最近10行):"
    docker compose logs --tail=10
}

# 获取服务器信息
get_server_info() {
    echo ""
    print_info "获取服务器配置信息..."
    
    # 等待密钥文件生成
    local max_wait=30
    local wait_time=0
    
    while [ ! -f "./data/hbbs/id_ed25519.pub" ] && [ $wait_time -lt $max_wait ]; do
        sleep 1
        wait_time=$((wait_time + 1))
    done
    
    if [ -f "./data/hbbs/id_ed25519.pub" ]; then
        local public_key=$(cat ./data/hbbs/id_ed25519.pub)
        local server_ip=$(curl -s ifconfig.me 2>/dev/null || echo "请手动获取服务器公网IP")
        
        echo ""
        print_success "RustDesk 服务器配置信息:"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo -e "📡 ${BLUE}ID 服务器:${NC}     $server_ip:21116"
        echo -e "🔄 ${BLUE}中继服务器:${NC}   $server_ip:21117"
        echo -e "🔑 ${BLUE}服务器密钥:${NC}   $public_key"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        print_info "客户端配置步骤:"
        echo "1. 下载 RustDesk 客户端: https://rustdesk.com/"
        echo "2. 点击 ID 右侧的设置按钮（三个点）"
        echo "3. 选择 'ID/中继服务器'"
        echo "4. 输入上述服务器信息"
        echo ""
    else
        print_warning "密钥文件尚未生成，请稍后运行以下命令获取密钥:"
        echo "cat ./data/hbbs/id_ed25519.pub"
    fi
}

# 显示帮助信息
show_help() {
    echo "RustDesk 远程桌面服务管理脚本"
    echo ""
    echo "用法: $0 [选项]"
    echo ""
    echo "选项:"
    echo "  start     启动 RustDesk 服务"
    echo "  stop      停止 RustDesk 服务"
    echo "  restart   重启 RustDesk 服务"
    echo "  status    查看服务状态"
    echo "  logs      查看服务日志"
    echo "  key       显示服务器密钥"
    echo "  info      显示服务器配置信息"
    echo "  update    更新 RustDesk 服务"
    echo "  help      显示帮助信息"
    echo ""
}

# 主函数
main() {
    local action=${1:-start}
    
    case $action in
        "start")
            print_info "开始部署 RustDesk 远程桌面服务..."
            check_docker
            check_ports
            create_directories
            configure_firewall
            start_services
            show_status
            get_server_info
            ;;
        "stop")
            print_info "停止 RustDesk 服务..."
            docker compose down
            print_success "RustDesk 服务已停止"
            ;;
        "restart")
            print_info "重启 RustDesk 服务..."
            docker compose restart
            print_success "RustDesk 服务已重启"
            ;;
        "status")
            docker compose ps
            ;;
        "logs")
            docker compose logs -f
            ;;
        "key")
            if [ -f "./data/hbbs/id_ed25519.pub" ]; then
                print_info "服务器公钥:"
                cat ./data/hbbs/id_ed25519.pub
            else
                print_error "密钥文件不存在，请先启动服务"
            fi
            ;;
        "info")
            get_server_info
            ;;
        "update")
            print_info "更新 RustDesk 服务..."
            docker compose pull
            docker compose up -d
            print_success "RustDesk 服务更新完成"
            ;;
        "help"|"--help"|"-h")
            show_help
            ;;
        *)
            print_error "未知操作: $action"
            show_help
            exit 1
            ;;
    esac
}

# 进入脚本目录
cd "$(dirname "$0")"

# 执行主函数
main "$@"
```

## 客户端配置

在 RustDesk 客户端中，依次进入：

**设置 → 网络 → 中继服务器**

并填写以下信息：

- **ID 服务器**：`<您的服务器 IP 地址>`
- **中继服务器**：`<您的服务器 IP 地址>`
- **Key**：填写服务器启动后日志中输出的密钥（Key）

> 🔑 该 Key 用于客户端与服务器之间的身份验证，确保通信安全。
