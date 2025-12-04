---
tags:
  - Python
---
> Pydantic 是一个基于 Python 类型注解（Type Hints）的 **数据验证（Data Validation）** 和 **数据设置（Data Settings）** 库。它的核心价值在于，它允许您使用标准的 Python 类和类型注解来定义数据结构和约束，然后自动进行数据解析和验证。

## 基本模型定义
```python
from pydantic import BaseModel

# 定义一个 User 模型
class User(BaseModel):
    # 字段名: 期望类型
    id: int
    name: str = 'Jane Doe'  # 可以设置默认值
    signup_ts: datetime.datetime | None = None  # 使用 Union 或 | 定义可选类型
    is_active: bool = True
```
## 模型实例化/验证
```python
from datetime import datetime

# 传入有效数据
user_data = {
    'id': 123,
    'name': 'Alice',
    'signup_ts': '2025-11-25T15:00:00', # Pydantic 会自动将字符串转换为 datetime 对象
}

try:
    user = User(**user_data)
    
    print(user.id)          # 123
    print(user.name)        # Alice
    print(user.signup_ts)   # datetime.datetime(2025, 11, 25, 15, 0)
    print(user.is_active)   # True (使用了默认值)

except Exception as e:
    print(f"验证错误: {e}")
```
## 模型嵌套
```python
class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    items: list[Item] # 列表中的每个元素都必须是 Item 模型
    customer_id: int

# 验证数据
order_data = {
    'customer_id': 456,
    'items': [
        {'name': 'Laptop', 'price': 999.99},
        {'name': 'Mouse', 'price': 25.00}
    ]
}

order = Order(**order_data)
print(order.items[0].name) # Laptop
```
## 模型序列化
```
# 假设上面的 user 实例已经创建
print(user.model_dump()) 
# 输出: {'id': 123, 'name': 'Alice', 'signup_ts': datetime.datetime(2025, 11, 25, 15, 0), 'is_active': True}

print(user.model_dump_json(indent=2)) 
# 输出一个格式化的 JSON 字符串
```
## 自定义字段校验
> 在模型中定义一个方法，使用 `@field_validator('字段名')` 装饰器将其标记为特定字段的校验器
```python
from pydantic import BaseModel, ValidationError, field_validator
import re

class Contact(BaseModel):
    name: str
    phone_number: str

    # 1. 定义一个校验器方法
    # 2. 使用 @field_validator('字段名') 装饰器，并设置 mode='before' 或 mode='after'
    #    'before'：在 Pydantic 执行内置类型转换之前运行 (常用)
    #    'after'：在 Pydantic 执行内置类型转换之后运行
    @field_validator('phone_number')
    @classmethod
    def validate_phone_format(cls, value):
        # 校验：确保是 11 位数字
        if not re.match(r'^\d{11}$', value):
            raise ValueError('Phone number must be an 11-digit string.')
        return value  # 校验成功后，必须返回该值
```
## 字典约束
> 使用 `Field` 函数对字段进行简单的约束（如最小长度、最大值）
```python
from pydantic import BaseModel, Field

class Profile(BaseModel):
    # 长度必须在 5 到 50 个字符之间
    bio: str = Field(min_length=5, max_length=50)
    
    # 值必须大于 0 且小于 100
    rating: float = Field(gt=0, lt=100) # gt: greater than (大于), lt: less than (小于)

# 测试: bio 长度太短
try:
    Profile(bio='Hi', rating=50.0)
except ValidationError as e:
    print("\n--- Field Constraint Test ---")
    print(e)
```