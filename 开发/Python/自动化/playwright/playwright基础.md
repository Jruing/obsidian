---
tags:
  - 浏览器自动化
  - Python
---
## 同步运行
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()
```
## 异步运行
```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())
```
## 无头模式运行
```python

```
## 跳转页面
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
	# 声明浏览器对象
    browser = p.chromium.launch()
    # 声明页面对象
    page = browser.new_page()
    # url：跳转页面url
    # timeout：超时时间，单位毫秒
    # wait_until: 操作成功判断条件，["commit", "domcontentloaded", "load", "networkidle", None],默认为load
    page.goto(url="https://www.baidu.com",timeout=60000,wait_until="load")
    browser.close()
```
## 元素定位
```python
page.locator("css=button")
```
## 元素操作
### 输入内容
```python
# 直接填充
page.locator("#username").fill("输入内容")
# 逐字输入
page.locator('#area').press_sequentially("输入内容")
```
### 点击按钮
```python
# 左键点击,force为强制点击
page.locator("#submit").click(force=True)
# 右击
page.locator("#submit").click(button="right")
# 双击
page.locator("#submit").dbclick()
# shift+左键点击
page.locator("#submit").click(modifiers=["Shift"])
# 鼠标悬浮
page.locator("#submit").hover()
# 点击所选中元素的指定位置
page.locator("#submit").click(position={ "x": 0, "y": 0})
```
### 单选/复选框
```python
# 点击触发选中或者取消选中
page.locator("#sex").check()
# 校验是否被选中
expect(page.locator('#sex')).to_be_checked()
```
### 下拉框选项
```python
# 单选（匹配值/标签）
page.locator("#sex").select_option('男')
# 单选（仅匹配标签）
page.locator("#sex").select_option(label='男')
# 多选
page.locator("#sex").select_option(['red', 'green', 'blue'])
```
### 快捷键
```python
# 快捷键列表
Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.
# 回车
page.locator("#submit").press("Enter")
```
### 上传文件
```python
# 单文件上传
page.locator("#file").set_input_files('myfile.pdf')
# 多文件上传
page.locator("#file").set_input_files(['file1.txt', 'file2.txt'])
# 清空上传的文件
page.locator("#file").set_input_files([])
```
### 拖放
```python
# 方式一
page.locator("#a").drag_to(page.locator("#b"))
# 方式二
page.locator("#a").hover()
page.mouse.down()
page.locator("#b").hover()
page.mouse.up()
```