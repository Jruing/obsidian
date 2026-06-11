---
title: Gemini CLI 快速入门
date: 2026-01-27
tags:
  - AI
  - Gemini
  - CLI
---
## 快速入门
Gemini CLI 是一款开源 AI 终端代理，基于 ReAct 推理-行动循环，为开发者提供在本地或远程 MCP 服务器上调用 Gemini 系列模型的能力。您可以借助它完成从代码生成、调试到自动化运维的全流程任务。
## 免费使用
您的旅程从一个慷慨的免费层开始，非常适合实验和轻度使用。

您的免费使用限制取决于您的授权类型。
### 使用 Google 登录（个人 Gemini 代码辅助）

适用于使用 Google 账户验证以访问个人 Gemini 代码辅助的用户。这包括：

    每天每个用户 1000 次模型请求
    每分钟每个用户 60 次模型请求
    模型请求将由 Gemini CLI 确定的 Gemini 模型系列进行处理。

了解更多信息 个人 Gemini 代码辅助限制 。
### 使用 Gemini API 密钥登录（未付费）

如果你使用的是 Gemini API 密钥，你也可以享受免费套餐。这包括：

    每个用户每天 250 次模型请求
    每个用户每分钟 10 次模型请求
    仅限对 Flash 模型发起的模型请求。

了解更多信息 Gemini API 速率限制 .
### 使用 Vertex AI 登录（快速模式）

Vertex AI 提供一种无需启用计费功能的快速模式，包括：

    90天前您需要启用计费。
    配额和模型是可变的，并且特定于您的账户。

## 先决条件
- 操作系统：macOS、Linux 或 Windows
- 运行环境：已安装 Node.js ≥ 18（建议使用 LTS 版本）
- 网络访问：能够访问 Google AI 相关服务（若位于受限网络，可提前配置代理或镜像）
## 安装
### 使用 npm
```
npm install -g @google/gemini-cli
```
### 临时使用
```
npx @google/gemini-cli
```
### 验证安装
```
gemini --version
```
> 首次运行将提示选择配色方案，并要求使用 Google 个人账号或 API Key 进行身份验证。完成登录后，个人账户默认配额为 60 次/分钟、1,000 次/日。

## 常用命令速览
### 查看所有命令
```
gemini help
```
### 检查配置状态
```
gemini status
```
### 管理工具与 MCP
```
/tools
/mcp
```
## 下一步
### 🔧 配置与高级定制
了解环境变量、~/.gemini/settings.json 与 .geminiignore 等配置选项，按需调整模型、代理与文件过滤。

参考链接：[Configuration Guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)

### 🔌 扩展与插件体系
通过 Gemini CLI Extensions 将自定义工具、工作流或第三方 API 注入 CLI，扩展模型能力。

参考链接：[Gemini CLI Extensions](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#gemini_cli_extensions)

### 📖 最佳实践与案例
参考 Google Cloud 官方技术博客，深入了解 GEMINI.md 上下文文件的组织方式、MCP 集成以及团队协作模式。

参考链接：[Getting Started with Gemini CLI](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#gemini_cli_extensions)

## 问题
### 问题1：已完成Google认证依旧无法使用
```
Failed to login. Message: This account requires setting the GOOGLE_CLOUD_PROJECT env var.
```
### 修复方案
1. 打开 https://console.cloud.google.com/
2. 选择一个项目，或者创建一个新项目。然后复制项目ID(注意：一定是项目ID，不是项目编号)。
3. 设置环境变量
```
set GOOGLE_CLOUD_PROJECT=你的项目ID
```
4. API搜索 Gemini for Google Cloud 这个服务并启用