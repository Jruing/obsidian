---
title: "tmux 使用手册"
date: 2026-06-09
tags:
  - Linux
  - 基础
  - tmux
  - 终端复用
  - 会话管理
  - 后台任务
  - 快捷键
  - 命令行
---

# 🐧 Linux `tmux` 使用手册

> `tmux`（Terminal Multiplexer）是一个终端多路复用器，允许你在一个终端窗口中管理多个终端会话，并且可以在断开连接后重新连接这些会话。

---

## 一、安装 tmux

大多数 Linux 发行版默认已安装 `tmux`。如果没有，可以用以下命令安装：

- Debian/Ubuntu:
  ```bash
  sudo apt install tmux
  ```

- CentOS/RHEL:
  ```bash
  sudo yum install tmux
  ```

- Fedora:
  ```bash
  sudo dnf install tmux
  ```

---

## 二、基本使用

### 1. 启动一个新的会话

```bash
tmux
```

### 2. 启动命名会话（推荐）

```bash
tmux new -s session_name
```
例如：
```bash
tmux new -s work
```

### 3. 查看所有会话

```bash
tmux ls
```

输出示例：
```
0: 1 windows (created Tue Jun 10 10:00:00 2025)
work: 2 windows (created Tue Jun 10 10:05:00 2025)
```

### 4. 恢复某个会话

```bash
tmux attach -t session_name
```
例如：
```bash
tmux attach -t work
```

### 5. 断开会话（Detach）

在 tmux 中按下组合键：
```
Ctrl + b 然后按 d
```

### 6. 结束会话

在 tmux 会话中输入：
```bash
exit
```
或使用命令强制结束：
```bash
tmux kill-session -t session_name
```

---

## 三、常用快捷键（前缀：`Ctrl + b`）

> 所有快捷键操作都在进入 tmux 会话后生效。

| 快捷键                  | 功能                                |
| ----------------------- | ----------------------------------- |
| `Ctrl + b c`            | 创建新窗口                          |
| `Ctrl + b n`            | 切换到下一个窗口                    |
| `Ctrl + b p`            | 切换到上一个窗口                    |
| `Ctrl + b w`            | 显示窗口列表并切换                  |
| `Ctrl + b l`            | 切换到最后使用的窗口                |
| `Ctrl + b ,`            | 重命名当前窗口                      |
| `Ctrl + b %`            | 垂直分割窗格                        |
| `Ctrl + b "` （双引号） | 水平分割窗格                        |
| `Ctrl + b o`            | 在不同窗格之间切换                  |
| `Ctrl + b x`            | 关闭当前窗格                        |
| `Ctrl + b [`            | 进入复制模式（滚动、选择文本）      |
| `Ctrl + b :`            | 输入 tmux 命令（如 `kill-session`） |

---

## 四、高级功能

### 1. 多人共享会话

```bash
tmux attach -t session_name
```
多个用户可以同时连接到同一个会话，适合协作调试。

### 2. 后台运行任务并查看日志

```bash
tmux new -d -s mytask 'ping google.com'
```
然后恢复查看：
```bash
tmux attach -t mytask
```

### 3. 分屏操作

- 垂直分屏：
  ```
  Ctrl + b %
  ```

- 水平分屏：
  ```
  Ctrl + b "
  ```

- 切换窗格：
  ```
  Ctrl + b o
  ```

- 调整窗格大小（进入调整模式）：
  ```
  Ctrl + b Alt + 方向键
  ```

---

## 五、配置文件（~/.tmux.conf）

你可以通过编辑 `~/.tmux.conf` 自定义 `tmux` 行为。以下是几个常用配置示例：

```bash
# 设置前缀为 Ctrl + a（代替默认的 Ctrl + b）
set-option -g prefix C-a
unbind C-b
bind C-a send-prefix

# 启用鼠标支持（需要 tmux 2.1+）
set -g mouse on

# 设置状态栏颜色
set -g status-bg black
set -g status-fg white

# 显示窗口列表
set -g status-left '#(whoami)@#H'

# 设置窗口自动命名
set-option -g allow-rename off
```

加载配置文件：
```bash
tmux source-file ~/.tmux.conf
```

---

## 六、常用命令总结

| 操作               | 命令                                                  |
| ------------------ | ----------------------------------------------------- |
| 列出会话           | `tmux ls`                                             |
| 新建会话           | `tmux new -s session_name`                            |
| 恢复会话           | `tmux attach -t session_name`                         |
| 强制恢复会话       | `tmux attach -t session_name -d`                      |
| 结束会话           | `tmux kill-session -t session_name`                   |
| 重命名会话         | `tmux rename-session -t old_name new_name`            |
| 发送命令到后台会话 | `tmux send-keys -t session_name 'your_command' Enter` |

---

## 七、常见问题

### Q: 如何退出复制模式？

A: 按 `q` 键即可退出。

### Q: 出现 `no current session` 错误？

A: 说明你没有在 tmux 会话中执行命令，请先进入一个会话。

### Q: 如何设置窗口标题？

A: 在 `.tmux.conf` 中添加：
```bash
set-option -g set-titles on
set-option -g set-titles-string "#T"
```

---

## 八、示例流程

### 示例 1：启动后台任务并查看输出

```bash
tmux new -d -s task 'ping baidu.com'
tmux attach -t task
```

### 示例 2：创建多个窗口并切换

```bash
tmux new -s demo
Ctrl + b c      # 创建第二个窗口
Ctrl + b w      # 查看窗口列表
Ctrl + b n/p    # 切换窗口
```

---

## ✅ 小技巧

- 💡 使用命名会话更容易管理多个任务。
- 💡 鼠标支持 (`mouse on`) 可以方便地点击切换窗格。
- 💡 使用 `Ctrl + b [` 进入复制模式后，按 `Enter` 开始选中，再按 `Enter` 复制。
- 💡 使用插件系统（如 [tpm](https://github.com/tmux-plugins/tpm)）可以扩展功能（如 CPU 监控、自动补全等）。

---

