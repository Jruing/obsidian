---
tags:
  - Python
  - 日志
---
## 默认模板
```python
import logging
from logging.handlers import RotatingFileHandler
import sys

# --- 配置参数 ---
LOG_FILE = 'dual_output.log'
LOG_LEVEL = logging.DEBUG # 设置为 DEBUG 级别，可以看到所有级别的日志

# --- 1. 创建 Logger ---
logger = logging.getLogger('dual_logger')
logger.setLevel(LOG_LEVEL)

# --- 2. 定义 Formatter (格式化器) ---
# 统一使用一个详细的格式
formatter = logging.Formatter(
    '[%(asctime)s] - [%(levelname)s] - %(name)s - (%(filename)s:%(lineno)d) - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --- 3. 创建并配置 Handler ---

# A. 控制台输出 Handler (StreamHandler)
console_handler = logging.StreamHandler(sys.stdout) # 默认使用 sys.stderr，这里明确使用 stdout
console_handler.setLevel(logging.INFO)             # 控制台只输出 INFO 级别及以上的日志
console_handler.setFormatter(formatter)

# B. 文件轮转 Handler (RotatingFileHandler)
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=1024 * 1024 * 10, # 10 MB
    backupCount=3,             # 保留 3 个备份文件
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG) # 文件输出所有 DEBUG 级别及以上的日志
file_handler.setFormatter(formatter)

# --- 4. 将 Handler 添加到 Logger ---
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# --- 5. 演示日志输出 ---

# 注意：
# DEBUG 消息会写入文件，但不会显示在控制台
logger.debug("这是一个 DEBUG 消息，只写入文件。")

# INFO 及以上消息会同时写入文件和控制台
logger.info("这是一个 INFO 消息，会同时出现在控制台和文件中。")
logger.warning("这是一个 WARNING 消息，通知功能即将被弃用。")
logger.error("操作失败，请检查配置。")

print(f"\n日志已写入文件: {LOG_FILE}")
```

## 自定义Handler
>自定义 Slack 通知 Handler
```python
import logging
import requests # 假设使用 requests 库发送数据
import json

# 定义一个自定义 Handler
class SlackHandler(logging.Handler):
    def __init__(self, webhook_url, level=logging.ERROR):
        super().__init__(level)
        self.webhook_url = webhook_url

    # 核心方法：处理日志记录并将其发送到目标
    def emit(self, record):
        # 1. 使用 Formatter 将 LogRecord 转换为字符串
        log_entry = self.format(record)
        
        # 2. 构造 Slack 消息载荷
        slack_payload = {
            "text": f"🔥 **ERROR ALERT** 🔥\nLogger: {record.name}\nTime: {record.asctime}\nMessage:\n```\n{log_entry}\n```"
        }
        
        # 3. 模拟发送请求
        try:
            # 实际上这里会使用 requests.post(self.webhook_url, json=slack_payload)
            # 为了演示，我们只打印发送内容
            print("\n--- SIMULATING SLACK NOTIFICATION ---")
            print(f"Severity: {record.levelname}")
            print(f"Payload Sent: {json.dumps(slack_payload, indent=2)}")
            print("-------------------------------------\n")
            
        except Exception as e:
            self.handleError(record) # 如果发送失败，调用默认错误处理
            
# ----------------------------------------------------------------------

# 配置和使用自定义 Handler

# 1. 再次获取 Logger
custom_logger = logging.getLogger('custom_app')
custom_logger.setLevel(logging.INFO)

# 2. 创建 SlackHandler 实例
# 假设的 Slack Webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/..."

slack_handler = SlackHandler(SLACK_WEBHOOK)
# 只需要 ERROR 级别以上的日志才发送 Slack 通知
slack_handler.setLevel(logging.ERROR) 

# 3. 设置 Formatter (可以使用更简洁的格式，因为它有自己的 payload 结构)
simple_formatter = logging.Formatter('%(message)s (in file %(filename)s:%(lineno)d)')
slack_handler.setFormatter(simple_formatter)

# 4. 添加 Handler
custom_logger.addHandler(slack_handler)

# 演示
custom_logger.info("This is an INFO message and will NOT trigger Slack.")
custom_logger.warning("This is a WARNING message and will NOT trigger Slack.")
custom_logger.error("Database connection failed due to Timeout.") # 这条会触发 Slack 通知
```