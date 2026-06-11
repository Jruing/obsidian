---
title: Google ADK - 多工具智能体
date: 2026-03-18
tags:
  - AI
  - 智能体
  - Google ADK
  - 教程
---
## 创建项目
```
adk create multi_tools_agent
```
## 构建一个多工具的智能体(agent.py)
```python
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models import LiteLlm
import datetime
import os
os.environ['OPENAI_API_KEY'] = 'sk-xxxxxxxx'
os.environ['OPENAI_API_BASE'] = 'https://apis.iflow.cn/v1/chat/completions'

# 模型配置
MODEL = LiteLlm(
        model="openai/qwen3-max-preview",
    )

def get_weather(city):
    if city == "北京":
        return "北京天气：下雨"
    else:
        return "不支持除了北京以外的城市查询"

def get_current_datetime():
    return f"当前时间{datetime.datetime.now()}"


root_agent = LlmAgent(
    model=MODEL,
    name='root_agent',
    description='一个支持天气与时间查询的助手',
    instruction='根据使用工具进行查询',
    tools=[get_weather, get_current_datetime], # 定义工具列表
)
```
## 运行
```
adk web
```

![](https://jruing-blogs.oss-cn-beijing.aliyuncs.com/blogs/202603161006.png)