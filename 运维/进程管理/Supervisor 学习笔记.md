---
tags:
  - 进程管理
---

## 一、Supervisor 背景介绍

Supervisor 是一个 **进程管理工具**，主要用于在 Linux/Unix 系统中 **管理和守护后台服务进程**。

它可以做到：

* 程序异常退出后 **自动重启**
* 统一管理多个进程（启动 / 停止 / 重启 / 查看状态）
* 提供 **Web 管理界面**
* 支持日志管理

Supervisor 本身是用 **Python** 编写的，稳定、成熟，在生产环境中非常常见。

---

## 二、应用场景

Supervisor 常见使用场景包括：

### 1. Web 服务守护

* Flask / Django / FastAPI
* Gunicorn / Uvicorn

### 2. 后台任务

* Celery worker
* 定时任务脚本
* 消息队列消费者

### 3. 非 systemd 环境

* Docker 容器内
* 老系统或精简系统

### 4. 多进程统一管理

* 同一台机器跑多个服务
* 开发 / 测试 / 生产环境

---

## 三、安装 Supervisor

### 方式一：使用系统包管理器（推荐）

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install supervisor -y
```

#### CentOS / Rocky / AlmaLinux

```bash
sudo yum install epel-release -y
sudo yum install supervisor -y
```

安装完成后通常会自动启动：

```bash
systemctl status supervisord
```

---

### 方式二：pip 安装

```bash
pip install supervisor
```

生成配置文件：

```bash
echo_supervisord_conf > /etc/supervisord.conf
```

启动：

```bash
supervisord -c /etc/supervisord.conf
```

---

## 四、Supervisor 核心组件

| 组件            | 作用       |
| ------------- | -------- |
| supervisord   | 后台守护进程   |
| supervisorctl | 命令行管理工具  |
| 配置文件          | 定义要管理的程序 |
| Web UI        | 浏览器管理界面  |

---

## 五、目录结构（常见）

```text
/etc/supervisor/
├── supervisord.conf
└── conf.d/
    ├── flask.conf
    ├── celery.conf
    └── xxx.conf
```

`conf.d` 中每个 `.conf` 文件代表一个或一组程序。

---

## 六、Supervisor 基本使用

### 1. 常用命令

```bash
supervisorctl status      # 查看状态
supervisorctl start all   # 启动所有
supervisorctl stop all    # 停止所有
supervisorctl restart all # 重启所有
```

单个程序：

```bash
supervisorctl start flask_app
```

---

### 2. 重新加载配置

```bash
supervisorctl reread   # 读取新配置
supervisorctl update   # 应用配置变更
```

---

## 七、配置文件详解

### 1. 全局配置（supervisord.conf）

```ini
[supervisord]
logfile=/var/log/supervisord.log
pidfile=/var/run/supervisord.pid

[unix_http_server]
file=/var/run/supervisor.sock
chmod=0700

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock

