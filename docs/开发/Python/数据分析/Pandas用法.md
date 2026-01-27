---
tags:
  - Python
---
## 示例数据
```python
import pandas as pd
import numpy as np

# 创建一个示例 DataFrame
data = {
    'City': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu'],
    'Population': [2154, 2487, 1530, 1756, 1633],
    'Area': [16410, 6340, 7434, 1997, 14312],
    'GDP': [3537, 4325, 2501, 2800, 2076],
    'Score': [85, 92, np.nan, 88, 79] # 引入一个缺失值 np.nan
}
df = pd.DataFrame(data)
```
## 数据查看与描述
| **方法**          | **描述**                                | **示例**          | **结果示例**                             |
| --------------- | ------------------------------------- | --------------- | ------------------------------------ |
| `df.head(n)`    | 查看数据框的**前 $n$ 行** (默认为 5)。            | `df.head(3)`    | 前三行数据                                |
| `df.info()`     | 打印关于数据框的**摘要信息**，包括数据类型、非空值数量和内存使用情况。 | `df.info()`     | 各列类型、非空计数                            |
| `df.describe()` | 生成**数值列**的描述性统计信息 (计数、均值、标准差等)。       | `df.describe()` | Population、Area、GDP 的统计信息            |
| `df.shape`      | 返回数据框的**行数和列数** (作为元组)。               | `df.shape`      | `(5, 5)`                             |
| `df.dtypes`     | 返回每个列的**数据类型**。                       | `df.dtypes`     | City: object, Population: int64, ... |
## 数据筛选与选择
| **方法**                      | **描述**                    | **示例**                 | **结果示例**              |
| --------------------------- | ------------------------- | ---------------------- | --------------------- |
| `df['ColName']`             | 选择**单个列**，返回一个 Series。    | `df['City']`           | 包含所有城市名的 Series       |
| `df[['C1', 'C2']]`          | 选择**多个列**，返回一个 DataFrame。 | `df[['City', 'GDP']]`  | 包含 City 和 GDP 两列的数据框  |
| `df.loc[row_idx, col_idx]`  | 基于**标签**（索引名和列名）进行选择。     | `df.loc[0, 'City']`    | 'Beijing'             |
| `df.iloc[row_idx, col_idx]` | 基于**位置**（整数索引）进行选择。       | `df.iloc[1, 3]`        | 2487 (Shanghai 的 GDP) |
| **条件筛选**                    | 使用布尔值 Series 筛选行。         | `df[df['GDP'] > 3000]` | 仅包含 GDP 大于 3000 的行    |
## 数据清理与处理
| **方法**                      | **描述**                                  | **示例**                                   | **结果示例**              |
| --------------------------- | --------------------------------------- | ---------------------------------------- | --------------------- |
| `df.isnull()`               | 返回一个布尔型数据框，指示哪些位置是**缺失值** (`True` 为缺失)。 | `df.isnull()`                            | Score 列第 2 行返回 `True` |
| `df.dropna()`               | **删除**包含**缺失值** (`NaN`) 的行或列。           | `df.dropna()`                            | 删除 Score 为 NaN 的那一行   |
| `df.fillna(value)`          | 用指定值**填充缺失值**。                          | `df['Score'].fillna(df['Score'].mean())` | 用 Score 列的均值填充缺失值     |
| `df.drop(labels, axis=0/1)` | **删除**指定的行 (axis=0) 或列 (axis=1)。        | `df.drop('Area', axis=1)`                | 删除 'Area' 列           |
| `df.rename(columns={...})`  | **重命名**列名或索引标签。                         | `df.rename(columns={'City': 'Name'})`    | 将 'City' 改名为 'Name'   |
## 数据转换与应用
| **方法**                     | **描述**                                    | **示例**                                               | **结果示例**               |
| -------------------------- | ----------------------------------------- | ---------------------------------------------------- | ---------------------- |
| `df['Col'].apply(func)`    | 对 Series 中的**每一个元素**应用一个函数（包括 lambda 函数）。 | `df['Population'].apply(lambda x: x / 100)`          | Population 列的数值都除以 100 |
| `df.assign(new_col=...)`   | **添加**新列。                                 | `df.assign(Density = df['Population'] / df['Area'])` | 添加 'Density' 列         |
| `df['Col'].astype(dtype)`  | 将 Series 的**数据类型转换**为指定的类型。               | `df['Population'].astype(float)`                     | Population 列转换为浮点数     |
| `df.sort_values(by='Col')` | 根据一个或多个列的**值进行排序**。                       | `df.sort_values(by='GDP', ascending=False)`          | 按 GDP 降序排列所有行          |
## 分组与聚合
| **方法**                     | **描述**                     | **示例**                                   | **结果示例**                |
| -------------------------- | -------------------------- | ---------------------------------------- | ----------------------- |
| `df.groupby('Col')`        | 根据指定列的值将数据**分组**。          | `df.groupby('City')`                     | 返回一个 GroupBy 对象         |
| `df.groupby().mean()`      | 对每个分组计算**均值**。             | `df.groupby('City')['GDP'].mean()`       | 每个城市的平均 GDP (在本例中与原值相同) |
| `df.groupby().sum()`       | 对每个分组计算**总和**。             | `df.groupby('City')['Population'].sum()` | 每个城市的总人口                |
| `df['Col'].value_counts()` | 统计 Series 中每个**唯一值的出现次数**。 | `df['City'].value_counts()`              | 每个城市名出现的次数              |
## 数据合并与连接
| **方法**                         | **描述**                                                    | **示例**                                               | **结果示例**              |
| ------------------------------ | --------------------------------------------------------- | ---------------------------------------------------- | --------------------- |
| `pd.concat([df1, df2])`        | 沿着轴（默认是行）**堆叠**或连接多个 DataFrame。                           | `pd.concat([df, df_new], axis=0)`                    | 将 df_new 的行添加到 df 的底部 |
| `pd.merge(df1, df2, on='key')` | 类似于 SQL 中的 **JOIN** 操作，通过共同的键（'key'）将两个 DataFrame **合并**。 | `pd.merge(df_orders, df_customers, on='CustomerID')` | 将订单数据与客户数据连接          |
## 读取数据
### 读取csv
```python
import pandas as pd

# 基本读取
df_csv = pd.read_csv('data.csv')

# 常用参数：
df_custom = pd.read_csv(
    'data.txt',
    sep='\t',          # 指定分隔符，例如 tab 制表符
    header=0,          # 指定哪一行是列名 (0 表示第一行)
    index_col='ID',    # 指定某一列作为索引
    parse_dates=['Date'], # 指定需要解析为日期/时间格式的列
    na_values=['N/A', 'Unknown'] # 指定哪些字符串应被视为缺失值 (NaN)
)
```
### 读取Excel
```python
# 读取第一个工作表（sheet）
df_excel = pd.read_excel('data.xlsx')

# 读取指定名称或位置的工作表 (Sheet2 或 索引为 1 的工作表)
df_sheet = pd.read_excel('data.xlsx', sheet_name='Sheet2')
df_index_sheet = pd.read_excel('data.xlsx', sheet_name=1)
```
### 读取Json
```python
# 读取 JSON 文件
df_json = pd.read_json('data.json')

# 常用参数：
# orient='records' (默认): 预期格式 [{'col1': val, 'col2': val}, ...]
# orient='columns': 预期格式 {'col1': [val1, val2, ...], 'col2': [val1, val2, ...]}
```
### 读取数据库
```python
from sqlalchemy import create_engine

# 创建数据库连接引擎 (以 SQLite 为例)
engine = create_engine('sqlite:///my_database.db')

# 直接运行 SQL 查询并将结果读入 DataFrame
sql_query = "SELECT * FROM users WHERE age > 25"
df_sql = pd.read_sql(sql_query, engine)

# 也可以读取整个表
df_table = pd.read_sql_table('table_name', engine)
```
## 导出数据
### 导出至CSV
```python
# 导出一个处理后的 DataFrame
df_processed.to_csv('output_processed.csv')

# 常用参数：
df_processed.to_csv(
    'output_no_index.csv',
    index=False,        # 不将 DataFrame 的行索引写入文件 (非常常用)
    sep='|',            # 指定分隔符
    na_rep='NULL',      # 指定缺失值 (NaN) 在文件中的表示方式
    encoding='utf-8'    # 指定文件编码
)
```
### 导出到 Excel 文件
```python
# 导出到 Excel 文件
df_processed.to_excel('output_processed.xlsx', sheet_name='CleanData')

# 导出多个 DataFrame 到同一个 Excel 文件的不同 Sheet (需要使用 ExcelWriter)
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    df_raw.to_excel(writer, sheet_name='Raw Data', index=False)
    df_clean.to_excel(writer, sheet_name='Clean Data', index=False)
```
### 导出到 JSON 文件
```python
# 导出到 Excel 文件
df_processed.to_excel('output_processed.xlsx', sheet_name='CleanData')

# 导出多个 DataFrame 到同一个 Excel 文件的不同 Sheet (需要使用 ExcelWriter)
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    df_raw.to_excel(writer, sheet_name='Raw Data', index=False)
    df_clean.to_excel(writer, sheet_name='Clean Data', index=False)
```
### 导出到 SQL 数据库
```python
# 假设 engine 已创建
df_processed.to_sql(
    'new_results_table',  # 要写入的表名
    engine,               # 数据库连接引擎
    if_exists='replace',  # 如果表已存在：'fail' (报错), 'replace' (替换), 'append' (追加)
    index=False           # 不将 DataFrame 的索引作为一列写入数据库
)
```