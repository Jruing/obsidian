---
title: "React 条件判断"
date: 2026-06-09
tags:
  - 开发
  - 前端
  - React
  - 条件判断
---

```
import "./App.css";
import React from "react";
function App() {
  // 生成一个随机数
  const status = Math.random() > 0.5;
  return (
    <>
      <p>{status===true?"大于0.5":"小于0.5"}</p>
    </>
  );
}

export default App;
```
