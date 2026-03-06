# Jruing 技术学习笔记

这是一个个人技术学习和实践记录的知识库，涵盖了前端开发、后端开发、运维、AI、数据库和Linux等多个技术领域。所有内容均为中文记录，格式统一，便于查阅和学习。

静态站点采用 MkDocs + Material 主题进行部署。

## 📁 项目结构

```
docs/
├── readme.md
├── AI/
│   ├── Agent/
│   │   ├── Agent学习笔记-Skills.md
│   │   ├── Agent学习笔记-自定义数据库查询Skills.md
│   │   ├── AnythingLLM+Ollama搭建本地知识库.md
│   │   ├── LlamaIndex-Agent关联数据库.md
│   │   └── Llamaindex-Agent自然语言查询数据库.md
│   ├── Coze/
│   │   └── 安装 Coze Studio.md
│   ├── Eino/
│   ├── Google ADK/
│   │   ├── Google ADK安装.md
│   │   └── Google ADK实现简历打分助手.md
│   ├── MCP/
│   │   ├── MCP学习笔记-从0到1.md
│   │   ├── MCP学习笔记-天气预报.md
│   │   └── MCP学习笔记-查询主机资源使用情况.md
│   ├── 提示词/
│   │   ├── Banana提示词-文章变成卡通信息图.md
│   │   ├── deepseekR1增强.md
│   │   ├── gork-涩涩.md
│   │   ├── Graphviz工具.md
│   │   ├── NSFW.md
│   │   ├── RooCode角色提示词.md
│   │   ├── 互动式零基础教学.md
│   │   ├── 人类作者模拟器.md
│   │   ├── 八荣八耻.md
│   │   ├── 单词记忆助手.md
│   │   ├── 反向PUA.md
│   │   ├── 叛逆小子.md
│   │   ├── 可视化网页.md
│   │   ├── 天气卡片.md
│   │   ├── 归纳总结.md
│   │   ├── 源文档到SVG幻灯片生成器.md
│   │   ├── 猫娘.md
│   │   ├── 豆包-KFC图片.md
│   │   ├── 豆包-丝控.md
│   │   ├── 豆包-生成架构图.md
│   │   └── 黑白系图片生成.md
│   ├── Claude Code+Claude Code Router.md
│   ├── Docker安装OneAPI.md
│   ├── Gemini-cli.md
│   ├── llms.txt 标准完整教程.md
│   └── OpenCode.md
├── Linux/
│   └── 基础/
│       ├── linux学习笔记-awk.md
│       ├── linux学习笔记-cgroup(一).md
│       ├── linux学习笔记-cgroup(二).md
│       ├── linux学习笔记-grep.md
│       ├── linux学习笔记-iptables.md
│       ├── linux学习笔记-jq.md
│       ├── linux学习笔记-nano用法.md
│       ├── linux学习笔记-ProxyChains4.md
│       ├── linux学习笔记-rsync数据同步.md
│       ├── linux学习笔记-screen.md
│       ├── linux学习笔记-sed手册.md
│       ├── linux学习笔记-SSH隧道代理.md
│       ├── linux学习笔记-sudo.md
│       ├── linux学习笔记-Systemd.md
│       ├── linux学习笔记-tmux.md
│       ├── linux学习笔记-Ubuntu常用软件安装.md
│       ├── linux学习笔记-ufw.md
│       ├── linux学习笔记-免密登录.md
│       ├── linux学习笔记-搭建FTP服务.md
│       ├── linux学习笔记-更换镜像源.md
│       ├── linux学习笔记-服务器基础信息查询脚本.md
│       ├── linux学习笔记-权限管理.md
│       └── linux学习笔记-终端美化-zsh.md
├── 开发/
│   ├── Golang/
│   │   ├── gozero/
│   │   │   ├── api语法.md
│   │   │   └── 安装.md
│   │   ├── 基础/
│   │   │   ├── Golang学习笔记-goto.md
│   │   │   ├── Golang学习笔记-判断.md
│   │   │   ├── Golang学习笔记-变量.md
│   │   │   ├── Golang学习笔记-常量.md
│   │   │   ├── Golang学习笔记-循环.md
│   │   │   └── Golang学习笔记-数据类型.md
│   │   └── 进阶/
│   │       ├── Golang 学习笔记-sqlc 代码生成.md
│   │       ├── Golang 学习笔记-Viper.md
│   │       ├── Golang 学习笔记-结构体与匿名结构体.md
│   │       ├── Golang学习笔记-Casbin学习笔记.md
│   │       ├── Golang学习笔记-CorbaCLI学习笔记.md
│   │       ├── Golang学习笔记-go-resty请求.md
│   │       ├── Golang学习笔记-jwt.md
│   │       ├── Golang学习笔记-令牌桶限流.md
│   │       ├── Golang学习笔记-处理HTTP请求参数.md
│   │       ├── Golang学习笔记-定时任务.md
│   │       ├── Golang学习笔记-自定义日志轮转及输出.md
│   │       └── Golang学习笔记-跨平台编译.md
│   ├── Java/
│   │   └── 基础/
│   │       ├── Java学习笔记-反射.md
│   │       ├── Java学习笔记-异常处理.md
│   │       ├── Java学习笔记-数组操作.md
│   │       ├── Java学习笔记-流程控制.md
│   │       ├── Java学习笔记-程序基础.md
│   │       └── Java学习笔记-面向对象.md
│   ├── Python/
│   │   ├── Web/
│   │   │   ├── Django/
│   │   │   ├── FastAPI/
│   │   │   │   └── 安装.md
│   │   │   └── Flask/
│   │   ├── 基础/
│   │   │   ├── pathlib用法.md
│   │   │   ├── pydantic用法.md
│   │   │   ├── python日志.md
│   │   │   ├── struct用法.md
│   │   │   ├── uv安装Python.md
│   │   │   ├── zipapp用法.md
│   │   │   ├── 函数.md
│   │   │   ├── 判断.md
│   │   │   ├── 安装环境.md
│   │   │   ├── 异常处理.md
│   │   │   ├── 循环.md
│   │   │   ├── 数据类型.md
│   │   │   ├── 模块.md
│   │   │   ├── 类.md
│   │   │   └── 继承与多继承MRO.md
│   │   ├── 数据分析/
│   │   │   └── Pandas用法.md
│   │   ├── 爬虫/
│   │   │   ├── JsRpc练习.md
│   │   │   ├── Python selenium过图片滑块验证.md
│   │   │   ├── Python爬虫-无限VM debugger解决方案.md
│   │   │   ├── 有道翻译爬虫.md
│   │   │   └── 某验五子棋验证码.md
│   │   ├── 自动化/
│   │   │   ├── playwright/
│   │   │   │   ├── playwright基础.md
│   │   │   │   ├── playwright安装.md
│   │   │   │   ├── playwright进阶.md
│   │   │   │   ├── playwright防自动化检测.md
│   │   │   │   └── 目录.md
│   │   │   └── selenium/
│   │   │       └── Selenium接管浏览器.md
│   │   ├── 设计模式/
│   │   │   ├── 单例模式.md
│   │   │   └── 工厂模式.md
│   │   └── 进阶/
│   │       ├── Python学习笔记-__missing__用法.md
│   │       ├── Python学习笔记-Alembic Python数据库迁移教程.md
│   │       ├── Python学习笔记-gc垃圾回收.md
│   │       ├── Python学习笔记-grpc.md
│   │       ├── Python学习笔记-property和setter.md
│   │       ├── Python学习笔记-Schema数据结构及类型校验.md
│   │       ├── Python学习笔记-struct处理二进制数据.md
│   │       ├── Python学习笔记-with上下文管理器.md
│   │       ├── Python学习笔记-yield用法及优点.md
│   │       ├── Python学习笔记-Zipapp打包可执行文件.md
│   │       ├── python学习笔记-偏函数.md
│   │       ├── Python学习笔记-创建虚拟环境及配置.md
│   │       ├── Python学习笔记-参数类型提示.md
│   │       ├── Python学习笔记-实现链式函数调用.md
│   │       ├── Python学习笔记-装饰器.md
│   │       ├── Python学习笔记-读取指定文件指定行.md
│   │       └── Python学习笔记-调用dll.md
│   ├── 前端/
│   │   ├── React/
│   │   │   ├── React-JSX.md
│   │   │   ├── React-Props传递给组件.md
│   │   │   ├── React-列表渲染.md
│   │   │   ├── React-响应事件.md
│   │   │   ├── React-安装.md
│   │   │   ├── React-数据展示.md
│   │   │   ├── React-更新页面数据.md
│   │   │   └── React-条件判断.md
│   │   ├── Vue/
│   │   │   ├── Vue3 Router路由.md
│   │   │   └── Vue3+Vite项目基础环境搭建.md
│   │   └── 基础三剑客/
│   │       └── javascript/
│   │           ├── fetch 学习笔记.md
│   │           ├── forEach数组循环.md
│   │           ├── Javascript学习笔记-js实现拷贝复制功能.md
│   │           ├── js控制台Hook.md
│   │           └── 元素选择器.md
│   └── Jetbrains全家桶激活.md
├── 数据库/
│   ├── MySQL/
│   │   └── Mysql57绿色版安装.md
│   ├── PostgreSQL/
│   │   ├── Postgres学习笔记-Sequence自增序列.md
│   │   └── postgres安装.md
│   └── Redis/
│       ├── Redis7.XCentos集群搭建.md
│       └── 安装及基础.md
├── 日常工具/
│   ├── Frp 内网穿透搭建.md
│   ├── jookdb重置试用期.md
│   ├── RustDesk 私有化部署.md
│   ├── task任务构建工具.md
│   ├── UPX使用方法.md
│   ├── Wiki.js 安装.md
│   ├── win10右键添加复制文件绝对路径.md
│   └── 基于订阅号开发属于自己的微信消息通知.md
└── 运维/
    ├── Caddy/
    │   ├── caddy安装.md
    │   ├── caddy实战-basicauth授权.md
    │   ├── caddy实战-反向代理.md
    │   ├── caddy实战-静态站点.md
    │   ├── caddy实战-黑白名单.md
    │   ├── caddy手册.md
    │   ├── caddy简介.md
    │   └── caddy静态文件.md
    ├── Jenkins/
    │   ├── Freestyle Job.md
    │   ├── Jenkinsfile.md
    │   ├── Pipline.md
    │   ├── Trigger.md
    │   ├── 环境搭建与安装.md
    │   ├── 目录.md
    │   └── 部署Github项目.md
    ├── Minio/
    │   └── 环境搭建与安装.md
    ├── Nginx/
    │   ├── Nginx学习笔记-auth_basic认证.md
    │   ├── Nginx学习笔记-Centos 7 安装Nginx.md
    │   ├── Nginx学习笔记-Nginx简介.md
    │   ├── Nginx学习笔记-图片防盗链.md
    │   ├── Nginx学习笔记-解决前端后端跨域.md
    │   ├── Nginx学习笔记-负载均衡配置.md
    │   ├── Nginx学习笔记-部署静态页面实践.md
    │   ├── Nginx学习笔记-配置文件详解.md
    │   ├── Nginx学习笔记-黑名单-白名单.md
    │   └── 环境搭建与安装.md
    ├── Serverless/
    │   └── ServerLess学习笔记-FnProject完整指南.md
    ├── Traefik/
    │   ├── Traefik学习笔记-安装.md
    │   ├── Traefik学习笔记-概念详解（基于 Docker Labels 配置）.md
    │   ├── Traefik学习笔记-自定义中间件.md
    │   └── Traefik学习笔记-重定向配置.md
    ├── 容器化/
    │   ├── Docker/
    │   │   ├── Docker Swarm 学习笔记.md
    │   │   ├── Docker-Compose安装.md
    │   │   ├── Docker学习笔记-redis部署.md
    │   │   ├── Docker学习笔记-在线安装教程.md
    │   │   ├── Docker学习笔记-多阶段构建学习笔记.md
    │   │   ├── Docker学习笔记-安装Nginx及实践应用.md
    │   │   ├── Docker学习笔记-容器镜像导入导出.md
    │   │   ├── Docker学习笔记-构建私有镜像仓库.md
    │   │   ├── Docker学习笔记-镜像体积缩小.md
    │   │   └── 环境搭建与安装.md
    │   └── Kubernetes/
    │       ├── kubernetes学习笔记-ConfigMap.md
    │       ├── kubernetes学习笔记-Deployment.md
    │       ├── kubernetes学习笔记-helm.md
    │       ├── kubernetes学习笔记-Ingress.md
    │       ├── kubernetes学习笔记-namespace.md
    │       ├── kubernetes学习笔记-Pod.md
    │       ├── kubernetes学习笔记-ReplicaSet.md
    │       ├── kubernetes学习笔记-Service.md
    │       ├── kubernetes学习笔记-安装.md
    │       └── 目录.md
    ├── 监控/
    │   ├── Prometheus/
    │   │   ├── Prometheus学习笔记-file_sd_config.md
    │   │   ├── Prometheus学习笔记-Grafana可视化.md
    │   │   ├── Prometheus学习笔记-Label标签.md
    │   │   ├── Prometheus学习笔记-告警规则配置.md
    │   │   ├── Prometheus学习笔记-安装.md
    │   │   ├── Prometheus学习笔记-安装blackbox_exporter.md
    │   │   ├── Prometheus学习笔记-安装Node_exporter.md
    │   │   ├── Prometheus学习笔记-监控docker容器.md
    │   │   ├── Prometheus学习笔记-设置Basic_auth登录校验.md
    │   │   └── Prometheus学习笔记-配置文件字段解析.md
    │   ├── 日志监控/
    │   │   └── 基于Grafana+Loki+Promatil搭建日志分析平台.md
    │   └── Uptime-kuma 监控.md
    ├── 进程管理/
    │   └── Supervisor 学习笔记.md
    ├── IP划分.md
    └── Neo4j 实现一个简单的CMDB管理平台.md
```

