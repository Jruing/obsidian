---
tags:
  - Python
---
## 创建Path对象
```python
from pathlib import Path

# 表示当前工作目录
current_dir = Path('.')
print(f"当前目录: {current_dir.resolve()}") 
# 输出示例: C:\Users\YourName\...\current_dir

# 表示特定路径 (Windows 或 Linux/macOS 风格都支持)
# Pathlib 会自动处理不同操作系统间的路径分隔符差异
file_path = Path('/Users/shared/report.txt')
```
## 路径拼接
```python
root_dir = Path('/home/user')
project_dir = root_dir / 'my_project' # 路径连接

file_name = 'data.csv'
data_file = project_dir / 'data' / file_name # 连续连接

print(data_file)
# 输出示例: /home/user/my_project/data/data.csv
```
## 路径信息
| **属性**    | **描述**                       | **示例**     | **输出示例 (对于 /home/user/app/script.py)**      |
| --------- | ---------------------------- | ---------- | ------------------------------------------- |
| `.name`   | 文件或目录的**名称** (最后一部分)。        | `p.name`   | `script.py`                                 |
| `.stem`   | **不带后缀**的文件名。                | `p.stem`   | `script`                                    |
| `.suffix` | 文件的**后缀** (扩展名)。             | `p.suffix` | `.py`                                       |
| `.parent` | 路径的**父目录** (返回一个新的 Path 对象)。 | `p.parent` | `/home/user/app`                            |
| `.parts`  | 路径的所有**组成部分** (元组)。          | `p.parts`  | `('/', 'home', 'user', 'app', 'script.py')` |
## 路径操作方法
| **方法**                  | **描述**                         | **示例**                                |
| ----------------------- | ------------------------------ | ------------------------------------- |
| `p.exists()`            | 检查路径指向的文件或目录**是否存在**。          | `Path('config.ini').exists()`         |
| `p.is_file()`           | 检查路径是否指向一个**文件**。              | `p.is_file()`                         |
| `p.is_dir()`            | 检查路径是否指向一个**目录**。              | `p.is_dir()`                          |
| `p.resolve()`           | 获取路径的**绝对路径**，并消除符号链接。         | `Path('../data').resolve()`           |
| `p.with_suffix(suffix)` | **更改**文件的**后缀名**，返回新的 Path 对象。 | `Path('file.txt').with_suffix('.md')` |
## 目录操作
```python
target_dir = Path('reports/2025/q4')

# 创建多级目录 (如果父目录不存在也会创建)
target_dir.mkdir(parents=True, exist_ok=True) 

# 删除空目录
# target_dir.rmdir() 

# 重命名/移动目录或文件
# target_dir.rename('old_reports')
```
## 文件操作
```python
file = Path('settings.txt')

# 写入文本内容 (覆盖或创建文件)
file.write_text("API_KEY=12345\nDEBUG=True", encoding='utf-8')

# 读取整个文本内容
content = file.read_text(encoding='utf-8')
print(f"File Content: \n{content}")

# 删除文件
# file.unlink()
```
## 文件与目录遍历
```python
# 假设当前目录下有 files/a.txt, files/b.csv, files/sub/c.txt

data_dir = Path('files')

# 遍历 files 目录下的所有文件和目录
for item in data_dir.iterdir():
    print(item.name) # 输出: a.txt, b.csv, sub

# 递归查找所有 .txt 文件
# ** 表示递归查找所有子目录
for txt_file in data_dir.glob('**/*.txt'):
    print(f"Found: {txt_file}")
    # 输出: Found: files/a.txt, Found: files/sub/c.txt
```