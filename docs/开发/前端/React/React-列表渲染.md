---
title: "React 列表渲染"
date: 2026-06-09
tags:
  - 开发
  - 前端
  - React
---

```
import "./App.css";
const colorList = ["red", "blue", "yellow"];
const colorItem = colorList.map((item,index) => (
  <li style={{ color: item }}>{index}-{item}</li>
));

function App() {
  return (
    <>
      <ul>{colorItem}</ul>
    </>
  );
}

export default App;
```