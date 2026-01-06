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
## 删除文件
```python
from pathlib import Path

# 1. 定义要删除的文件路径
file_path = Path("/home/user/documents/temp_file.txt")
# 相对路径示例
# file_path = Path("test_delete.txt")

# 2. 基础删除（如果文件不存在会报错）
try:
    file_path.unlink()
    print(f"文件 {file_path} 已成功删除")
except FileNotFoundError:
    print(f"文件 {file_path} 不存在，无需删除")
except PermissionError:
    print(f"没有权限删除文件 {file_path}")

# 3. 更安全的删除（先判断文件是否存在）
if file_path.is_file():  # 确保是文件且存在
    file_path.unlink()
    print(f"文件 {file_path} 已删除")
else:
    print(f"文件 {file_path} 不存在或不是文件")

# 4. 进阶：unlink() 的 missing_ok 参数（Python 3.8+ 支持）
# missing_ok=True 表示文件不存在时不报错，无需手动捕获异常
file_path.unlink(missing_ok=True)
print(f"已尝试删除 {file_path}（文件不存在也不会报错）")

# ❗ 注意：pathlib 不能直接用 unlink() 删除目录
# 删除目录需要用 rmdir()，且目录必须为空
folder_path = Path("/home/user/empty_folder")
if folder_path.is_dir():
    folder_path.rmdir()  # 仅删除空目录
    print(f"空目录 {folder_path} 已删除")
```
## 移动文件
```python
source_file2 = Path("docs/data.csv")
target_file2 = Path("archive/2025/data.csv")

# 场景1：如果目标文件已存在，rename() 会报错，需先判断
if not target_file2.exists():
    source_file2.rename(target_file2)
else:
    print(f"目标文件 {target_file2} 已存在，跳过移动")
# 场景2：强制覆盖已存在的目标文件（使用 replace()）,replace() 会直接覆盖同名文件，无需手动删除
source_file2.replace(target_file2)
print(f"文件已强制移动并覆盖：{target_file2}")
```
