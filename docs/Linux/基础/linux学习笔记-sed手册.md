---
title: "sed 手册"
date: 2026-06-09
tags:
  - Linux
  - 基础
  - sed
  - 文本处理
  - 流编辑器
  - 正则表达式
  - 批量替换
  - 命令行
---

`sed` 是一个流编辑器（Stream Editor），用于对文本进行基本的文本转换。它可以在不交互的情况下对文件或输入流进行编辑，常用于脚本中处理文本数据。

以下是 `sed` 的简明中文手册，涵盖常用命令、语法和示例：

---

## 📘 一、sed 基本语法

```bash
sed [选项] '编辑命令' 文件名
```

或者从管道输入：

```bash
command | sed '编辑命令'
```

---

## 📗 二、常用选项（Options）

| 选项 | 说明 |
|------|------|
| `-n` | 静默模式，只输出匹配处理的行 |
| `-e` | 允许同时指定多个编辑命令 |
| `-f` | 从文件中读取编辑命令 |
| `-i` | 直接修改文件内容（慎用） |
| `-r` 或 `-E` | 启用扩展正则表达式 |

---

## 📙 三、常用命令（编辑命令）

### 1. 打印（Print）

- 打印第 3 行：
  ```bash
  sed -n '3p' filename
  ```

- 打印 2 到 5 行：
  ```bash
  sed -n '2,5p' filename
  ```

- 打印匹配 "hello" 的行：
  ```bash
  sed -n '/hello/p' filename
  ```

- 打印从 "start" 到 "end" 的段落：
  ```bash
  sed -n '/start/,/end/p' filename
  ```

---

### 2. 删除（Delete）

- 删除第 3 行：
  ```bash
  sed '3d' filename
  ```

- 删除所有包含 "error" 的行：
  ```bash
  sed '/error/d' filename
  ```

- 删除空行：
  ```bash
  sed '/^$/d' filename
  ```

---

### 3. 替换（Substitute）

基本格式：

```bash
s/原字符串/替换字符串/[flags]
```

- 替换每行第一个 "apple" 为 "orange"：
  ```bash
  sed 's/apple/orange/' filename
  ```

- 替换所有 "apple"：
  ```bash
  sed 's/apple/orange/g' filename
  ```

- 只替换第 3 行中的 "apple"：
  ```bash
  sed '3 s/apple/orange/g' filename
  ```

- 替换匹配行中的内容：
  ```bash
  sed '/error/s/this/that/g' filename
  ```

- 使用不同分隔符（如 `#`）避免与路径冲突：
  ```bash
  sed 's#/usr/bin#/usr/local/bin#g' filename
  ```

---

### 4. 插入（Insert）、追加（Append）

- 在第 3 行前插入一行：
  ```bash
  sed '3i\This is a new line' filename
  ```

- 在第 3 行后添加一行：
  ```bash
  sed '3a\Another new line' filename
  ```

- 在匹配行后添加多行：
  ```bash
  sed '/pattern/r file_to_insert.txt' filename
  ```

---

### 5. 更改整行（Change）

- 将第 3 行替换为新内容：
  ```bash
  sed '3c\New content here' filename
  ```

---

### 6. 转换字符（Translate）

- 将小写转为大写（仅限 GNU sed）：
  ```bash
  sed 'y/abc/ABC/' filename
  ```

---

### 7. 写入到文件（Write）

- 将匹配行写入另一个文件：
  ```bash
  sed -n '/error/w error.log' filename
  ```

---

## 📕 四、高级技巧

### 多命令执行

- 使用 `-e` 指定多个命令：
  ```bash
  sed -e 's/foo/bar/' -e 's/baz/qux/' filename
  ```

- 或在单引号中使用分号：
  ```bash
  sed 's/foo/bar/; s/baz/qux/' filename
  ```

### 分组与引用（需配合正则捕获）

- 提取 IP 地址示例：
  ```bash
  echo "IP: 192.168.1.1" | sed -E 's/.*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*/\1/'
  ```

### 模拟 grep 功能

```bash
sed -n '/pattern/p' filename
```

---

## 📓 五、实战示例

### 示例 1：批量替换目录下所有文件中的字符串（慎用！）

```bash
sed -i 's/old_string/new_string/g' *.txt
```

### 示例 2：删除注释行和空行

```bash
sed -e 's/#.*//' -e '/^$/d' config.conf
```

### 示例 3：提取 HTTP 状态码日志

```bash
sed -n '/HTTP\/1.1" 404/p' access.log
```

---

## 📒 六、注意事项

- `sed -i` 会直接修改原文件，请备份后再操作。
- 正则表达式默认是**基础正则表达式（BRE）**，使用 `-r` 或 `-E` 开启**扩展正则表达式（ERE）**。
- 如果要处理 Unicode 文本，请确保终端编码一致（如 UTF-8）。

---

## 📜 七、参考资料

- `man sed`
- GNU Sed 官方文档：https://www.gnu.org/software/sed/manual/sed.html
