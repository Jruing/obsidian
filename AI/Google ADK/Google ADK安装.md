---
tags:
  - 智能体
---
## 简介
> Agent Development Kit (ADK) 是一个灵活且模块化的框架，用于开发和部署 AI 智能体。虽然针对 Gemini 和 Google 生态系统进行了优化，但 ADK 是模型无关的、部署无关的，并且构建为与其他框架兼容。ADK 旨在使智能体开发感觉更像软件开发，让开发人员更容易创建、部署和编排从简单任务到复杂工作流的智能体架构。

## 官网
> https://adk.wiki
## 安装
```
pip install google-adk 
pip install litellm
```
## 创建智能体项目
```
adk create my_agent
```
## 运行项目
```
adk run my_agent
```
## 通过网页运行/调试
```
adk web --port 8000
```
![](https://adk.wiki/assets/adk-web-dev-ui-chat.png)