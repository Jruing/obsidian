---
title: "React 响应事件"
date: 2026-06-09
tags:
  - 开发
  - 前端
  - React
---

```
import "./App.css";

function App() {
  // 定义响应事件函数
  function handleClick() {
    alert("你点击了按钮");
  }
  function handleChange(e) {
    console.log(e.target.value);
  }
  return (
    <>
      // 调用点击事件函数
      <button onClick={handleClick}>点击</button>
      <input onChange={handleChange} placeholder="请输入内容" />
    </>
  );
} 

export default App;
```
