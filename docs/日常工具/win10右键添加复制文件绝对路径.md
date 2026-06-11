---
title: "Win10 右键添加复制文件绝对路径"
date: 2026-06-09
tags:
  - 日常工具
  - Windows
  - Win10
  - 右键菜单
  - 注册表
  - 文件路径
  - 系统配置
  - 效率工具
---

文件名称：win10右键添加复制文件绝对路径.reg
```
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\Allfilesystemobjects\shell\windows.copyaspath]

"CanonicalName"=""

"CommandStateHandler"=""

"CommandStateSync"=""

"Description"="@shell32.dll,-30336"

"Icon"="imageres.dll,-5302"

"InvokeCommandOnSelection"=dword:00000001

"MUIVerb"="@shell32.dll,-30329"

"VerbHandler"=""

"VerbName"="copyaspath"

```