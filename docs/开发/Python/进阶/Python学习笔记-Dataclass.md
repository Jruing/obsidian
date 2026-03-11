---
tags:
  - Python
---
#### 1. 概述

Python的`dataclass`是Python 3.7引入的标准库特性，旨在简化主要用来存储数据的类的定义。它通过装饰器自动生成`__init__`、`__repr__`、`__eq__`等常用但繁琐的特殊方法，减少样板代码，使代码更简洁、可读性更强。

#### 2. 基础用法

首先，需要从标准库导入`dataclass`：

```
from dataclasses import dataclass
```

- **最简定义**：使用`@dataclass`装饰器，代码可以极大地简化。

```
@dataclass
class User:
    name: str
    age: int

# 自动生成 __init__ 和 __repr__
user = User("Alice", 30)
print(user)  # User(name='Alice', age=30)
```

- **默认值**：可以为字段指定默认值。注意：带有默认值的字段必须定义在没有默认值的字段之后。

```
@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True  # 带默认值的可选字段
```

#### 3. 核心配置参数

`@dataclass`装饰器本身接受参数来控制生成方法的行为：

- `init`：是否生成`__init__`方法。默认为`True`。
- `repr`：是否生成`__repr__`方法。默认为`True`。
- `eq`：是否生成`__eq__`方法。默认为`True`。
- `order`：是否生成`__lt__`, `__le__`, `__gt__`, `__ge__`等比较方法。要求`eq=True`。
- `frozen`：如果为`True`，则实例初始化后属性不能被修改（不可变对象）。

```
@dataclass(order=True, frozen=True)
class Score:
    value: int
    timestamp: float
# 现在可以比较大小，并且实例创建后无法修改 value 或 timestamp
```

#### 4. 高级特性与field()

对于更精细的控制，可以使用`dataclasses.field()`函数来配置单个字段。

- **处理可变默认值**：永远不要直接将可变对象（如列表、字典）作为默认值，否则所有实例会共享同一个对象。

```
#  错误做法
@dataclass
class BadExample:
    items: list = []  # 危险！所有实例共享同一个列表

#  正确做法：使用 default_factory
@dataclass
class GoodExample:
    items: list = field(default_factory=list)  # 每个实例都有独立的列表
```

- **字段行为控制**：`field()`函数提供了多个参数来定制字段行为。
    - `default_factory`：一个无参可调用对象，用于生成每个实例的独立默认值。
    - `repr`：如果为`False`，该字段不会出现在`__repr__`的输出中。
    - `compare`：如果为`False`，该字段不参与`==`和`!=`比较。
    - `init`：如果为`False`，该字段不会作为`__init__`的参数。

```
@dataclass
class SensitiveData:
    user_id: int
    password: str
    api_key: str = field(repr=False)  # 打印对象时不会显示 api_key

data = SensitiveData(1, "123456", "secret-key")
print(data)  # SensitiveData(user_id=1, password='123456')
```

#### 5. 钩子方法与InitVar

- `__post_init__`：如果需要在初始化完成后执行一些额外的逻辑（如数据验证、计算派生字段），可以定义`__post_init__`方法。它会在自动生成的`__init__`执行完毕后被调用。

```
@dataclass
class User:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

- `InitVar`：`InitVar`是一种特殊的字段类型。标记为`InitVar`的字段会作为参数传递给`__init__`和`__post_init__`，但不会成为类的实例属性。这在需要一些“临时”参数来辅助初始化时非常有用。

```
from dataclasses import dataclass, InitVar

@dataclass
class User:
    name: str
    age: int = 0
    raw_age: InitVar[int] = None  # 仅用于初始化的临时字段

    def __post_init__(self, raw_age):
        # 使用 raw_age 计算最终的 age 值
        if raw_age is not None:
            self.age = raw_age if raw_age >= 0 else 0
```

#### 6. 常用辅助函数

`dataclasses`模块还提供了一些有用的工具函数：

- `asdict(instance)`：将dataclass实例递归地转换为一个字典。
- `astuple(instance)`：将dataclass实例递归地转换为一个元组。
- `replace(instance, **changes)`：创建一个现有实例的副本，并用`changes`中指定的值替换相应字段。

```
from dataclasses import asdict, replace

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = replace(p1, x=3)  # Point(x=3, y=2)
p1_dict = asdict(p1)   # {'x': 1, 'y': 2}
```

#### 7. 与普通类对比

| 特性 | 普通类 | dataclass |
| ------ |------ |------ |
| **样板代码** | 需手动编写`__init__`, `__repr__`等 | 自动生成`__init__`, `__repr__`等 |
| **类型提示** | 可选，不影响运行 | 是字段定义的核心部分 |
| **不可变性** | 需手动实现 | 通过`frozen=True`一键实现 |
| **默认工厂** | 需在`__init__`中处理 | 使用`field(default_factory=list)` |
| **核心理念** | 行为优先 | 数据优先 |

#### 8. 总结

`dataclass`非常适合用于定义数据传输对象（DTO）、配置类、纯数据模型等场景，能显著提升代码的简洁性和可维护性。

