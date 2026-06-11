---
title: "Python爬虫-无限VM debugger解决方案"
date: 2026-06-09
tags:
  - 开发
  - Python
  - 爬虫
  - 反调试
---

打开F12控制台输入以下内容：
```
Function.prototype.constructor = function(){}
```
