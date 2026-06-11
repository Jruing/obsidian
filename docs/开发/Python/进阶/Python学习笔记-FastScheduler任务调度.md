---
title: "FastScheduler 任务调度"
date: 2026-06-09
tags:
  - 开发
  - Python
  - 进阶
  - FastScheduler
  - 任务调度
  - 定时任务
  - 异步编程
  - FastAPI
  - Cron
  - SQLModel
  - 后台任务
---

# FastScheduler 任务调度

> FastScheduler 是一个轻量级 Python 任务调度库，支持同步/异步任务、时区、Cron 表达式、状态持久化、自动重试、任务超时和 FastAPI 实时监控面板。
>
> 项目地址：[MichielMe/fastscheduler](https://github.com/MichielMe/fastscheduler)

## 核心能力

- 使用装饰器定义任务，写法简单。
- 原生支持 `async/await`。
- 支持按秒、分钟、小时、天、周等间隔调度。
- 支持固定时间、一次性任务和 Cron 表达式。
- 支持时区配置。
- 支持任务状态持久化，重启后可恢复任务。
- 支持 SQLite、PostgreSQL、MySQL 等数据库存储。
- 支持 FastAPI Dashboard 实时查看任务状态。
- 支持自动重试、超时控制、暂停、恢复、取消任务。
- 支持 Dead Letter Queue，用于记录和排查失败任务。

## 安装

```bash
# 基础安装
pip install fastscheduler

# 支持 FastAPI Dashboard
pip install fastscheduler[fastapi]

# 支持 Cron 表达式
pip install fastscheduler[cron]

# 支持数据库存储
pip install fastscheduler[database]

# 安装全部功能
pip install fastscheduler[all]
```

## 快速开始

```python
from fastscheduler import FastScheduler

scheduler = FastScheduler(quiet=True)


@scheduler.every(10).seconds
def task():
    print("Task executed")


@scheduler.daily.at("14:30")
async def daily_task():
    print("Daily task at 2:30 PM")


scheduler.start()
```

## 调度方式

### 间隔调度

```python
@scheduler.every(10).seconds
@scheduler.every(5).minutes
@scheduler.every(2).hours
@scheduler.every(1).days
```

### 固定时间调度

```python
@scheduler.daily.at("09:00")
def daily_job():
    ...


@scheduler.hourly.at(":30")
def hourly_job():
    ...


@scheduler.weekly.monday.at("10:00")
def monday_job():
    ...


@scheduler.weekly.weekdays.at("09:00")
def weekday_job():
    ...


@scheduler.weekly.weekends.at("12:00")
def weekend_job():
    ...
```

### Cron 表达式

> 需要安装：`pip install fastscheduler[cron]`

```python
@scheduler.cron("0 9 * * MON-FRI")
def market_open():
    ...


@scheduler.cron("*/15 * * * *")
def frequent_check():
    ...


@scheduler.cron("0 0 1 * *")
def monthly_report():
    ...
```

### 一次性任务

```python
@scheduler.once(60)
def delayed_task():
    ...


@scheduler.at("2024-12-25 00:00:00")
def christmas_task():
    ...
```

## 时区支持

```python
@scheduler.daily.at("09:00", tz="America/New_York")
def nyc_morning():
    print("Good morning, New York!")


@scheduler.weekly.monday.tz("Europe/London").at("09:00")
def london_standup():
    print("Monday standup")


@scheduler.cron("0 9 * * MON-FRI").tz("Asia/Tokyo")
def tokyo_market():
    print("Tokyo market open")
```

常用时区：

- `UTC`
- `America/New_York`
- `America/Los_Angeles`
- `Europe/London`
- `Europe/Paris`
- `Asia/Tokyo`
- `Asia/Shanghai`
- `Australia/Sydney`

## 任务控制

### 超时控制

```python
@scheduler.every(1).minutes.timeout(30)
def quick_task():
    ...


@scheduler.daily.at("02:00").timeout(3600)
def nightly_backup():
    ...
```

### 自动重试

```python
@scheduler.every(5).minutes.retries(5)
def flaky_api_call():
    ...
```

重试默认使用指数退避，例如 `2s`、`4s`、`8s`、`16s`。

### 跳过补偿执行

默认情况下，调度器重启后会计算错过的执行并补跑。可以使用 `no_catch_up()` 跳过补偿执行。

```python
@scheduler.every(1).hours.no_catch_up()
def hourly_stats():
    ...
```

### 暂停、恢复、取消

```python
# 暂停任务
scheduler.pause_job("job_0")

# 恢复任务
scheduler.resume_job("job_0")

# 取消任务
scheduler.cancel_job("job_0")

# 按函数名取消任务
scheduler.cancel_job_by_name("my_task")
```

## FastAPI 集成

FastScheduler 可以挂载一个实时监控面板到 FastAPI 应用中。

```python
from fastapi import FastAPI
from fastscheduler import FastScheduler
from fastscheduler.fastapi_integration import create_scheduler_routes

app = FastAPI()
scheduler = FastScheduler(quiet=True)

app.include_router(create_scheduler_routes(scheduler))


@scheduler.every(30).seconds
def background_task():
    print("Background work")


scheduler.start()
```

访问地址：

```text
http://localhost:8000/scheduler/
```

Dashboard 支持：

- Server-Sent Events 实时更新。
- 任务状态、最近运行结果和倒计时展示。
- 直接在 UI 中运行、暂停、恢复、取消任务。
- 查看执行历史。
- 查看 Dead Letter Queue 中的失败任务。
- 查看成功率、运行时间、活跃任务数等统计信息。

## Dashboard API

| Endpoint | Method | 说明 |
| --- | --- | --- |
| `/scheduler/` | GET | Dashboard UI |
| `/scheduler/api/status` | GET | 调度器状态 |
| `/scheduler/api/jobs` | GET | 任务列表 |
| `/scheduler/api/jobs/{job_id}` | GET | 指定任务详情 |
| `/scheduler/api/jobs/{job_id}/pause` | POST | 暂停任务 |
| `/scheduler/api/jobs/{job_id}/resume` | POST | 恢复任务 |
| `/scheduler/api/jobs/{job_id}/run` | POST | 立即执行任务 |
| `/scheduler/api/jobs/{job_id}/cancel` | POST | 取消任务 |
| `/scheduler/api/history` | GET | 执行历史 |
| `/scheduler/api/dead-letters` | GET | 失败任务列表 |
| `/scheduler/api/dead-letters` | DELETE | 清空失败任务 |
| `/scheduler/events` | GET | SSE 事件流 |

## 配置项

```python
scheduler = FastScheduler(
    state_file="scheduler.json",
    storage="json",
    database_url=None,
    quiet=True,
    auto_start=False,
    max_history=5000,
    max_workers=20,
    history_retention_days=8,
    max_dead_letters=500,
)
```

常用参数：

| 参数 | 说明 |
| --- | --- |
| `state_file` | JSON 后端状态文件 |
| `storage` | 存储后端，默认 `json`，也可使用 `sqlmodel` |
| `database_url` | SQLModel 后端数据库连接地址 |
| `quiet` | 是否关闭日志输出 |
| `auto_start` | 是否初始化后自动启动 |
| `max_history` | 最大执行历史数量 |
| `max_workers` | 最大并发任务线程数 |
| `history_retention_days` | 历史记录保留天数 |
| `max_dead_letters` | 失败任务队列最大记录数 |

## 历史记录和失败任务

历史记录会按两个条件清理：

- `max_history`：最大保留条数。
- `history_retention_days`：最大保留天数。

设置 `history_retention_days=0` 可以关闭基于时间的清理。

失败任务会进入 Dead Letter Queue：

```python
dead_letters = scheduler.get_dead_letters(limit=100)
scheduler.clear_dead_letters()
```

Dead Letter Queue 会记录：

- 失败任务。
- 错误信息。
- 时间戳。
- 运行次数。
- 执行耗时。

## 数据库存储

> 生产环境或高可靠场景建议使用数据库存储。
>
> 需要安装：`pip install fastscheduler[database]`

### SQLite

```python
scheduler = FastScheduler(
    storage="sqlmodel",
    database_url="sqlite:///scheduler.db",
)
```

### PostgreSQL

```python
scheduler = FastScheduler(
    storage="sqlmodel",
    database_url="postgresql://user:password@localhost:5432/mydb",
)
```

### MySQL

```python
scheduler = FastScheduler(
    storage="sqlmodel",
    database_url="mysql://user:password@localhost:3306/mydb",
)
```

SQLModel 后端会自动创建以下表：

| 表 | 用途 |
| --- | --- |
| `scheduler_jobs` | 活跃任务定义 |
| `scheduler_history` | 执行历史 |
| `scheduler_dead_letters` | 失败任务记录 |
| `scheduler_metadata` | 任务计数和统计信息 |

## 运行状态查询

```python
jobs = scheduler.get_jobs()
job = scheduler.get_job("job_0")

history = scheduler.get_history(limit=100)
history = scheduler.get_history(func_name="my_task", limit=50)

stats = scheduler.get_statistics()
scheduler.print_status()
```

## 上下文管理器

```python
import time
from fastscheduler import FastScheduler

with FastScheduler(quiet=True) as scheduler:
    @scheduler.every(5).seconds
    def task():
        print("Running")

    time.sleep(30)
```

退出 `with` 块后调度器会自动停止。

## 完整示例

```python
import asyncio
import time
from fastscheduler import FastScheduler

scheduler = FastScheduler(quiet=True)


@scheduler.every(10).seconds
def heartbeat():
    print(f"[{time.strftime('%H:%M:%S')}] Heartbeat")


@scheduler.daily.at("09:00", tz="America/New_York").timeout(60)
async def morning_report():
    print("Generating report...")
    await asyncio.sleep(5)
    print("Report sent!")


@scheduler.cron("*/5 * * * *").retries(3)
def check_api():
    print("Checking API health")


@scheduler.weekly.monday.at("10:00")
def weekly_standup():
    print("Time for standup!")


scheduler.start()

try:
    while True:
        time.sleep(60)
        scheduler.print_status()
except KeyboardInterrupt:
    scheduler.stop()
```

## FastAPI Lifespan 示例

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastscheduler import FastScheduler
from fastscheduler.fastapi_integration import create_scheduler_routes

scheduler = FastScheduler(quiet=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.stop(wait=True)


app = FastAPI(lifespan=lifespan)
app.include_router(create_scheduler_routes(scheduler))


@scheduler.every(30).seconds
def background_job():
    print("Working...")
```

## API 速查

### FastScheduler 方法

| 方法 | 说明 |
| --- | --- |
| `start()` | 启动调度器 |
| `stop(wait=True, timeout=30)` | 停止调度器 |
| `get_jobs()` | 获取全部任务 |
| `get_job(job_id)` | 获取指定任务 |
| `get_history(func_name=None, limit=50)` | 获取执行历史 |
| `get_statistics()` | 获取运行统计 |
| `get_dead_letters(limit=100)` | 获取失败任务 |
| `clear_dead_letters()` | 清空失败任务队列 |
| `pause_job(job_id)` | 暂停任务 |
| `resume_job(job_id)` | 恢复任务 |
| `run_job_now(job_id)` | 立即运行任务 |
| `cancel_job(job_id)` | 取消任务 |
| `cancel_job_by_name(func_name)` | 按函数名取消任务 |
| `print_status()` | 打印状态 |

### 调度方法

| 方法 | 说明 |
| --- | --- |
| `every(n).seconds/minutes/hours/days` | 间隔调度 |
| `daily.at("HH:MM")` | 每日固定时间 |
| `hourly.at(":MM")` | 每小时固定分钟 |
| `weekly.monday.at("HH:MM")` | 每周固定星期 |
| `weekly.weekdays.at("HH:MM")` | 工作日调度 |
| `weekly.weekends.at("HH:MM")` | 周末调度 |
| `cron("expression")` | Cron 表达式调度 |
| `once(seconds)` | 延迟一次性执行 |
| `at("YYYY-MM-DD HH:MM:SS")` | 指定时间一次性执行 |

### 链式修饰符

| 修饰符 | 说明 |
| --- | --- |
| `.timeout(seconds)` | 最大执行时长 |
| `.retries(n)` | 最大重试次数 |
| `.no_catch_up()` | 跳过错过任务补偿 |
| `.tz("timezone")` | 设置时区 |