## 📊 项目统计

- **总文件数量**: 229 个 Markdown 文件
- **主要分类**: 6 个核心技术领域

## 🚀 快速导航

### 开发
- **前端**: JavaScript基础、React、Vue
- **后端**: Golang、Python、Java
- **自动化**: Playwright、Selenium 测试框架

### 运维
- **监控**: Prometheus、Grafana、Uptime-kuma
- **容器化**: Docker、Kubernetes、Helm
- **CI/CD**: Jenkins、Traefik、Nginx、Caddy
- **进程管理**: Supervisor

### AI
- **AI工具**: Claude、Gemini、Google ADK、Coze
- **Agent**: LlamaIndex、AnythingLLM
- **MCP**: Model Context Protocol 学习笔记
- **提示词**: 多种AI提示词模板和技巧

### 数据库
- **MySQL、PostgreSQL、Redis**

### Linux
- **基础命令**: 20+ 个常用Linux命令和配置

## 📝 使用说明

1. **搜索**: 使用 Obsidian 的搜索功能快速查找相关内容
2. **标签**: 每个文件都包含相关标签，便于分类查找
3. **链接**: 文档之间有相互链接，便于知识体系构建

## 🔧 技术栈

- **笔记工具**: Obsidian
- **版本控制**: Git
- **静态站点**: MkDocs + Material 主题
- **内容格式**: Markdown

## 📄 许可证

本项目为个人学习笔记，仅供学习交流使用。

---

*最后更新: 2026-03-06*
