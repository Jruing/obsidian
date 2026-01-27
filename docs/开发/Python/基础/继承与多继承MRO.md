---
tags:
  - Python
---
## 继承
```markdown
class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):  # 继承 Parent
    def greet(self):
        # 使用 super() 调用父类方法
        super().greet()
        print("Hello from Child")


d = Child().greet()
```

## 多继承

> 📌 **MRO**（Method Resolution Order，方法解析顺序）  
> ✅ Python 使用 **C3 线性化算法** 计算 MRO，确保满足以下条件：
> - 子类优先于父类；
> - 父类按定义顺序（从左到右）考虑；
> - 保持单调性（不破坏已有的继承关系）。

### 示例

```python
class 爷爷:
    pass

class 奶奶:
    pass

class 外公:
    pass

class 外婆:
    pass

class 爸爸(爷爷, 奶奶):
    pass

class 妈妈(外公, 外婆):
    pass

class 儿子(爸爸, 妈妈):
    pass

print(儿子.__mro__)
```

### 输出结果

```python
(<class '__main__.儿子'>,
 <class '__main__.爸爸'>,
 <class '__main__.爷爷'>,
 <class '__main__.奶奶'>,
 <class '__main__.妈妈'>,
 <class '__main__.外公'>,
 <class '__main__.外婆'>,
 <class 'object'>)
```

### 验证 C3 合并规则

```python
class 爷爷:
    pass

class 奶奶:
    pass

class 外公:
    pass

class 外婆:
    pass

class 爸爸(爷爷, 奶奶):
    pass

class 妈妈(外公, 外婆):
    pass

class 儿子(爸爸, 妈妈):
    pass

class 女儿(妈妈, 爸爸):
    pass

print(儿子.__mro__)
print(女儿.__mro__)

# 尝试引入一个同时继承 儿子 和 女儿 的子类
class 弟弟(儿子, 女儿):
    pass

print(弟弟.__mro__)
```
### 输出结果（报错）

```text
Traceback (most recent call last):
  File "C:\workspace\test_dev\20260112.py", line 55, in 
    class 弟弟(儿子, 女儿):
TypeError: Cannot create a consistent method resolution order (MRO) for bases 爸爸, 妈妈
```
### 原因分析

- `儿子` 的 MRO 要求：**爸爸 在 妈妈 之前**；
- `女儿` 的 MRO 要求：**妈妈 在 爸爸 之前**；
- 两者冲突 → C3 算法无法构造一致的线性继承顺序。

### ⚠️ 注意事项

MRO 并非简单的“深度优先”或“广度优先”。  
在早期 Python（2.2 之前）中确实使用深度优先搜索（DFS），但存在菱形继承等问题。  
**C3 线性化算法**解决了这些问题，确保：
- 每个类在 MRO 中仅出现一次；
- 继承顺序符合开发者预期且逻辑一致。