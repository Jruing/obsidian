---
title: "screen 使用手册"
date: 2026-06-09
tags:
  - Linux
  - 基础
  - screen
  - 终端复用
  - 会话管理
  - 后台任务
  - 快捷键
  - 命令行
---

# 🐧 Linux `screen` 快速参考手册（Cheatsheet）

## 🔹 基本命令

| 操作 | 命令 |
|------|------|
| 启动一个新的会话 | `screen` |
| 启动命名会话 | `screen -S session_name` |
| 查看所有会话 | `screen -ls` |
| 恢复会话 | `screen -r session_name_or_pid` |
| 强制恢复会话 | `screen -dr session_name_or_pid` |
| 新建后台会话并运行命令 | `screen -dmS session_name command` |
| 结束当前会话 | 在 screen 中输入 `exit` 或 `Ctrl + a :quit` |

## 🔹 快捷键（前缀：`Ctrl + a`）

> 所有快捷键操作都在进入 `screen` 会话后生效。

| 快捷键                | 功能                                        |
| --------------------- | ------------------------------------------- |
| `Ctrl + a` 然后 `c`   | 创建一个新窗口                              |
| `Ctrl + a` 然后 `n`   | 切换到下一个窗口                            |
| `Ctrl + a` 然后 `p`   | 切换到上一个窗口                            |
| `Ctrl + a` 然后 `0-9` | 切换到编号为 0~9 的窗口                     |
| `Ctrl + a` 然后 `"`   | 显示窗口列表，选择切换                      |
| `Ctrl + a` 然后 `'`   | 输入窗口编号跳转                            |
| `Ctrl + a` 然后 `d`   | 断开会话（Detach）                          |
| `Ctrl + a` 然后 `k`   | 杀死当前窗口（谨慎使用）                    |
| `Ctrl + a` 然后 `?`   | 显示帮助信息                                |
| `Ctrl + a` 然后 `H`   | 开始/停止记录终端日志（生成 `screenlog.0`） |
| `Ctrl + a` 然后 `[`   | 进入复制模式（滚动、搜索、复制）            |
| `Ctrl + a` 然后 `]`   | 粘贴缓冲区内容                              |

---

## 🔹 管理会话的高级命令

| 操作               | 命令                                               |
| ------------------ | -------------------------------------------------- |
| 杀死某个会话       | `screen -X -S session_id quit`                     |
| 发送命令到后台会话 | `screen -S session_name -X stuff 'your_command\n'` |
| 在后台运行命令     | `screen -dmS mysession ping google.com`            |

---

## 🔹 配置文件示例（`~/.screenrc`）

```bash
# 自动创建带标签的窗口
screen -t "main" 0
screen -t "logs" 1

# 设置状态栏显示主机名、时间等信息
hardstatus alwayslastline
hardstatus string '%{= kG}[ %{G}%H %{g}][%= %{=kw}%?%-Lw%?%{r}(%{W}%n*%f %t%?(%u)%?%{r})%{w}%?%+Lw%?%=%{g} ][%{B}%Y-%m-%d %{W}%c %{g}]'
```

---

## 🔹 小技巧

- 💡 使用命名会话更容易管理多个任务。
- 💡 `screen -x` 可以多用户共享同一个会话（协作调试时非常有用）。
- 💡 记录日志功能适合调试和审计。

---

## 📄 示例流程

### 启动后台任务并查看输出：

```bash
screen -dmS mytask ping baidu.com
screen -r mytask
```

### 创建多个窗口并切换：

```bash
screen -S demo
Ctrl + a c      # 创建第二个窗口
Ctrl + a "      # 查看窗口列表
Ctrl + a n/p    # 切换窗口
```

