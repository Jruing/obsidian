---
title: "ServerLess学习笔记-FnProject完整指南"
date: 2026-06-09
tags:
  - 运维
  - Serverless
---

## FnProject介绍

Fn 是一个事件驱动的开源功能即服务 FaaS计算平台，您可以在任何地方运行。它的一些主要特点：

- ✅ **开源**：完全开源，可自由使用和修改
- 🐳 **原生 Docker**：使用任何 Docker 容器作为你的函数
- 🌍 **支持所有语言**：Python、Go、Java、Node.js等
- 🚀 **随处运行**：
  - 公有云、私有云和混合云
  - 导入 Lambda 函数并在任何地方运行它们
- 👨‍💻 **易于开发人员使用**
- 🔧 **易于操作员管理**
- 📈 **简单而强大的可扩展性**

### 官方文档
https://fnproject.io/tutorials/

---

## 环境准备

### 前提条件

- ✅ Docker 17.10.0-ce 或更高版本
- 📦 注册DockerHub账号（非必须，如果使用本地模式则不需要，如果需要将服务推动到仓库则需要）

### 系统要求

- Linux/macOS/Windows
- 至少4GB RAM
- 至少2GB 可用磁盘空间

---

## 安装部署

### Linux安装

#### 方式1：通过脚本安装（推荐）

```bash
curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh
```

#### 方式2：二进制安装

```bash
# 下载
wget -O fn https://github.com/fnproject/fn/releases/download/0.3.25/fn_linux

# 赋予可执行权限
chmod +x fn

# 移动到系统路径
sudo mv fn /usr/local/bin/
```

### 验证安装

```bash
fn --version
```

### 启动服务

```bash
# 启动命令
fn start

# 注意：默认使用8080端口及2375端口
# 若想修改为其他的端口需要执行：
fn start -p 8081

# 配置环境变量
export FN_API_URL=http://127.0.0.1:8081
```

### 服务启动日志示例

```
2023/10/19 18:02:02 ¡¡¡ 'fn start' should NOT be used for PRODUCTION !!! see https://github.com/fnproject/fn-helm/
time="2023-10-19T10:02:02Z" level=info msg="Setting log level to" fields.level=info
time="2023-10-19T10:02:02Z" level=info msg="Registering data store provider 'sql'"
time="2023-10-19T10:02:02Z" level=info msg="Connecting to DB" url="sqlite3:///app/data/fn.db"
time="2023-10-19T10:02:02Z" level=info msg="Fn serving on `:8080`" type=full version=0.3.750
```

### 停止服务

```bash
fn stop
```

---

## 基本使用

### 初始化函数目录

```bash
# 初始化 fn_demo1
fn init --runtime python fn_demo1

# 初始化 fn_demo2
fn init --runtime python fn_demo2
```

### 创建应用

```bash
fn create app fn_app
```

### 修改函数代码

#### func.py 示例

```python
import io
import json
import logging
from fdk import response

def handler(ctx, data: io.BytesIO = None):
    name = "fn_demo1"  # 将此处的World修改为fn_demo1方便测试调用后的展示结果
    
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))
    
    logging.getLogger().info("Inside Python Hello World function")
    
    return response.Response(
        ctx, 
        response_data=json.dumps({"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
```

#### func.yaml 配置文件字段详解

```yaml
schema_version: 20180708  # 标识此函数文件的架构版本
name: fn_demo1           # 函数的名称。与目录名称匹配
version: 0.0.1           # 版本号：从 0.0.1 自动开始
runtime: python          # 运行时设置的语言环境
entrypoint: /python/bin/fdk /function/func.py handler  # 调用函数时要调用的可执行文件的名称
memory: 256              # 函数的最大内存大小，单位：MB
timeout: 30              # 函数执行超时时间，单位：秒
idle_timeout: 30         # 函数空闲超时时间，单位：秒
```

### 部署应用/函数

```bash
# 进入函数目录
cd fn_demo1/

# 部署函数
fn --verbose deploy --app fn_app --local
```

### 部署日志示例

```
Deploying fn_demo1 to app: fn_app
Bumped to version 0.0.4
Using Container engine docker
Building image fn_demo1:0.0.4 
[+] Building 120.6s (17/17) FINISHED
 => [internal] load build definition from Dockerfile
 => [build-stage 1/6] FROM fnproject/python:3.9-dev
 => [stage-1 1/5] FROM fnproject/python:3.9
 => [build-stage 4/6] RUN pip3 install --target /python/ --no-cache --no-cache-dir -r requirements.txt
 => [stage-1 5/5] RUN chmod -R o+r /function
 => exporting to image
 => => writing image sha256:5700ac5e7fc00f10b9c812292283184c25be858c8cf537e9b15d1d3dec80ef96
 => => naming to docker.io/library/fn_demo1:0.0.1

Updating function fn_demo1 using image fn_demo1:0.0.1...
```

### 查看生成的服务镜像

```bash
docker images
```

### 查看函数信息

```bash
fn inspect function fn_app fn_demo1
```

### 查看部署后的函数信息示例

