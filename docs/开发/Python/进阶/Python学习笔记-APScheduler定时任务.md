---
title: "APScheduler定时任务"
date: 2026-06-09
tags:
  - 开发
  - Python
  - 进阶
  - 定时任务
---

# Python APScheduler 定时任务

## 简介

APScheduler（Advanced Python Scheduler）是一个轻量级的 Python 定时任务框架，相比 Celery 更加轻量且支持**动态添加定时任务**。

主要优点：
- 支持**持久化**任务存储（内存、数据库、Redis 等）
- 支持**动态添加**定时任务
- 支持多种调度器、执行器、触发器

### 安装

```bash
pip install apscheduler
```

### 组件关系

APScheduler 包含以下核心组件：

- **调度器（Scheduler）** — 协调各组件，提供 API
- **触发器（Trigger）** — 决定任务何时执行
- **执行器（Executor）** — 负责执行任务（线程池/进程池）
- **任务存储器（Job Store）** — 存储任务元数据

---

## 一般使用

基本步骤：

1. 创建调度器
2. 配置调度器（任务存储器 + 执行器 + 全局配置）
3. 添加任务
4. 运行调度任务
5. 修改/删除任务

> 除此之外，还可以监听事件，执行自定义的函数

### 快速开始

```python
import datetime
from pytz import timezone

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore

job_stores = {
    'default': MemoryJobStore()
}
executors = {
    'processpool': ProcessPoolExecutor(max_workers=5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


def hello_world():
    print("hello world")


scheduler = BlockingScheduler()
scheduler.configure(jobstores=job_stores, executors=executors, job_defaults=job_defaults)

# 在当前时间的3秒后触发执行
scheduler.add_job(hello_world, "date",
                  run_date=datetime.datetime.now() + datetime.timedelta(seconds=3),
                  timezone=timezone("Asia/Shanghai"))

scheduler.start()
```

---

## 调度器（Scheduler）

不同的应用场景选择不同的调度器：

| 调度器 | 适用场景 |
|--------|---------|
| `BlockingScheduler` | 调度器是程序中唯一运行的东西 |
| `BackgroundScheduler` | 应用程序后台静默运行 |
| `AsyncIOScheduler` | 使用 `asyncio` 库 |
| `GeventScheduler` | 使用 `gevent` 库 |
| `TornadoScheduler` | 构建 Tornado 应用 |
| `TwistedScheduler` | 构建 Twisted 应用 |
| `QtScheduler` | 构建 Qt 应用 |

> 使用非阻塞调度器时需注意：**程序是否会退出导致无法执行任务**

---

## 执行器（Executor）

执行器负责处理作业的运行，通过将任务提交到线程池或进程池来执行。

### 支持的类型

| 执行器 | 说明 |
|--------|------|
| `ThreadPoolExecutor` | 线程池执行器（**默认**） |
| `ProcessPoolExecutor` | 进程池执行器 |
| `AsyncIOExecutor` | AsyncIO 事件循环执行器 |
| `GeventExecutor` | Gevent 事件循环执行器 |
| `TornadoExecutor` | Tornado 事件循环执行器 |

> `ThreadPoolExecutor` 和 `ProcessPoolExecutor` 分别基于 `concurrent.futures`，参数：`max_workers=10`, `pool_kwargs=None`

### 使用示例

```python
from apscheduler.executors.pool import ThreadPoolExecutor

executors = {
    'pool': ThreadPoolExecutor(max_workers=5)
}

scheduler = BlockingScheduler()
scheduler.configure(executors=executors)

# 添加任务时指定执行器
scheduler.add_job(hello_world, "date", executor="pool", ...)
```

---

## 任务存储器（Job Store）

任务存储器用于存储被调度的任务。默认使用内存存储，也可持久化到数据库。

> **注意**：任务存储器不能共享调度器

### 支持的类型

| 存储器                  | 说明                       |
| -------------------- | ------------------------ |
| `MemoryJobStore`     | 内存存储（**默认**）             |
| `SQLAlchemyJobStore` | 基于 SQLAlchemy ORM 的关系数据库 |
| `MongoDBJobStore`    | MongoDB 存储               |
| `RedisJobStore`      | Redis 存储                 |
| `RethinkDBJobStore`  | RethinkDB 存储             |
| `ZooKeeperJobStore`  | ZooKeeper 存储             |

