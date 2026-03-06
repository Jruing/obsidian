---
tags:
  - Vibe-coding
  - AI
  - Agent
---
# Skill 技能系统完整教程

为 AI Agent 提供专业化能力的扩展系统

---

## 什么是 Skill

Skill 本质上就是教 AI 按固定流程做事的操作说明书，一旦写好，就能像函数一样反复调用。

我们可以把 Skills 看成把"某类事情应该怎么专业做"这件事，封装成一个可复用、可自动触发的能力模块。

Skill 是一个文件夹，里面装着指令文档、参考资料、可执行脚本等资源。AI 拿到它，就能胜任一项原本不会的特定工作。

### 核心概念

- **知识复用**：经验、最佳实践、工作流程
- **基于简单的 Markdown 文件**：任何人都可以创建
- **渐进式加载**：Token 使用效率高
- **无需服务器或后端设置**：适用于各种 AI 客户端

---

## 与传统方式的对比

### Skills vs 普通 Prompt

| 对比项 | 普通 Prompt | Skills 机制 |
|--------|-------------|-------------|
| 每次都要重新描述 | 是 | 否（只描述一次） |
| 上下文长度占用 | 每次全量塞入 | 渐进式加载（只在触发时才读完整内容） |
| 一致性 | 依赖每次 prompt 质量 | 高（固定 SOP + 模板） |
| 复用性 | 手动复制粘贴 | 自动匹配 / slash 命令 / 项目共享 |
| 维护方式 | 改一次 prompt 就要重新发 | 修改 SKILL.md 文件，全局/项目生效 |

### Skills vs MCP

| 特性 | Skills | MCP |
|------|--------|-----|
| 用途 | 知识复用 | 能力扩展 |
| 内容 | 经验、最佳实践、工作流程 | 连接 API、数据库、外部工具 |
| 创建方式 | 基于简单的 Markdown 文件 | 需要编码能力和服务器端配置 |
| 加载方式 | 渐进式加载 | 启动时加载全部工具定义 |
| Token 消耗 | 高效 | 更高 |
| 适用场景 | Web / Desktop / CLI | 外部系统集成 |

---

## 核心结构

Skills 的核心就是：**一个文件夹 + 一个 SKILL.md 文件**。

### 最小结构

```
my-skill/
└── SKILL.md    # 唯一必需文件
```

### 完整结构示例

```
skills/
├── pdf-editor/              # 技能目录
│   ├── SKILL.md            # 技能主文件（必需）
│   ├── LICENSE.txt         # 许可证文件（可选）
│   ├── reference.md        # 参考文档（可选）
│   ├── templates/          # 模板目录（可选）
│   │   ├── template1.html
│   │   └── template2.js
│   └── scripts/            # 脚本目录（可选）
│       ├── extract.py
│       └── merge.py
├── docx-editor/
│   ├── SKILL.md
│   ├── LICENSE.txt
│   └── scripts/
│       └── convert.py
└── webapp-testing/
    ├── SKILL.md
    └── examples/
        └── test-config.json
```

---

## SKILL.md 文件格式

SKILL.md 是 Markdown 文件，包含两个部分：
1. **YAML frontmatter**：告诉 AI"什么时候用我"
2. **Markdown 正文**：告诉 AI"具体怎么做"

### 基本结构

```markdown
---
# YAML frontmatter 开始（顶格）
name: skill-name                    # 必填：技能名称
description: 简要描述技能功能和使用场景  # 必填：技能描述
license: MIT                        # 可选：许可证
---

# Markdown 正文开始

## 使用场景
...

## 操作步骤
...
```

### YAML Frontmatter 字段说明

| 字段 | 是否必填 | 说明 |
|------|----------|------|
| `name` | ✅ 必填 | 技能的唯一标识符。必须小写，使用连字符代替空格，通常与技能目录名匹配 |
| `description` | ✅ 必填 | 描述技能的功能以及何时应该使用它 |
| `license` | ❌ 可选 | 适用于此技能的许可证描述 |

### 最小必填示例

```markdown
---
name: pdf-processing
description: 从 PDF 中提取文本和表格，填写表单，并合并文档
---

# PDF 处理

## 使用场景

当需要对 PDF 文件进行操作时使用，例如：
- 提取 PDF 文本或表格数据
- 填写 PDF 表单
- 合并多个 PDF 文件

## 提取文本

使用 `pdfplumber` 提取文本型 PDF 内容。扫描版 PDF 需配合 OCR 工具。

## 填写表单

1. 读取 PDF 表单字段
2. 按输入数据填充
3. 生成新文件
```

---

## 完整示例

### 示例 1：GitHub Actions 调试技能