[include]
files = /etc/supervisor/conf.d/*.conf
```

---

### 2. Program 配置参数说明

```ini
[program:demo]
command=python app.py
directory=/opt/demo
autostart=true
autorestart=true
startsecs=5
user=www-data
stdout_logfile=/var/log/demo.out.log
stderr_logfile=/var/log/demo.err.log
environment=ENV=prod,DEBUG=false
```

#### 常用参数说明

| 参数             | 说明                  |
| -------------- | ------------------- |
| command        | 启动命令                |
| directory      | 工作目录                |
| autostart      | supervisord 启动时自动启动 |
| autorestart    | 异常退出自动重启            |
| startsecs      | 运行多少秒视为成功           |
| user           | 运行用户                |
| stdout_logfile | 标准输出日志              |
| stderr_logfile | 错误日志                |
| environment    | 环境变量                |

---

## 八、Web 管理界面配置

### 1. 启用 Web UI

在 `supervisord.conf` 中添加：

```ini
[inet_http_server]
port=0.0.0.0:9001
username=admin
password=admin123
```

重启 Supervisor：

```bash
systemctl restart supervisord
```

### 2. 访问 Web UI

浏览器访问：

```text
http://服务器IP:9001
```

功能：

* 查看进程状态
* 启停 / 重启进程
* 查看日志

⚠️ **生产环境请限制访问 IP 或使用强密码**

---

## 九、Flask Demo + Supervisor 实战

### 1. Flask 示例代码

`app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Supervisor + Flask"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 2. Supervisor 配置 Flask

`/etc/supervisor/conf.d/flask_demo.conf`

```ini
[program:flask_demo]
command=/usr/bin/python3 app.py
directory=/opt/flask_demo
autostart=true
autorestart=true
startsecs=3
user=www-data
stdout_logfile=/var/log/flask_demo.out.log
stderr_logfile=/var/log/flask_demo.err.log
environment=FLASK_ENV=production
```

---

### 3. 启动 Flask 服务

```bash
supervisorctl reread
supervisorctl update
supervisorctl start flask_demo
```

访问：

```text
http://服务器IP:5000
```

---

## 十、Supervisor + Gunicorn（推荐生产方式）

```ini
[program:flask_gunicorn]
command=gunicorn -w 4 -b 0.0.0.0:8000 app:app
directory=/opt/flask_demo
autostart=true
autorestart=true
stdout_logfile=/var/log/gunicorn.out.log
stderr_logfile=/var/log/gunicorn.err.log
```

---

## 十一、常见问题

### 1. 程序启动后立刻退出

* command 写错
* 端口被占用
* 缺少虚拟环境路径

### 2. 虚拟环境问题

```ini
command=/opt/venv/bin/gunicorn app:app
environment=PATH="/opt/venv/bin"
```

---

## 十二、Supervisor vs systemd

| 对比     | Supervisor | systemd |
| ------ | ---------- | ------- |
| 易用性    | ⭐⭐⭐⭐       | ⭐⭐⭐     |
| Web UI | 支持         | 不支持     |
| 容器友好   | 好          | 一般      |
| 系统级    | 否          | 是       |

---

## 十三、生产级配置规范（推荐）

本节给出 **生产环境可直接使用的 Supervisor 配置规范**，重点关注：

* 稳定性
* 可观测性（日志）
* 安全性
* 可维护性

---

### 1. supervisord.conf（生产模板）

```ini
[supervisord]
logfile=/var/log/supervisor/supervisord.log
logfile_maxbytes=50MB
logfile_backups=10
loglevel=info
pidfile=/var/run/supervisord.pid
nodaemon=false
minfds=1024
minprocs=200

[unix_http_server]
file=/var/run/supervisor.sock
chmod=0700
chown=root:root

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock

[include]
files = /etc/supervisor/conf.d/*.conf
```

目录准备：

```bash
mkdir -p /var/log/supervisor
```

---

### 2. Program 通用生产模板

```ini
[program:app_name]
command=/opt/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
directory=/opt/app
autostart=true
autorestart=true
startsecs=10
startretries=3
stopsignal=TERM
stopwaitsecs=30
killasgroup=true
stopasgroup=true
user=www-data
environment=ENV=prod,PYTHONUNBUFFERED=1

stdout_logfile=/var/log/app/app.out.log
stdout_logfile_maxbytes=100MB
stdout_logfile_backups=10
stderr_logfile=/var/log/app/app.err.log
stderr_logfile_maxbytes=100MB
stderr_logfile_backups=10
```

日志目录：

```bash
mkdir -p /var/log/app
chown -R www-data:www-data /var/log/app
```

---

## 十四、日志轮转（Logrotate）方案（生产必备）

Supervisor **自身日志轮转能力有限**，生产环境推荐结合 `logrotate`。

---

### 1. Logrotate 配置示例

创建文件：

```bash
/etc/logrotate.d/app
```

内容：

```conf
/var/log/app/*.log {
    daily
    rotate 14
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
    dateext
}
```

参数说明：

| 参数           | 含义         |
| ------------ | ---------- |
| daily        | 每天轮转       |
| rotate 14    | 保留 14 份    |
| compress     | gzip 压缩    |
| copytruncate | 不重启进程即可切日志 |
| dateext      | 文件名带日期     |

---

### 2. 验证日志轮转

```bash
logrotate -f /etc/logrotate.d/app
```

---

## 十五、生产环境最佳实践

### 1. 不直接暴露 Flask

* 使用 Gunicorn / Uvicorn
* Nginx 作为反向代理

### 2. 不使用 root 运行

* 统一 www-data / app 用户

### 3. Supervisor 只做进程管理

* 不做配置中心
* 不做日志分析

### 4. Web UI 安全

```ini
[inet_http_server]
port=127.0.0.1:9001
username=strong_user
password=strong_password
```

配合：

* SSH 隧道
* 内网访问

---

## 十六、完整 Flask + Gunicorn + Supervisor（生产示例）

```ini
[program:flask_prod]
command=/opt/venv/bin/gunicorn -w 4 -k gthread -t 60 \
    -b 127.0.0.1:8000 app:app
directory=/opt/flask_demo
autostart=true
autorestart=true
startsecs=10
user=www-data
stdout_logfile=/var/log/flask/flask.out.log
stderr_logfile=/var/log/flask/flask.err.log
environment=FLASK_ENV=production,PYTHONUNBUFFERED=1
```

---

## 十七、总结

Supervisor 在生产环境中适合：

* Python Web / Worker 进程
* 中小规模服务管理
* 容器或非 systemd 场景

**推荐组合：**

> Nginx + Gunicorn + Flask + Supervisor + Logrotate