```json
{
  "annotations": {
    "fnproject.io/fn/invokeEndpoint": "http://localhost:8080/invoke/01HD66V4V6NG8G00RZJ000000H"
  },
  "app_id": "01HD65NGGGNG8G00RZJ000000G",
  "created_at": "2023-10-20T09:32:11.494Z",
  "id": "01HD66V4V6NG8G00RZJ000000H",
  "idle_timeout": 30,
  "image": "fn_demo1:0.0.4",
  "memory": 256,
  "name": "fn_demo1",
  "timeout": 30,
  "updated_at": "2023-10-20T09:32:11.494Z"
}
```

---

## 常用命令

### 启动/停止

```bash
# 启动
fn start

# 停止
fn stop
```

### 创建

```bash
# 创建应用
fn create app <app-name>

# 创建函数
fn create function <app-name> <function-name>

# 创建触发器
fn create trigger <app-name> <function-name>
```

### 查询

```bash
# 列出所有应用
fn list apps

# 列出应用关联的函数
fn list functions <app-name>

# 列出所有的触发器
fn list triggers

# 查询函数详情
fn inspect function <app-name> <function-name>

# 列出应用的配置
fn list config <app-name>
```

### 删除

```bash
# 删除应用
fn delete app <app-name>

# 删除函数
fn delete function <app-name> <function-name>

# 删除触发器
fn delete trigger <app-name> <function-name>
```

### 调用

#### 通过CLI调用

```bash
fn invoke <app-name> <function-name>
```

#### 通过Curl调用

```bash
curl -X "POST" -H "Content-Type: application/json" -d '{"name":"fn_demo1"}' http://localhost:8080/invoke/01HD66V4V6NG8G00RZJ000000H
```

---

## 函数调用示例

### 通过fn调用函数

```bash
# 调用 fn_demo1
fn invoke fn_app fn_demo1
# 输出: {"message": "Hello fn_demo1"}

# 调用 fn_demo2
fn invoke fn_app fn_demo2
# 输出: {"message": "Hello fn_demo2"}
```

### 通过Curl调用函数

```bash
# 调用 fn_demo1
curl -X "POST" -H "Content-Type: application/json" -d '{"name":"fn_demo1"}' http://localhost:8080/invoke/01HD66V4V6NG8G00RZJ000000H
# 输出: {"message": "Hello fn_demo1"}

# 调用 fn_demo2
curl -X "POST" -H "Content-Type: application/json" -d '{"name":"fn_demo2"}' http://localhost:8080/invoke/01HD66XF41NG8G00RZJ000000J
# 输出: {"message": "Hello fn_demo2"}
```

---

## 最佳实践

### 1. 项目结构

```
serverless/
├── fn_app/
│   ├── fn_demo1/
│   │   ├── func.py
│   │   ├── func.yaml
│   │   └── requirements.txt
│   └── fn_demo2/
│       ├── func.py
│       ├── func.yaml
│       └── requirements.txt
└── fn_app.yaml
```

### 2. 环境变量管理

```bash
# 设置应用配置
fn config app fn_app FN_RUNTIME python

# 设置函数配置
fn config function fn_app fn_demo1 FN_MEMORY 512
```

### 3. 日志管理

```python
import logging

# 启用日志
logging.getLogger().setLevel(logging.INFO)

# 记录日志
logging.getLogger().info("函数执行开始")
logging.getLogger().error("发生错误")
```

### 4. 错误处理

```python
import json

def handler(ctx, data: io.BytesIO = None):
    try:
        body = json.loads(data.getvalue())
        # 处理业务逻辑
    except json.JSONDecodeError as ex:
        logging.getLogger().error(f"JSON解析错误: {ex}")
        return response.Response(ctx, response_data=json.dumps({"error": "Invalid JSON"}))
    except Exception as ex:
        logging.getLogger().error(f"处理错误: {ex}")
        return response.Response(ctx, response_data=json.dumps({"error": "处理失败"}))
```

### 5. 性能优化

- ✅ 合理设置内存大小（建议256-1024MB）
- ⏱️ 设置合适的超时时间
- 🐳 使用轻量级基础镜像
- 📦 减少依赖包数量
- 🔍 使用Docker多阶段构建

### 6. 安全建议

- 🔐 不要在代码中硬编码敏感信息
- 🔑 使用环境变量存储配置
- 🛡️ 限制函数权限
- 🔍 定期更新依赖包

### 7. 监控和调试

```bash
# 查看函数调用日志
fn logs <app-name> <function-name>

# 查看系统日志
docker logs fn
```

---

## 故障排查

### 常见问题

1. **Docker权限问题**
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

2. **端口占用**
   ```bash
   # 检查端口占用
   lsof -i :8080
   
   # 使用其他端口
   fn start -p 8081
   ```

3. **函数部署失败**
   - 检查Dockerfile语法
   - 验证依赖包版本
   - 检查网络连接

4. **内存不足**
   - 减少函数内存设置
   - 优化代码逻辑
   - 检查系统资源

### 调试技巧

1. 使用 `fn logs` 查看实时日志
2. 在函数中添加详细日志输出
3. 使用 `fn inspect` 查看函数状态
4. 检查Docker镜像构建日志

---

## 相关资源

- 📖 [FnProject官方文档](https://fnproject.io/tutorials/)
- 🐳 [Docker官方文档](https://docs.docker.com/)
- 📦 [Python FDK](https://github.com/fnproject/python-fdk)
- 🎯 [FnProject GitHub](https://github.com/fnproject/fn)

---

**最后更新**: 2023-10-20
**版本**: v1.0.0