```markdown
---
name: github-actions-failure-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows.
---

# GitHub Actions 失败调试指南

## 调试流程

调试 GitHub Actions 工作流失败时，按以下步骤操作：

1. 使用 `list_workflow_runs` 工具查看 PR 的最近工作流运行及其状态
2. 使用 `summarize_job_log_failures` 工具获取失败作业日志的 AI 摘要
3. 如需更多信息，使用 `get_job_logs` 或 `get_workflow_run_logs` 工具获取详细日志
4. 在自己的环境中尝试复现失败
5. 修复失败的构建

## 注意事项

- 提交更改前，确保已修复能复现的问题
- 不要让上下文窗口被数千行日志填满
```

### 示例 2：文档处理技能

```markdown
---
name: docx-processing
description: Word 文档创建、编辑和分析，支持修订跟踪、批注、格式保留
---

# Word 文档处理

## 使用场景

- 创建专业格式的 Word 文档
- 编辑现有文档并保留格式
- 分析文档结构和内容
- 添加批注和跟踪修订

## 核心功能

### 创建文档

使用 `python-docx` 库创建文档：

```python
from docx import Document

doc = Document()
doc.add_heading('标题', level=1)
doc.add_paragraph('正文内容')
doc.save('output.docx')
```

### 编辑文档

1. 打开现有文档
2. 修改段落和表格
3. 保留原有格式

### 格式化

- 使用样式保持一致性
- 支持页眉页脚
- 支持目录生成
```

### 示例 3：Web 应用测试技能

```markdown
---
name: webapp-testing
description: Guide for testing web applications, including unit tests, integration tests, and E2E tests
---

# Web 应用测试指南

## 测试类型

### 单元测试

测试独立的函数和组件：

```javascript
describe('calculateTotal', () => {
  it('should sum items correctly', () => {
    const result = calculateTotal([10, 20, 30]);
    expect(result).toBe(60);
  });
});
```

### 集成测试

测试多个组件的协作：

```javascript
describe('API Integration', () => {
  it('should fetch user data', async () => {
    const response = await fetch('/api/users/1');
    const data = await response.json();
    expect(data.id).toBe(1);
  });
});
```

### E2E 测试

使用 Playwright 或 Cypress：

```javascript
test('user login flow', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});
```

## 最佳实践

1. 保持测试独立
2. 使用有意义的测试名称
3. 每个测试只验证一个行为
4. 清理测试数据
```

---

## 创建技能的步骤

### 步骤 1：确定技能目录位置

根据使用范围选择存放位置：

| 类型 | 作用域 | 存放路径 |
|------|--------|----------|
| 项目技能 | 仅当前项目 | `.claude/skills/` 或 `.github/skills/` |
| 个人技能 | 所有项目共享 | `~/.claude/skills/` 或 `~/.copilot/skills/` |

### 步骤 2：创建技能目录

```bash
# 创建项目技能目录
mkdir -p .claude/skills/my-skill

# 或创建个人技能目录
mkdir -p ~/.claude/skills/my-skill
```

**命名规范：**
- 使用小写字母
- 使用连字符代替空格
- 例如：`pdf-editor`、`webapp-testing`、`code-review`

### 步骤 3：创建 SKILL.md 文件

在技能目录中创建 `SKILL.md` 文件：

```bash
# 进入技能目录
cd .claude/skills/my-skill

# 创建 SKILL.md
touch SKILL.md
```

### 步骤 4：编写 YAML Frontmatter

```markdown
---
name: my-skill
description: 清晰描述这个技能做什么，以及什么情况下应该使用它
license: MIT
---
```

### 步骤 5：编写技能指令

在 YAML frontmatter 后编写 Markdown 内容：

```markdown
---
name: my-skill
description: 技能描述
---

# 技能标题

## 使用场景

描述何时使用这个技能。

## 操作步骤

1. 第一步操作
2. 第二步操作
3. 第三步操作

## 注意事项

- 注意事项 1
- 注意事项 2

## 示例

提供具体的代码或使用示例。
```

### 步骤 6：添加资源文件（可选）

根据需要添加：

```
my-skill/
├── SKILL.md          # 主文件
├── reference.md      # 参考文档
├── scripts/          # 脚本
│   └── helper.py
└── templates/        # 模板
    └── example.json
```

### 步骤 7：测试技能

使用斜杠命令测试：

```
/my-skill
```

或在对话中自然触发：

```
帮我处理 PDF 文档
```

---

## 最佳实践

### 1. 编写清晰的描述

描述是 AI 判断何时使用技能的关键：

```markdown
❌ 不好：
description: PDF 处理

✅ 好：
description: 从 PDF 中提取文本和表格，填写表单，合并文档。当用户需要处理 PDF 文件时使用此技能。
```

### 2. 使用结构化的正文

```markdown
❌ 不好：
直接写一大段文字描述如何操作...

✅ 好：
## 使用场景
...

## 操作步骤
1. ...
2. ...

## 代码示例
...

## 注意事项
...
```

### 3. 提供具体示例

```markdown
## 代码示例

使用 pdfplumber 提取文本：

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```
```

### 4. 包含错误处理

```markdown
## 常见问题

### 问题：PDF 是扫描版

解决方案：使用 OCR 工具处理

