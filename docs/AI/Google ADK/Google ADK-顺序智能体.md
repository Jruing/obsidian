---
title: Google ADK - 顺序智能体
date: 2026-03-18
tags:
  - AI
  - 智能体
  - Google ADK
  - 教程
---
## 创建项目
```
adk create seq_agent
```
## 构建一个顺序智能体(agent.py)
```python
"""
每日健康助手 - Daily Health Assistant
按顺序执行：问候用户 → 获取天气 → 建议穿衣 → 提醒喝水 → 道别
"""
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.models import LiteLlm
import datetime
import os
os.environ['OPENAI_API_KEY'] = 'sk-xxxxx'
os.environ['OPENAI_API_BASE'] = 'https://apis.iflow.cn/v1/chat/completions'

# 模型配置
MODEL = LiteLlm(
        model="openai/qwen3-max-preview",
    )


def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    # 模拟天气数据
    weather_data = {
        "北京": "晴天，气温 18°C，空气质量良好",
        "上海": "多云，气温 22°C，有轻微雾霾",
        "广州": "小雨，气温 26°C，湿度较高",
        "深圳": "阴天，气温 25°C，空气清新",
        "成都": "晴天，气温 20°C，适合户外活动",
    }
    return weather_data.get(city, f"{city}：晴天，气温 20°C")


def get_current_datetime() -> str:
    """获取当前日期和时间"""
    now = datetime.datetime.now()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return f"{now.strftime('%Y年%m月%d日')} {weekdays[now.weekday()]} {now.strftime('%H:%M')}"


# ============================================================================
# 步骤1: 问候用户
# ============================================================================
greeting_agent = LlmAgent(
    model=MODEL,
    name="greeting_agent",
    description="问候用户，了解基本信息",
    instruction="""
你是每日健康助手的问候模块。

## 你的任务
1. 使用 get_current_datetime 工具获取当前时间
2. 以温暖友好的方式问候用户
3. 询问用户所在的城市（用于后续天气查询）

## 输出格式
### 🌅 问候
[根据时间段（早/中/晚）给出恰当的问候]

### ⏰ 当前时间
[显示当前日期和时间]

### 📍 城市询问
[礼貌询问用户所在城市]

---
用温暖亲切的语气，使用中文输出。假设用户回复"北京"。
""",
    tools=[get_current_datetime],
    output_key="greeting_result",
)

# ============================================================================
# 步骤2: 获取当前天气
# ============================================================================
weather_agent = LlmAgent(
    model=MODEL,
    name="weather_agent",
    description="获取用户所在城市的天气信息",
    instruction="""
你是每日健康助手的天气查询模块。

## 上下文
用户刚刚完成问候，用户信息如下：
{greeting_result}

## 你的任务
1. 使用 get_weather 工具获取用户城市的天气
2. 城市默认使用"北京"
3. 整理并呈现天气信息

## 输出格式
### 🌤️ 天气预报
- 城市：[城市名称]
- 天气：[天气状况]
- 气温：[温度]
- 建议：[简单的出行建议]

---
用清晰明了的语气，使用中文输出。
""",
    tools=[get_weather],
    output_key="weather_result",
)

# ============================================================================
# 步骤3: 建议穿衣
# ============================================================================
clothing_agent = LlmAgent(
    model=MODEL,
    name="clothing_agent",
    description="根据天气给出穿衣建议",
    instruction="""
你是每日健康助手的穿衣建议模块。

## 上下文
当前天气信息如下：
{weather_result}

## 你的任务
根据天气情况，为用户提供今日穿衣建议。

## 输出格式
### 👔 今日穿搭建议

**上衣**：[建议穿着的上衣类型]

**下装**：[建议穿着的裤子/裙子]

**外套**：[是否需要外套，及外套类型]

**配饰**：[帽子、雨伞、防晒等建议]

### 💡 温馨提示
[根据天气的特殊提醒，如防晒、带伞等]

---
用贴心细致的语气，使用中文输出。
""",
    output_key="clothing_result",
)

# ============================================================================
# 步骤4: 提醒喝水
# ============================================================================
hydration_agent = LlmAgent(
    model=MODEL,
    name="hydration_agent",
    description="提醒用户保持水分摄入",
    instruction="""
你是每日健康助手的水分提醒模块。

## 上下文
今日天气情况：
{weather_result}

## 你的任务
1. 根据天气情况，给出今日饮水建议
2. 提供健康饮水小贴士

## 输出格式
### 💧 今日饮水计划

**建议饮水量**：[根据天气推荐的每日饮水量]

**饮水时间表**：
- 早晨起床后：一杯温水
- 上午：[具体建议]
- 午餐后：[具体建议]
- 下午：[具体建议]
- 晚餐前：[具体建议]
- 睡前：[少量温水]

### 🌿 健康小贴士
[关于健康饮水的2-3个小贴士]

---
用关心健康的语气，使用中文输出。
""",
    output_key="hydration_result",
)

# ============================================================================
# 步骤5: 道别
# ============================================================================
farewell_agent = LlmAgent(
    model=MODEL,
    name="farewell_agent",
    description="结束对话，送上祝福",
    instruction="""
你是每日健康助手的道别模块。

## 上下文
今日健康建议汇总：
- 问候信息：{greeting_result}
- 天气情况：{weather_result}
- 穿衣建议：{clothing_result}
- 饮水提醒：{hydration_result}

## 你的任务
1. 简要总结今日健康建议要点
2. 给用户送上美好祝福
3. 友好道别

## 输出格式
### 📋 今日健康摘要
[用简洁的列表总结今日建议]

### 🌈 美好祝愿
[给用户送上正能量祝福]

### 👋 告别语
[温暖的道别，期待明天再见]

---
用温暖真诚的语气，使用中文输出。
""",
    output_key="farewell_result",
)

# ============================================================================
# 组装 SequentialAgent
# ============================================================================
root_agent = SequentialAgent(
    name="daily_health_assistant",
    description="每日健康助手：按顺序执行问候→天气→穿衣→喝水提醒→道别",
    sub_agents=[
        greeting_agent,
        weather_agent,
        clothing_agent,
        hydration_agent,
        farewell_agent,
    ],
)
```
## 运行
```
adk web
```
![](https://jruing-blogs.oss-cn-beijing.aliyuncs.com/blogs/202603161825.png)


