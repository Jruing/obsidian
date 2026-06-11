---
title: "js实现拷贝复制功能"
date: 2026-06-09
tags:
  - 开发
  - 前端
  - 前端基础
  - JavaScript
  - Clipboard
---

```
    /**
     * 复制单行内容到粘贴板
     * content : 需要复制的内容
     * message : 复制完后的提示，不传则默认提示"复制成功"
     */
    function copyToClip(content, message) {
        var aux = document.createElement("input");
        aux.setAttribute("value", content);
        document.body.appendChild(aux);
        aux.select();
        document.execCommand("copy");
        document.body.removeChild(aux);
        if (message == null) {
            alert("复制成功");
        } else{
            alert(message);
        }
    }
```