```python
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path("scanned.pdf")
for image in images:
    text = pytesseract.image_to_string(image)
```
```

### 5. 按需引用资源文件

```markdown
## 参考文档

详细 API 参考，请参阅 [reference.md](./reference.md)。

## 脚本工具

使用 `scripts/extract.py` 进行批量提取：

```bash
python scripts/extract.py --input ./pdfs --output ./output
```
```

### 6. 保持技能单一职责

```markdown
❌ 不好：一个技能包含 PDF、Word、Excel 处理

✅ 好：分成三个独立技能
- pdf-processing
- docx-processing
- xlsx-processing
```

---

## 技能分类参考

### 文档处理类

| 技能名称 | 功能描述 | 适用场景 |
|----------|----------|----------|
| pdf-processing | PDF 文本/表格提取、表单填写、合并拆分 | PDF 文档处理 |
| docx-processing | Word 文档创建、编辑、格式保留 | 专业文档编辑 |
| xlsx-processing | Excel 表格创建、数据分析、图表生成 | 数据处理 |

### 开发工具类

| 技能名称 | 功能描述 | 适用场景 |
|----------|----------|----------|
| code-review | 代码审查最佳实践、检查清单 | 代码质量控制 |
| git-workflow | Git 工作流程、分支管理、提交规范 | 版本控制 |
| testing-guide | 单元测试、集成测试、E2E 测试指南 | 测试开发 |

### 创意工具类

| 技能名称 | 功能描述 | 适用场景 |
|----------|----------|----------|
| algorithmic-art | 使用代码创建算法艺术 | 生成艺术 |
| data-visualization | 数据可视化最佳实践 | 数据展示 |
| technical-writing | 技术文档写作规范 | 文档编写 |

---

## 常见问题

### Q1: SKILL.md 文件名可以改变吗？

**A:** 不可以。`SKILL.md` 是固定文件名，必须全大写，扩展名 `.md` 小写。AI 客户端只会查找这个固定名称的文件。

### Q2: 一个技能可以有多个 SKILL.md 吗？

**A:** 不可以。每个技能目录只能有一个 `SKILL.md` 文件。如果需要多个相关技能，应该创建多个技能目录。

### Q3: 如何在 SKILL.md 中引用其他文件？

**A:** 使用相对路径引用：

```markdown
详细 API 参考，请参阅 [reference.md](./reference.md)

使用脚本：`python ./scripts/helper.py`
```

### Q4: 技能可以依赖其他技能吗？

**A:** 可以在描述中提及依赖关系，但当前没有正式的依赖管理机制。建议在指令中说明：

```markdown
## 前置技能

此技能依赖于 `pdf-processing` 技能的基础知识。
```

### Q5: 如何更新技能？

**A:** 直接编辑 `SKILL.md` 文件即可。AI 客户端会在下次使用时加载最新内容。某些客户端可能需要刷新或重启。

### Q6: 技能可以包含二进制文件吗？

**A:** 可以，但需要注意：
- 大型二进制文件会影响加载速度
- 建议将脚本等资源放在 `scripts/` 目录
- 图片等资源放在 `assets/` 或 `images/` 目录

---

## 快速检查清单

### 创建技能检查清单

```
□ 目录结构
  □ 创建技能目录（小写+连字符）
  □ 位置正确（项目级或个人级）

□ SKILL.md 文件
  □ 文件名正确（SKILL.md）
  □ YAML frontmatter 格式正确
  □ name 字段已填写
  □ description 字段已填写
  □ description 清晰描述使用场景

□ 正文内容
  □ 包含使用场景说明
  □ 包含操作步骤
  □ 包含代码示例（如适用）
  □ 包含注意事项（如适用）

□ 可选资源
  □ 参考文档（如需要）
  □ 脚本文件（如需要）
  □ 模板文件（如需要）

□ 测试
  □ 使用斜杠命令测试
  □ 验证 AI 能正确理解指令
  □ 验证 AI 能正确触发技能
```

---

## 延伸阅读

### 相关概念

- **MCP (Model Context Protocol)**：用于能力扩展，连接 API、数据库等外部工具
- **Prompt Engineering**：编写有效提示词的技术
- **Agent**：能够自主执行任务的 AI 系统

### 学习资源

- 官方文档和示例
- 社区分享的技能库
- 最佳实践案例

---

## 总结

### 核心要点

- **Skill 本质**：教 AI 按固定流程做事的操作说明书
- **核心结构**：一个文件夹 + 一个 SKILL.md 文件
- **关键文件**：SKILL.md 包含 YAML frontmatter（元数据）和 Markdown 正文（指令）
- **存放位置**：项目级或个人级目录
- **命名规范**：小写字母 + 连字符

### 记住

Skills 不是复杂的系统，而是简单、实用的知识封装方式。从最小结构开始，根据需要逐步添加资源文件，重点是让 AI 能够理解何时使用以及如何执行。

**开始创建你的第一个 Skill 吧！** 🚀