### SQLAlchemy + MySQL 示例

```python
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

MYSQL = {
    "url": "mysql+pymysql://root:123456@localhost/test"
}
job_stores = {
    'mysql': SQLAlchemyJobStore(**MYSQL)
}

scheduler = BlockingScheduler()
scheduler.configure(jobstores=job_stores)
scheduler.add_job(hello_world, "date", jobstore="mysql", ...)
```

### Redis 示例

```python
from apscheduler.jobstores.redis import RedisJobStore

REDIS = {
    'host': '127.0.0.1',
    'port': '6379',
    'db': 0,
}
job_stores = {
    'redis': RedisJobStore(**REDIS)
}

scheduler = BlockingScheduler()
scheduler.configure(jobstores=job_stores)
scheduler.add_job(hello_world, "date", jobstore="redis", ...)
```

---

## 触发器（Trigger）

触发器包含调度逻辑，每个任务都有自己的触发器来决定下次运行时间。触发器完全是无状态的。

### date — 日期触发（执行一次）

```python
from datetime import date

# 在2021年12月3日执行
scheduler.add_job(my_job, 'date', run_date=date(2021, 12, 3), args=['text'])

# 立即执行
scheduler.add_job(my_job, 'date', args=['text'], timezone="Asia/shanghai")
```

### interval — 间隔触发（每隔一段时间执行）

```python
# 每隔2秒执行一次
schedulers.add_job(job_function, 'interval', seconds=2, timezone="Asia/shanghai")
```

参数：`weeks`, `days`, `hours`, `minutes`, `seconds`, `start_date`, `end_date`

### cron — 周期触发（类似 crontab）

```python
# 每分钟的第2秒执行一次
scheduler.add_job(job_function, 'cron', second=2, timezone="Asia/shanghai")
```

参数：`year`, `month`, `day`, `week`, `day_of_week`, `hour`, `minute`, `second`

> 不指定参数时，默认为 `*`

**Crontab 表达式语法**：

| 表达式 | 说明 |
|--------|------|
| `*` | 任意时间 |
| `*/a` | 每隔 a 时间，如 `*/10 4 * * *` 表示 4 点每隔 10 分钟 |
| `a-b` | a-b 范围内 |
| `a-b/c` | a-b 范围内可被 c 整除 |
| `xth y` | 一个月内第 x 个礼拜的星期 y |
| `last x` | 一个月内最后的星期 x |
| `last` | 月末当天 |
| `x,y,z` | 不连续时间组合 |

```python
from apscheduler.triggers.cron import CronTrigger

# 每2分钟执行一次（使用 crontab 语法）
scheduler.add_job(job_function, CronTrigger.from_crontab("*/2 * * * *", timezone="Asia/shanghai"))

# 常用 crontab 示例：
# 45 22 * * *  每天 22:45
# 0 17 * * 1   每周一 17:00
# 0 4 1,15 * * 每月1号或15号的 4:00
# 40 4 * * 1-5 周一到周五的 4:40
```

---

## 调度器 API

### 添加任务

两种方式：

```python
# 方式一：add_job 直接添加
scheduler.add_job(func, trigger=None, args=None, kwargs=None, id=None, name=None,
                  misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
                  next_run_time=undefined, jobstore='default', executor='default',
                  replace_existing=False, **trigger_args)

# 方式二：scheduled_job 装饰器
@scheduler.scheduled_job(...)
def hello_world():
    print("hello_world")
```

**参数说明**：
| 参数 | 说明 |
|------|------|
| `func` | 任务函数 |
| `trigger` | 触发器 |
| `args/kwargs` | 给 func 的位置参数/关键字参数 |
| `id` | 任务标识 |
| `name` | 任务说明 |
| `misfire_grace_time` | 错过执行后的宽限时间 |
| `coalesce` | 是否合并多次错过的执行为一次 |
| `max_instances` | 最大并发实例数 |
| `jobstore` | 指定任务存储器 |
| `executor` | 指定执行器 |
| `replace_existing` | 为 True 时，用相同 id 替换现有任务 |
| `trigger_args` | 给触发器的关键字参数 |

> `.add_job()` 返回 `apscheduler.job.Job` 实例

