---
tags:
  - Vibe-coding
---
## 文档
[github](https://github.com/musistudio/claude-code-router)
## 安装步骤
### 安装claude code
```
npm install -g @anthropic-ai/claude-code
```
### claude code 登录
>用户家目录下创建`.claude/settings.json`
```json
{
  "env": {
    "ANTHROPIC_API_KEY": "sk-你的KEY",
    "ANTHROPIC_BASE_URL": "https://你的地址",
    "CLAUDE_CODE_MAX_OUTPUT_TOKENS": 32000,
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  },
  "permissions": {
    "allow": [],
    "deny": []
  },
  "apiKeyHelper": "echo 'sk-你的KEY'"
}
```
### 安装claude code router
```
npm install -g @musistudio/claude-code-router
```
### 页面配置模型
```
ccr ui
```
### 代码编写
```
ccr code
```