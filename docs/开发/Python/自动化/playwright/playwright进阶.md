---
tags:
  - 浏览器自动化
  - Python
---
## 常用的断言列表
[断言列表](https://playwright.dev/python/docs/test-assertions)
## 会话状态存储
> 当前目录下创建一个`.auth` 目录用于存储
```python
# 保存当前状态
storage = context.storage_state(path="state.json")
# 使用之前的状态
context = browser.new_context(storage_state="state.json")
```

## 对话框处理
> 必须监听`dialog` 事件
```python
# 点击确认
page.on("dialog", lambda dialog: dialog.accept())
# 点击关闭
page.on("dialog", lambda dialog: dialog.dismiss())
# 自定义处理逻辑
def handle_dialog(dialog):  
	# 具体逻辑  
	dialog.dismiss()
page.on("dialog", lambda: handle_dialog)
```
## 设备模拟
>`playwright.devices` 指定设备,[设备列表](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json)
```python
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
	iphone_13 = playwright.devices['iPhone 13']  
	browser = playwright.webkit.launch(headless=False)  
	context = browser.new_context(  
	**iphone_13,  
	)
with sync_playwright() as playwright:  
	run(playwright)
```
## 执行JS
```python
# 直接执行
page.evaluate('object => object.foo', { 'foo': 'bar' })

button = page.evaluate_handle('window.button')  
page.evaluate('button => button.textContent', button)
```
## 事件监听
>

```python
# 监听请求
page.on("request", lambda request: print(">>", request.method, request.url))
# 监听响应  
page.on("response", lambda response: print("<<", response.status, response.url))
```
## 截图
### 全屏截图
```python
page.screenshot(path="screenshot.png", full_page=True)
```
### 单个元素截图
```python
page.locator(".header").screenshot(path="screenshot.png")
```