### 移除任务

```python
# 通过 Job 实例
job = scheduler.add_job(myfunc, 'interval', minutes=2)
job.remove()

# 通过任务 ID
scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
scheduler.remove_job('my_job_id')
```

### 修改任务

```python
# 修改 Job 实例属性
job.modify(args=["lczmx"], max_instances=6, name='Alternate name')

# 根据 ID 修改参数
scheduler.modify_job("my_job_id", args=["lczmx"])

# 重新调度（更换触发器）
scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
```

### 暂停或恢复任务

```python
# 暂停
job.pause()
scheduler.pause_job("my_job_id")

# 恢复
job.resume()
scheduler.resume_job("my_job_id")
```

### 查看任务信息

```python
# 获取单个任务
scheduler.get_job("my_job_id")

# 获取全部任务
scheduler.get_jobs()

# 格式化输出全部任务信息
scheduler.print_jobs()
```

### 终止调度器

```python
# 默认等待当前所有任务执行完
scheduler.shutdown()

# 不等待
scheduler.shutdown(wait=False)
```

### 暂停/恢复调度器

```python
# 暂停整个调度器
scheduler.pause()

# 恢复
scheduler.resume()

# 启动时暂停
scheduler.start(paused=True)
```

---

## 事件监听

可以为 scheduler 绑定事件监听器，在某些情况下触发回调函数。

### 使用方法

```python
from apscheduler.events import *

def my_listener(event):
    if event.exception:
        print('发生异常')
    else:
        print('任务已经执行')

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
```

### 事件类型

| 事件                         | 说明         | 参数类型                 |
| -------------------------- | ---------- | -------------------- |
| `EVENT_SCHEDULER_STARTED`  | 调度器已启动     | `SchedulerEvent`     |
| `EVENT_SCHEDULER_SHUTDOWN` | 调度器被关闭     | `SchedulerEvent`     |
| `EVENT_SCHEDULER_PAUSED`   | 调度器暂停      | `SchedulerEvent`     |
| `EVENT_SCHEDULER_RESUMED`  | 调度器恢复      | `SchedulerEvent`     |
| `EVENT_JOB_ADDED`          | 添加任务       | `JobEvent`           |
| `EVENT_JOB_REMOVED`        | 移除任务       | `JobEvent`           |
| `EVENT_JOB_MODIFIED`       | 修改任务       | `JobEvent`           |
| `EVENT_JOB_SUBMITTED`      | 提交任务到执行器   | `JobSubmissionEvent` |
| `EVENT_JOB_MAX_INSTANCES`  | 执行器达到最大实例数 | `JobSubmissionEvent` |
| `EVENT_JOB_EXECUTED`       | 成功执行任务     | `JobExecutionEvent`  |
| `EVENT_JOB_ERROR`          | 任务执行出错     | `JobExecutionEvent`  |
| `EVENT_JOB_MISSED`         | 任务错过执行     | `JobExecutionEvent`  |
| `EVENT_ALL`                | 所有事件       | 动态                   |

---

## 配置方式

有三种配置方式：

### 方式一：实例化时传入

```python
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc
)
```

### 方式二：创建后调用 configure

```python
scheduler = BackgroundScheduler()
scheduler.configure(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc
)
```

### 方式三：字典配置

```python
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.mongo': {
        'type': 'mongodb'
    },
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///jobs.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
})
```

---

## 全局配置

```python
job_defaults = {
    'coalesce': False,      # 关闭聚合功能
    'max_instances': 3,      # 默认最大并发实例数
    "timezone": "UTC",       # 调度器时区
}
```

---

## 故障排查

将 APScheduler 的日志级别设为 DEBUG：

```python
import logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
```

---

## 核心概念

### 最大允许实例（max_instances）

默认每个任务同时只有一个实例在运行。如果任务到达计划时间但前一个实例未完成，则会 misfire（错过）。可通过 `max_instances` 参数设置并发实例数。

### 错过的作业与合并操作（coalescing）

当 scheduler 无法在计划时间执行任务时（如 scheduler 重启导致任务错过），会检查每个错过任务的 `misfire_grace_time` 来决定是否继续触发。

**coalescing（合并）**：启用后，将多次错过的执行合并为**一次**执行，避免连续多次触发。
