---
title: OpenSpec 中文文档 - AI原生规范驱动开发
date: 2026-04-23
tags:
  - AI
  - Vibe-coding
  - 开发
  - 规范
---

> AI 原生 · 规范驱动开发

## 让 AI 编码助手 真正理解你的意图

OpenSpec 是 AI-Native 的规范驱动开发系统，为 AI 编码助手提供轻量级规范层。在第一行代码编写之前，先与 AI 对齐需求，让开发过程更可预测、更高效。

→ 流动而非僵化  
→ 迭代而非瀑布  
→ 简单而非复杂  
→ 存量项目优先  
→ 从个人项目扩展到企业级

[快速开始](#快速开始) | [了解概念](#核心概念)

- ✅ 20+ 支持 AI 工具
- ✅ MIT 开源协议
- ✅ Node 20+ 运行环境

---

## 演示

### 三步完成一个完整变更

OpenSpec 简化了从想法到实现再到归档的完整开发流程

#### AI 对话 — 添加暗色模式

```
You: /opsx:propose add-dark-mode

AI: 已创建 openspec/changes/add-dark-mode/
    ✓ proposal.md — 为什么做、做什么
    ✓ specs/ — 需求与验收场景
    ✓ design.md — 技术实现方案
    ✓ tasks.md — 实现任务清单
    准备开始实现！

You: /opsx:apply

AI: 正在实现各项任务...
    ✓ 1.1 创建主题上下文 Provider
    ✓ 1.2 创建主题切换组件
    ✓ 2.1 添加 CSS 变量
    ✓ 2.2 接入 localStorage
    所有任务完成！

You: /opsx:archive

AI: 已归档至 openspec/changes/archive/2026-03-10-add-dark-mode/
    ✓ 规范已更新。准备好下一个功能！
```

[OpenSpec 控制台](#)

---

## 价值

### 为什么选择 OpenSpec？

AI 编码助手功能强大，但当需求只存在于聊天记录中时，结果往往难以预测

#### 🤝 先对齐再编码
人与 AI 在写代码前先就规范达成共识，避免方向性偏差带来的大量返工

#### 📁 井然有序
每个变更都有独立文件夹，包含提案、规范、设计和任务四个产物，清晰可查

#### 🌊 流动灵活
随时更新任意产物，无需遵守僵化的阶段门控，按自己的节奏推进

#### 🔧 工具生态广泛
通过 Slash 命令支持 20+ AI 助手，包括 Claude Code、Cursor、Windsurf 等主流工具

### 与同类产品对比

#### vs. Spec Kit (GitHub)
Spec Kit 全面但重量级，有严格阶段门控、大量 Markdown 文件、Python 环境依赖。**OpenSpec 更轻量，让你自由迭代。**

#### vs. Kiro (AWS)
Kiro 功能强大但锁定在其 IDE 内，且仅限 Claude 模型。**OpenSpec 支持你现有的全部工具。**

#### vs. 不用规范
没有规范的 AI 编码意味着模糊提示和不可预测的结果。**OpenSpec 在不增加繁文缛节的前提下带来可预测性。**

---

## 安装

### 安装指南

> 需要 Node.js 20.19.0 或更高版本

#### npm
```bash
npm install -g @fission-ai/openspec@latest
```

#### pnpm
```bash
pnpm add -g @fission-ai/openspec@latest
```

#### yarn
```bash
yarn global add @fission-ai/openspec@latest
```

#### bun
```bash
bun add -g @fission-ai/openspec@latest
```

#### Nix — 直接运行（无需安装）
```bash
nix run github:Fission-AI/OpenSpec -- init
```

#### Nix — 安装到 profile
```bash
nix profile install github:Fission-AI/OpenSpec
```

> 💡 **验证安装**
> ```bash
> openspec --version
> ```

---

## 快速开始

### 开始你的第一个变更

初始化项目，与 AI 协作完成一个完整的功能开发流程

#### 1. 初始化项目
进入你的项目目录，运行初始化命令。这将创建 OpenSpec 目录结构并为你的 AI 工具生成配置文件。

```bash
cd your-project
openspec init
```

#### 2. 创建你的第一个变更
在 AI 对话窗口中，使用 `/opsx:propose` 命令描述你想要构建的功能。AI 会自动创建所有必要的规划产物。

```
/opsx:propose add-dark-mode
```

#### 3. 实现任务
规划产物生成完毕后，运行 `/opsx:apply` 让 AI 按照任务清单逐步实现代码。

```
/opsx:apply
```

#### 4. 归档变更
完成实现后，运行 `/opsx:archive` 将 Delta 规范合并到主规范，并将变更文件夹移至归档目录。

```
/opsx:archive
```

> 🔥 **新功能：扩展工作流**
> 如需更细粒度的控制（`/opsx:new`、`/opsx:ff`、`/opsx:verify` 等），运行 `openspec config profile` 选择工作流，然后执行 `openspec update` 更新配置。

### 初始化后的目录结构

```
openspec/
├── specs/              # 主规范（当前系统行为的权威基准）
│   └── <domain>/
│       └── spec.md
├── changes/            # 提议中的变更（每个变更独立文件夹）
│   └── <change-name>/
│       ├── proposal.md    # 为什么做、做什么
│       ├── design.md      # 如何实现
│       ├── tasks.md       # 实现任务清单
│       └── specs/         # Delta 规范（正在变化的部分）
│           └── <domain>/
│               └── spec.md
└── config.yaml         # 项目配置（可选）
```

---

## 核心概念

### 理解 OpenSpec 的核心机制

深入了解规范、变更、产物和 Delta 机制如何协同工作

### 设计哲学

OpenSpec 围绕四个核心原则构建：

#### 🌊 流动而非僵化
传统规范系统将你锁定在阶段中：先规划，再实现，然后完成。OpenSpec 更灵活——你可以以任何有意义的顺序创建产物。

#### 🔄 迭代而非瀑布
需求会变化，理解会加深。最初看起来不错的方案在看到代码库后可能无法成立。OpenSpec 拥抱这种现实。

#### ✨ 简单而非复杂
一些规范框架需要大量设置、严格格式或繁重流程。OpenSpec 不挡你的路。几秒钟初始化，立即开始工作。

#### 🏗️ 存量项目优先
大多数软件工作不是从零开始，而是在已有系统上迭代改造。OpenSpec 基于 Delta 的方法，让描述"改了什么"变得自然而直观。

### 整体架构

OpenSpec 将你的工作组织为两个主要区域：

| 区域           | 说明                  |
| ------------ | ------------------- |
| **specs/**   | 权威基准，描述系统当前行为，归档时合并 |
| **changes/** | 提议中的修改，每个变更 = 一个文件夹 |

> 💡 这种分离是关键。你可以并行处理多个变更而不发生冲突，在变更影响主规范之前先进行审查，归档时 Delta 会干净地合并回主规范。

### 规范 (Specs)

规范使用结构化需求和场景来描述系统行为。一个典型的规范文件如下：

`openspec/specs/auth/spec.md`

```markdown
# Auth 规范

## 目的
应用程序的身份验证和会话管理。

## 需求

### 需求：用户身份验证
系统 SHALL 在登录成功时颁发 JWT 令牌。

#### 场景：有效凭据
- GIVEN 用户具有有效凭据
- WHEN 用户提交登录表单
- THEN 返回 JWT 令牌
- AND 用户被重定向到仪表板

#### 场景：无效凭据
- GIVEN 无效凭据
- WHEN 用户提交登录表单
- THEN 显示错误消息
- AND 不颁发令牌
```

| 元素 | 用途 |
|------|------|
| `## 目的` | 该规范领域的高层描述 |
| `### 需求：` | 系统必须具备的具体行为 |
| `#### 场景：` | 需求的具体示例（可验证的） |
| SHALL / MUST / SHOULD | RFC 2119 关键词，表示需求强度 |

> **规范的本质**：规范是 **行为契约**，而非实现计划。好的规范内容包括可观察行为、输入/输出/错误条件、外部约束。避免在规范中写内部类名、库或框架选择、逐步实现细节。

### 变更 (Changes)

变更是对系统的提议修改，打包为一个包含理解和实现所需一切的文件夹：

```
openspec/changes/add-dark-mode/
├── proposal.md           # 为什么做、做什么
├── design.md             # 如何实现（技术方案）
├── tasks.md              # 实现任务清单（带复选框）
├── .openspec.yaml        # 变更元数据（可选）
└── specs/                # Delta 规范
    └── ui/
        └── spec.md       # ui/spec.md 中正在变化的内容
```

- 📦 **一切在一起**：提案、设计、任务和规范都在一处。无需在不同位置寻找信息。
- ⚡ **并行工作**：多个变更可以同时存在而不冲突。在修复 bug 的同时开发新功能。
- 📚 **清晰历史**：归档时，变更移至 archive/ 并保留完整上下文，方便日后追溯原因。
- 🔍 **便于审查**：变更文件夹易于审查——打开它，阅读提案，检查设计，查看规范 Delta。

### 产物 (Artifacts)

产物是变更中指导工作的文档，它们相互构建，每个产物为下一个提供上下文：

```
proposal.md → specs/ → design.md → tasks.md
为什么做 + 范围 → 变化的内容 → 技术方案 → 实现步骤
```

#### 📄 Proposal — 提案文档

提案捕捉意图、范围和高层方案：

```markdown
# 提案：添加暗色模式

## 意图
用户希望有一个暗色模式选项，以减少夜间使用时的眼睛疲劳。

## 范围
包含：主题切换按钮、系统偏好检测、本地存储持久化
不包含：自定义颜色主题（未来工作）

## 方案
使用 CSS 自定义属性进行主题设置，React Context 进行状态管理。
```

#### 📐 Design — 设计文档

设计文档捕捉技术方案和架构决策：

```markdown
# 设计：添加暗色模式

## 技术方案
主题状态通过 React Context 管理以避免 prop drilling。
CSS 自定义属性支持运行时切换而无需切换 class。

## 架构决策

### 决策：Context 而非 Redux
使用 React Context 的原因：
- 简单的二值状态（亮/暗）
- 无复杂状态转换
- 避免引入 Redux 依赖
```

#### ✅ Tasks — 任务清单

任务是带复选框的具体实现步骤：

```markdown
# 任务

## 1. 主题基础设施
- [ ] 1.1 创建带有亮/暗状态的 ThemeContext
- [ ] 1.2 为颜色添加 CSS 自定义属性
- [ ] 1.3 实现 localStorage 持久化
- [ ] 1.4 添加系统偏好检测

## 2. UI 组件
- [ ] 2.1 创建 ThemeToggle 组件
- [ ] 2.2 在设置页面添加切换
- [ ] 2.3 更新 Header 包含快速切换

## 3. 样式
- [ ] 3.1 定义暗色主题调色板
- [ ] 3.2 更新组件使用 CSS 变量
```

### Delta 规范

Delta 规范是让 OpenSpec 适用于 **已有项目改造** 的关键概念。它们描述 **正在变化的内容**，而不是重新陈述整个规范。

```markdown
# Auth 的 Delta 规范

## ADDED Requirements（新增需求）

### 需求：双因素认证
系统 MUST 支持基于 TOTP 的双因素认证。

#### 场景：2FA 登录
- GIVEN 启用了 2FA 的用户
- WHEN 用户提交有效凭据
- THEN 呈现 OTP 挑战
- AND 仅在有效 OTP 后完成登录

## MODIFIED Requirements（修改需求）

### 需求：会话过期
系统 MUST 在 15 分钟不活动后使会话过期。
（之前：30 分钟）

## REMOVED Requirements（删除需求）

### 需求：记住我
（因支持 2FA 而废弃。用户应在每次会话重新认证。）
```

| Delta 节                    | 含义    | 归档时操作   |
| -------------------------- | ----- | ------- |
| `## ADDED Requirements`    | 新行为   | 追加到主规范  |
| `## MODIFIED Requirements` | 变更的行为 | 替换现有需求  |
| `## REMOVED Requirements`  | 废弃的行为 | 从主规范中删除 |

### Schema 机制

Schema 定义工作流的产物类型及其依赖关系。默认 Schema 为 `spec-driven`：

```yaml
name: spec-driven
artifacts:
  - id: proposal
    generates: proposal.md
    requires: []              # 无依赖，可以先创建

  - id: specs
    generates: specs/**/*.md
    requires: [proposal]      # 需要提案后才能创建

  - id: design
    generates: design.md
    requires: [proposal]      # 可与 specs 并行创建

  - id: tasks
    generates: tasks.md
    requires: [specs, design] # 需要 specs 和 design 都完成
```

```
proposal
   ↓
   ├──→ specs ──┐
   ├──→ design ─┤
   ↓            ↓
         tasks
```

### 完整工作流程

1. **启动变更**：`/opsx:propose` 或 `/opsx:new`
2. **创建产物**：proposal → specs → design → tasks
3. **实现任务**：`/opsx:apply`
4. **验证工作（可选）**：`/opsx:verify`
5. **归档变更**：Delta 合并入主规范，变更文件夹移至 archive/

### 术语表

| 术语 | 定义 |
|------|------|
| **产物 (Artifact)** | 变更中的文档（proposal、design、tasks 或 Delta 规范） |
| **归档 (Archive)** | 完成变更并将其 Delta 合并到主规范的过程 |
| **变更 (Change)** | 打包为带有产物的文件夹的系统提议修改 |
| **Delta 规范** | 描述变化（ADDED/MODIFIED/REMOVED）的规范 |
| **领域 (Domain)** | 规范的逻辑分组（如 auth/、payments/） |
| **需求 (Requirement)** | 系统必须具备的具体行为 |
| **场景 (Scenario)** | 需求的具体示例，通常采用 Given/When/Then 格式 |
| **Schema** | 产物类型及其依赖关系的定义 |
| **规范 (Spec)** | 描述系统行为的规格说明 |
| **权威基准** | openspec/specs/ 目录，包含当前一致同意的行为，是所有规范的最终依据 |

---

## 命令参考

### OPSX Slash 命令

在 AI 编码助手的对话界面中调用（如 Claude Code、Cursor、Windsurf）

#### 默认快速路径（core profile）

| 命令 | 用途 |
|------|------|
| `/opsx:propose` | 创建变更并一键生成规划产物 |
| `/opsx:explore` | 在提交变更前思考和探索想法 |
| `/opsx:apply` | 实现变更中的任务 |
| `/opsx:archive` | 归档已完成的变更 |

#### 扩展工作流命令（自定义选择）

| 命令 | 用途 |
|------|------|
| `/opsx:new` | 创建新变更脚手架 |
| `/opsx:continue` | 按依赖顺序创建下一个产物 |
| `/opsx:ff` | 快进：一次创建所有规划产物 |
| `/opsx:verify` | 验证实现是否与产物匹配 |
| `/opsx:sync` | 将 Delta 规范合并到主规范 |
| `/opsx:bulk-archive` | 批量归档多个变更 |
| `/opsx:onboard` | 引导式完整工作流教程 |

---

### `/opsx:propose`

> core profile

创建新变更并一步生成所有规划产物。这是 core profile 中的默认启动命令。

**语法**：`/opsx:propose [变更名或描述]`

| 参数 | 必填 | 描述 |
|------|------|------|
| `change-name-or-description` | 否 | kebab-case 名称或自然语言描述 |

**示例**：
```
You: /opsx:propose add-dark-mode

AI:  已创建 openspec/changes/add-dark-mode/
     ✓ proposal.md
     ✓ specs/ui/spec.md
     ✓ design.md
     ✓ tasks.md
     准备好实现。运行 /opsx:apply。
```

> 如果你想分步骤控制产物创建，请启用扩展工作流并使用 `/opsx:new` + `/opsx:continue`。

---

### `/opsx:explore`

> core profile

在提交变更之前，思考想法、调查问题、澄清需求。

**语法**：`/opsx:explore [话题]`

**示例**：
```
You: /opsx:explore

AI:  你想探索什么？

You: 如何为移动端应用处理身份验证？

AI:  让我来研究你当前的认证设置...
     [分析代码库]

     我看到你在 Web 端使用了基于 session 的认证。
     对于移动端，我们有三种主要选择：

     1. JWT 令牌（无状态，支持离线）
     2. OAuth2（如需第三方登录）
     3. 扩展当前 session（更简单，但需要连接）

     你的 API 已经配置了 CORS。你对哪个方向感兴趣？

You: 让我们用 JWT。能开始一个变更吗？

AI:  准备好了。运行 /opsx:propose add-jwt-auth 开始。
```

> 探索期间不会创建产物。适合在决定之前比较多种方案。

---

### `/opsx:new`

> 扩展工作流

创建新变更脚手架。创建变更文件夹，等待你用 `/opsx:continue` 或 `/opsx:ff` 生成产物。

**语法**：`/opsx:new [变更名] [--schema <schema-name>]`

**示例**：
```
You: /opsx:new add-dark-mode

AI:  已创建 openspec/changes/add-dark-mode/
     Schema: spec-driven

     准备创建: proposal
     使用 /opsx:continue 创建，或 /opsx:ff 创建所有产物。
```

> 使用描述性名称：`add-feature`、`fix-bug`、`refactor-module`。避免使用 `update`、`changes`、`wip` 等泛称。

---

### `/opsx:continue`

> 扩展工作流

在依赖链中创建下一个产物。每次创建一个产物以实现增量进度。

**语法**：`/opsx:continue [变更名]`

**示例**：
```
You: /opsx:continue

AI:  变更: add-dark-mode

     产物状态:
     ✓ proposal    (完成)
     ◆ specs       (就绪)
     ◆ design      (就绪)
     ○ tasks       (阻塞 - 需要: specs)

     正在创建 specs...
     ✓ 已创建 openspec/changes/add-dark-mode/specs/ui/spec.md

     现在可用: tasks
     运行 /opsx:continue 创建下一个产物。
```

> 当你想在继续之前审查每个产物时使用。可以在继续之前编辑已创建的产物。

---

### `/opsx:ff`

> 扩展工作流

快进产物创建。一次创建所有规划产物。

**语法**：`/opsx:ff [变更名]`

**示例**：
```
You: /opsx:ff add-dark-mode

AI:  快进 add-dark-mode...

     ✓ 创建 proposal.md
     ✓ 创建 specs/ui/spec.md
     ✓ 创建 design.md
     ✓ 创建 tasks.md

     所有规划产物完成！
     准备好实现。运行 /opsx:apply 开始。
```

> 当你对要构建的内容有清晰认识时使用。适合中小型功能。

---

### `/opsx:apply`

> core profile

实现变更中的任务。逐步处理任务列表，编写代码并勾选完成项。

**语法**：`/opsx:apply [变更名]`

**示例**：
```
You: /opsx:apply

AI:  实现 add-dark-mode...

     读取 tasks.md:
     - [ ] 1.1 创建 ThemeContext
     - [ ] 1.2 添加 CSS 自定义属性
     - [ ] 1.3 实现 localStorage 持久化

     处理 1.1: 创建 ThemeContext...
     [创建 src/context/ThemeContext.tsx]
     ✓ 1.1 完成

     处理 1.2: 添加 CSS 自定义属性...
     [更新 src/styles/globals.css]
     ✓ 1.2 完成
     ...
```

> 如果被打断可以恢复。可以通过指定变更名来并行处理多个变更。完成状态在 tasks.md 复选框中跟踪。

---

### `/opsx:verify`

> 扩展工作流

验证实现是否与变更产物匹配。从完整性、正确性和一致性三个维度检查。

**语法**：`/opsx:verify [变更名]`

| 维度 | 验证内容 |
|------|----------|
| **完整性** | 所有任务完成、所有需求已实现、场景已覆盖 |
| **正确性** | 实现与规范意图匹配、边缘情况已处理 |
| **一致性** | 设计决策在代码中有体现、模式一致 |

**示例**：
```
You: /opsx:verify

AI:  验证 add-dark-mode...

     完整性
     ✓ tasks.md 中的所有 8 个任务都已完成
     ✓ 规范中的所有需求都有对应代码
     ⚠ 场景"系统偏好检测"没有测试覆盖

     正确性
     ✓ 实现与规范意图匹配
     ✓ 场景中的边缘情况已处理

     一致性
     ✓ 设计决策在代码结构中有体现
     ⚠ 设计提到"CSS 变量"但实现使用了 Tailwind 类

     总结
     关键问题: 0 | 警告: 2 | 可以归档: 是（有警告）
```

---

### `/opsx:sync`

> 扩展工作流（可选）

将 Delta 规范从变更合并到主规范。归档时会提示同步，通常无需手动运行。

**语法**：`/opsx:sync [变更名]`

| 场景 | 是否使用 sync？ |
|------|----------------|
| 长期变更，归档前想先将规范同步到主分支 | 是 |
| 多个并行变更需要最新的基础规范 | 是 |
| 快速变更，直接归档 | 否（归档会处理） |

---

### `/opsx:archive`

> core profile

归档已完成的变更。完成变更并将其移至归档文件夹。

**语法**：`/opsx:archive [变更名]`

**示例**：
```
You: /opsx:archive

AI:  归档 add-dark-mode...

     产物状态:
     ✓ proposal.md 存在
     ✓ specs/ 存在
     ✓ design.md 存在
     ✓ tasks.md 存在 (8/8 任务完成)

     Delta 规范: 尚未同步
     → 现在同步？(推荐)

You: 是

AI:  ✓ 已将规范同步到 openspec/specs/ui/spec.md
     ✓ 已移至 openspec/changes/archive/2026-03-10-add-dark-mode/

     变更归档成功。
```

---

### `/opsx:bulk-archive`

> 扩展工作流

批量归档多个已完成的变更。自动处理变更之间的规范冲突。

**语法**：`/opsx:bulk-archive [变更名...]`

**示例**：
```
You: /opsx:bulk-archive

AI:  找到 3 个已完成的变更:
     - add-dark-mode (8/8 任务完成)
     - fix-login-bug (3/3 任务完成)
     - update-footer (2/2 任务完成)

     检查规范冲突...
     ⚠ add-dark-mode 和 update-footer 都触及 specs/ui/

     检查代码库以解决...
     两个变更都已实现。将按时间顺序合并:
     1. add-dark-mode (1 月 20 日创建)
     2. update-footer (1 月 22 日创建)

     归档所有 3 个变更？

You: 是

AI:  ✓ 已归档 add-dark-mode
     ✓ 已归档 fix-login-bug
     ✓ 已归档 update-footer
```

---

### `/opsx:onboard`

> 扩展工作流

完整工作流的引导式入门教程，使用你的真实代码库进行交互式演示。

**语法**：`/opsx:onboard`

> 📋 **包含 11 个阶段**
> 欢迎与代码库分析 → 发现改进机会 → 创建变更 → 编写提案 → 创建规范 → 编写设计 → 创建任务 → 实现任务 → 验证实现 → 归档变更 → 总结与后续步骤
> 
> 适合首次使用 OpenSpec 的用户。使用真实代码，不是玩具示例。完整完成约需 15-30 分钟。

---

### 不同 AI 工具的命令语法

| 工具 | 语法示例 |
|------|----------|
| Claude Code | `/opsx:propose`、`/opsx:apply` |
| Cursor | `/opsx-propose`、`/opsx-apply` |
| Windsurf | `/opsx-propose`、`/opsx-apply` |
| Copilot (IDE) | `/opsx-propose`、`/opsx-apply` |
| Trae | `/openspec-propose`、`/openspec-apply-change` |

---

## CLI 参考

### 终端命令完整参考

openspec CLI 提供项目设置、验证、状态检查和管理的终端命令

| 分类 | 命令 | 用途 |
|------|------|------|
| **设置** | `init`、`update` | 初始化和更新项目中的 OpenSpec |
| **浏览** | `list`、`view`、`show` | 探索变更和规范 |
| **验证** | `validate` | 检查变更和规范的问题 |
| **生命周期** | `archive` | 完成已完成的变更 |
| **工作流** | `status`、`instructions`、`templates`、`schemas` | 产物驱动的工作流支持 |
| **Schema** | `schema init`、`schema fork`、`schema validate`、`schema which` | 创建和管理自定义工作流 |
| **配置** | `config` | 查看和修改设置 |
| **工具** | `feedback`、`completion` | 反馈和 Shell 集成 |

---

### 初始化与更新

#### `openspec init`
在项目中初始化 OpenSpec

**语法**：
```bash
openspec init [path] [options]
```

| 选项 | 描述 |
|------|------|
| `--tools <list>` | 非交互式配置 AI 工具。使用 all、none 或逗号分隔的列表 |
| `--force` | 自动清理旧文件，无需提示 |
| `--profile <profile>` | 覆盖此次初始化的全局 profile（core 或 custom） |

**示例**：
```bash
# 交互式初始化
openspec init

# 非交互式：配置 Claude 和 Cursor
openspec init --tools claude,cursor

# 配置所有支持的工具
openspec init --tools all

# 覆盖 profile
openspec init --profile core
```

#### `openspec update`
升级 CLI 后更新 OpenSpec 指令文件

```bash
# npm 升级后更新指令文件
npm update @fission-ai/openspec
openspec update
```

---

### 浏览命令

#### `openspec list`
列出项目中的变更或规范

```bash
# 列出所有活跃变更
openspec list

# 列出所有规范
openspec list --specs

# JSON 输出（用于脚本）
openspec list --json
```

#### `openspec show`
显示变更或规范的详情

```bash
# 显示特定变更
openspec show add-dark-mode

# JSON 输出用于解析
openspec show add-dark-mode --json
```

---

### 验证命令

#### `openspec validate`
验证变更和规范的结构问题

```bash
# 验证特定变更
openspec validate add-dark-mode

# 验证所有变更
openspec validate --changes

# 验证所有内容并输出 JSON（用于 CI）
openspec validate --all --json

# 严格模式
openspec validate --all --strict --concurrency 12
```

---

### 生命周期命令

#### `openspec archive`
归档已完成的变更并将 Delta 规范合并到主规范

```bash
# 归档特定变更
openspec archive add-dark-mode

# 无提示归档（CI/脚本）
openspec archive add-dark-mode --yes

# 归档不影响规范的工具变更
openspec archive update-ci-config --skip-specs
```

---

### 工作流命令

#### `openspec status`
显示变更的产物完成状态

```bash
openspec status --change add-dark-mode

# 输出:
# Change: add-dark-mode
# Schema: spec-driven
# Progress: 2/4 artifacts complete
#
# [x] proposal
# [ ] design
# [x] specs
# [-] tasks (blocked by: design)
```

---

### Schema 命令

#### `openspec schema init`
创建新的项目本地 Schema

```bash
# 交互式创建 Schema
openspec schema init research-first

# 非交互式
openspec schema init rapid \
  --description "快速迭代工作流" \
  --artifacts "proposal,tasks" \
  --default
```

#### `openspec schema fork`
复制现有 Schema 到项目以进行自定义

```bash
# Fork 内置的 spec-driven schema
openspec schema fork spec-driven my-workflow
```

> 🔢 **Schema 优先级**
> 1. 项目级：`openspec/schemas/<name>/`
> 2. 用户级：`~/.local/share/openspec/schemas/<name>/`
> 3. 包级：内置 Schema

---

### 配置命令

#### `openspec config`
查看和修改全局 OpenSpec 配置

```bash
# 列出所有设置
openspec config list

# 获取特定值
openspec config get telemetry.enabled

# 设置值
openspec config set telemetry.enabled false

# 配置工作流 profile
openspec config profile

# 快速切换到 core profile
openspec config profile core

# 在编辑器中编辑
openspec config edit
```

---

### 环境变量

| 变量 | 描述 |
|------|------|
| `OPENSPEC_CONCURRENCY` | 批量验证的默认并发数（默认: 6） |
| `EDITOR` 或 `VISUAL` | openspec config edit 使用的编辑器 |
| `NO_COLOR` | 设置时禁用彩色输出 |
| `OPENSPEC_TELEMETRY=0` | 禁用遥测数据收集 |
| `DO_NOT_TRACK=1` | 全局禁用追踪 |

---

## 工作流

### 常见工作流模式

选择最适合你当前场景的工作流模式

#### 默认快速路径（core profile）
```
/opsx:propose → /opsx:apply → /opsx:archive
```
> 新安装默认使用 core，包含：propose、explore、apply、archive

#### 扩展工作流（自定义选择）
```
/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive
```

> 启用扩展工作流：
> ```bash
> openspec config profile
> openspec update
> ```

---

### 场景化工作流

#### ⚡ 快速功能（清晰需求）
```
/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive
```
**适用于**：中小型功能、Bug 修复、直接明了的变更

#### 🔍 探索式（需求不明确）
```
/opsx:explore → /opsx:new → /opsx:continue → ... → /opsx:apply
```
**适用于**：性能优化、调试、架构决策、需求不清晰

#### 🔀 并行变更（多任务）
```
变更 A 进行中时 → 切换上下文 → 同时处理变更 B → /opsx:bulk-archive
```
**适用于**：并行工作流、紧急中断、团队协作

---

### 何时使用 `/opsx:ff` 还是 `/opsx:continue`

| 场景 | 推荐使用 |
|------|----------|
| 需求清晰，准备构建 | `/opsx:ff` |
| 探索中，想逐步审查 | `/opsx:continue` |
| 想在创建规范前迭代提案 | `/opsx:continue` |
| 时间紧迫，需要快速推进 | `/opsx:ff` |
| 复杂变更，需要精细控制 | `/opsx:continue` |

> **经验法则**：如果你能预先描述完整范围，使用 `/opsx:ff`。如果你在过程中摸索，使用 `/opsx:continue`。

---

### 最佳实践

#### 01 保持变更聚焦
每个变更对应一个逻辑工作单元。"添加功能 X 同时重构 Y"应考虑拆成两个独立变更。

#### 02 需求不明确时使用 explore
在提交变更前先探索问题空间，探索可以澄清思路，避免错误方向带来的返工。

#### 03 归档前先 verify
使用 `/opsx:verify` 检查实现是否与产物匹配，在关闭变更前捕获不匹配问题。

#### 04 清晰命名变更
好名称让 `openspec list` 更有用：`add-dark-mode`、`fix-login-redirect`、`implement-2fa`。避免 `feature-1`、`update`、`wip`。

---

## 定制化

### 让 OpenSpec 按你的方式工作

三个级别的自定义，满足从个人到企业的不同需求

| 级别 | 用途 | 最适合 |
|------|------|--------|
| **项目配置** | 设置默认值、注入上下文/规则 | 大多数团队 |
| **自定义 Schema** | 定义你自己的工作流产物 | 有独特流程的团队 |
| **全局覆盖** | 跨所有项目共享 Schema | 高级用户 |

---

### 项目配置（openspec/config.yaml）

最简单的自定义方式，让你可以：

- 设置默认 Schema — 跳过每个命令的 `--schema`
- 注入项目上下文 — AI 了解你的技术栈、约定等
- 添加每产物规则 — 特定产物的自定义指导

```yaml
schema: spec-driven

context: |
  技术栈: TypeScript, React, Node.js, PostgreSQL
  API 风格: RESTful，文档在 docs/api.md
  测试: Jest + React Testing Library
  我们重视所有公共 API 的向后兼容性

rules:
  proposal:
    - 包含回滚计划
    - 确认受影响的团队
  specs:
    - 使用 Given/When/Then 格式
    - 在发明新模式之前引用现有模式
```

---

### 自定义 Schema

当项目配置不够用时，创建完全自定义的工作流 Schema。

#### Fork 现有 Schema（推荐）
```bash
openspec schema fork spec-driven my-workflow
```

#### 示例：快速迭代工作流
`openspec/schemas/rapid/schema.yaml`
```yaml
name: rapid
version: 1
description: 最小开销的快速迭代

artifacts:
  - id: proposal
    generates: proposal.md
    description: 快速提案
    template: proposal.md
    instruction: |
      为此变更创建简短提案。
      重点说明做什么和为什么，跳过详细规范。
    requires: []

  - id: tasks
    generates: tasks.md
    description: 实现清单
    template: tasks.md
    requires: [proposal]

apply:
  requires: [tasks]
  tracks: tasks.md
```

#### 示例：添加审查步骤
```bash
# Fork 默认 Schema 并添加审查步骤
openspec schema fork spec-driven with-review

# 然后编辑 schema.yaml 添加:
  - id: review
    generates: review.md
    description: 实现前的审查清单
    template: review.md
    instruction: |
      基于设计创建审查清单。
      包含安全、性能和测试注意事项。
    requires:
      - design
```

---

## 集成

### 支持的 AI 工具

OpenSpec 与 28+ AI 编码助手集成，运行 `openspec init` 时自动配置

| 工具 | 工具 | 工具 |
|------|------|------|
| Claude Code | Cursor | Windsurf |
| GitHub Copilot | Kiro | Cline |
| RooCode | Continue | Qoder |
| Gemini CLI | OpenCode | Amazon Q |
| Trae | Codex | Pi |
| Factory Droid | Auggie | CoStrict |
| Crush | iFlow | Kilo Code |
| Qwen Code | Antigravity | CodeBuddy |
| IBM Bob Shell | ForgeCode | Junie |
| Lingma IDE | | |

---

### 非交互式安装

用于 CI/CD 或脚本化安装，可使用 `--tools` 和 `--profile` 参数：

```bash
# 配置特定工具
openspec init --tools claude,cursor

# 配置所有支持的工具
openspec init --tools all

# 跳过工具配置
openspec init --tools none

# 指定 profile 覆盖
openspec init --profile core
```

---

### 工作流相关的安装

| Profile | 包含的工作流 |
|---------|--------------|
| **Core（默认）** | propose、explore、apply、archive |
| **Custom（自定义）** | 可选择：propose、explore、new、continue、apply、ff、sync、archive、bulk-archive、verify、onboard 的任意子集 |

---

## 多语言

### 多语言支持

配置 OpenSpec 以非英语生成产物

#### 快速配置

在 `openspec/config.yaml` 中添加语言指令即可：

**中文（简体）配置示例**
```yaml
schema: spec-driven

context: |
  语言：中文（简体）
  所有产出物必须用简体中文撰写。

  # 你的其他项目上下文在下面...
  技术栈: TypeScript, React, Node.js
```

#### 其他语言示例

**葡萄牙语**
```yaml
context: |
  Language: Portuguese (pt-BR)
  All artifacts must be written in Brazilian Portuguese.
```

**西班牙语**
```yaml
context: |
  Idioma: Español
  Todos los artefactos deben escribirse en español.
```

**日语**
```yaml
context: |
  言語：日本語
  すべての成果物は日本語で作成してください。
```

**法语**
```yaml
context: |
  Langue : Français
  Tous les artefacts doivent être rédigés en français.
```

---

## 贡献

### 参与贡献

#### 🐛 小型修复
Bug 修复、错别字更正和小改进可以直接作为 PR 提交。

#### 🏗️ 较大变更
对于新功能、重大重构或架构变更，请先提交 OpenSpec 变更提案，以便在实现开始前对齐意图和目标。

#### 🤖 AI 生成代码
欢迎 AI 生成的代码，只要经过测试和验证。PR 应注明使用的 AI 工具和模型（例如"使用 Claude Code claude-opus-4-5 生成"）。

---

### 开发指南

```bash
# 安装依赖
pnpm install

# 构建
pnpm run build

# 测试
pnpm test

# 本地开发 CLI
pnpm run dev
# 或
pnpm run dev:cli

# Commit 规范（单行）
type(scope): subject
```

> 📋 **写提案时**，请牢记 OpenSpec 的哲学：我们服务于不同编码助手、模型和用例的广泛用户。变更应该对所有人都适用。

---

### 遥测数据

OpenSpec 收集匿名使用统计数据。我们只收集命令名称和版本以了解使用模式。不收集参数、路径、内容或个人信息。在 CI 中自动禁用。

```bash
# 禁用遥测
export OPENSPEC_TELEMETRY=0
# 或
export DO_NOT_TRACK=1
```

---

## 实战指南

### OpenSpec 上手实践指南

> 从零开始掌握规范驱动开发，构建高质量 AI 协作工作流

> 📚 **本指南适合谁？**
> 希望系统学习 OpenSpec 的开发者，包括：想要提升 AI 编码效率的个人开发者、希望规范化 AI 协作流程的团队 Leader、以及对规范驱动开发（Spec-Driven Development）感兴趣的技术人员。

---

## Part 1: 深入理解 OpenSpec

> 不只是工具，更是一种全新的 AI 协作范式

### 1.1 OpenSpec 是什么？

OpenSpec 是一个 **轻量级规范驱动开发框架**，专为 AI 编码助手时代设计。它通过建立「人机对齐」的规范层，让开发者和 AI 在编写代码之前先达成共识。

#### 核心定位
OpenSpec 不是取代 AI 编码助手，而是 **增强它们的可控性和可预测性**。它让 AI 从「被动响应聊天历史」转变为「主动遵循结构化规范」。

| 维度 | 传统 AI 编码 | OpenSpec 增强 |
|------|--------------|---------------|
| **需求来源** | 聊天历史（易丢失、难追溯） | 结构化规范文件（可版本控制） |
| **实现过程** | 一次性生成，难以迭代 | 任务驱动，可暂停、可恢复 |
| **变更管理** | 无记录，难以审计 | Delta 机制，完整审计轨迹 |
| **团队协作** | 依赖个人 prompt 技巧 | 标准化工作流，经验可复用 |

---

### 1.2 为什么需要 OpenSpec？

AI 编码助手（如 Claude Code、Cursor、Copilot）的普及带来了三个核心痛点：

#### 😵 痛点一：AI 幻觉与偏离
需求只存在于聊天中，AI 容易「忘记」上下文或产生幻觉。长对话后，AI 可能偏离最初意图，实现出完全不符合预期的功能。

#### 🔄 痛点二：迭代成本高
没有结构化记录，每次修改都需要重新描述上下文。复杂功能的迭代开发变成「从头再来」，效率极低。

#### 👥 痛点三：团队协作难
个人 prompt 技巧无法复用，团队成员的 AI 协作质量参差不齐。缺乏统一的工作流程和质量标准。

#### OpenSpec 的解决方案

1. **规范先行**：在编码前通过 Proposal 明确意图、通过 Specs 定义行为契约、通过 Design 确定技术方案
2. **任务驱动**：Tasks 文件作为实现清单，AI 按任务逐项执行，可随时暂停和恢复，进度可追踪
3. **Delta 机制**：变更以增量方式记录（ADDED/MODIFIED/REMOVED），完美适配存量项目改造场景

---

### 1.3 核心架构解析

理解 OpenSpec 的架构设计，是高效使用它的基础。

#### OpenSpec 目录结构
```
openspec/
├── specs/                    # 【权威基准】系统当前行为的完整描述
│   ├── auth/
│   │   └── spec.md           # 认证模块规范
│   ├── payments/
│   │   └── spec.md           # 支付模块规范
│   └── ui/
│       └── spec.md           # UI 行为规范
│
├── changes/                  # 【变更工作区】正在进行的修改
│   ├── add-dark-mode/        # 变更文件夹（每个变更独立）
│   │   ├── proposal.md       # 提案：为什么做、做什么
│   │   ├── specs/            # Delta 规范：正在变化的部分
│   │   │   └── ui/
│   │   │       └── spec.md   # ADDED/MODIFIED/REMOVED 格式
│   │   ├── design.md         # 设计：如何实现
│   │   ├── tasks.md          # 任务：具体实现步骤
│   │   └── .openspec.yaml    # 变更元数据
│   │
│   └── archive/              # 【历史归档】已完成的变更
│       └── 2025-01-24-add-auth/
│
├── schemas/                  # 【可选】自定义工作流 Schema
│   └── my-workflow/
│       ├── schema.yaml
│       └── templates/
│
└── config.yaml               # 项目配置（上下文、规则等）
```

> 💡 **架构设计哲学**
> `specs/` 与 `changes/` 的分离是 OpenSpec 的核心设计。这确保了：① 主规范始终保持稳定 ② 多个变更可并行进行而不冲突 ③ 归档时 Delta 能干净合并回主规范

---

### 1.4 产物（Artifact）体系详解

OpenSpec 的产物体系遵循「渐进式明确」原则，每个产物为下一个提供上下文。

#### 📋 Proposal（提案）
**职责**：回答「为什么做」和「做什么」
- Intent（意图）：解决什么问题
- Scope（范围）：包含/不包含什么
- Approach（方案）：高层次的实现思路

> 💡 Proposal 是与 AI 对齐的第一步，确保你们对「做什么」有共识

#### 📐 Specs（规范）
**职责**：定义系统的行为契约
- Requirements：系统必须具备的行为
- Scenarios：可验证的具体场景（Given/When/Then）
- Delta 格式：ADDED / MODIFIED / REMOVED

> 💡 Specs 是行为契约，不是实现细节。关注「系统做什么」而非「代码怎么写」

#### 🏗️ Design（设计）
**职责**：回答「如何实现」
- Technical Approach：技术方案概述
- Architecture Decisions：关键决策及理由
- Data Flow：数据流和组件交互

> 💡 Design 记录架构决策的「为什么」，方便后续维护和回溯

#### ✅ Tasks（任务）
**职责**：具体的实现步骤清单
- 分组编号：按模块分组，层级编号（1.1, 1.2...）
- 复选框：`- [ ]` 未完成 / `- [x]` 已完成
- 可追踪：AI 按任务执行，进度实时可见

> 💡 Tasks 是 AI 实现代码的「导航图」，粒度要适中（一个任务 ≈ 一次提交）

#### 产物依赖关系图
```
proposal
   ↓
   ├──→ specs ──┐
   ├──→ design ─┤
   ↓            ↓
         tasks
           ↓
    implement（/opsx:apply）
```

---

## Part 2: OpenSpec 最佳实践

> 从实战经验中提炼的高效使用模式

### 2.1 工作流选择策略

OpenSpec 提供两种主要工作流，选择合适的工作流能显著提升效率。

#### ✅ Core 快速路径（推荐）
```
/opsx:propose → /opsx:apply → /opsx:archive
```

**适用场景**：
- 需求明确的中小型功能
- Bug 修复和小型优化
- 时间紧迫需要快速交付
- 个人项目或快速原型

**优势**：一条命令生成所有产物，最小化仪式感

#### 🔧 Expanded 扩展路径（精细控制）
```
/opsx:new → /opsx:continue → /opsx:apply → /opsx:verify → /opsx:archive
```

**适用场景**：
- 复杂功能开发（跨模块、跨团队）
- 需求不明确，需要探索
- 需要逐步审查每个产物
- 团队协作项目

**优势**：每个产物可单独创建和审查，控制粒度更细

#### 工作流选择决策树
```
你能在 30 秒内描述清楚「做什么」吗？
├── 是 → 需求明确
│   ├── 功能复杂度高（>10 个任务）？
│   │   ├── 是 → 使用 Expanded（/opsx:new + /opsx:ff）
│   │   └── 否 → 使用 Core（/opsx:propose）
│   └── 需要团队审查？
│       ├── 是 → 使用 Expanded（/opsx:continue 逐步审查）
│       └── 否 → 使用 Core（/opsx:propose）
│
└── 否 → 需求不明确
    └── 先使用 /opsx:explore 探索，然后选择合适路径
```

---

### 2.2 变更命名规范

好的命名让 `openspec list` 一目了然，也方便日后追溯。

| 模式 | 示例 | 适用场景 |
|------|------|----------|
| `add-<feature>` | `add-dark-mode`、`add-export-csv` | 新增功能 |
| `fix-<issue>` | `fix-login-redirect`、`fix-memory-leak` | Bug 修复 |
| `refactor-<module>` | `refactor-auth-service` | 代码重构 |
| `optimize-<target>` | `optimize-query-performance` | 性能优化 |
| `update-<component>` | `update-react-18` | 依赖更新 |
| `implement-<spec>` | `implement-2fa` | 实现某个规范 |

> **命名原则**：动词 - 名词格式，kebab-case 连字符分隔，具体描述意图。避免使用 `feature-1`、`update`、`wip` 等模糊命名。

---

### 2.3 高质量规范编写

规范是 OpenSpec 的核心，写好规范是提高 AI 实现质量的关键。

#### ✅ 好的规范示例
`specs/auth/spec.md`
```markdown
# Auth 规范

## 目的
用户身份验证和会话管理。

## 需求

### 需求：JWT 令牌认证
系统 SHALL 在登录成功时颁发 JWT 令牌。

#### 场景：有效凭据登录
- GIVEN 用户具有有效的邮箱和密码
- WHEN 用户提交登录表单
- THEN 系统返回包含 accessToken 和 refreshToken 的响应
- AND accessToken 有效期为 15 分钟
- AND refreshToken 有效期为 7 天
- AND 用户被重定向到 dashboard 页面

#### 场景：无效凭据登录
- GIVEN 用户提交无效的邮箱或密码
- WHEN 用户提交登录表单
- THEN 系统返回 401 状态码
- AND 响应包含 "Invalid credentials" 错误信息
- AND 不颁发任何令牌
```

#### ❌ 避免的写法

```markdown
# 不好的规范 - 包含实现细节

### 需求：登录功能
使用 bcrypt 比较密码，用 jsonwebtoken 库生成 JWT。
在 UserController.login() 方法中实现，
调用 AuthService.validatePassword() 验证...
```

> ⚠️ **规范 ≠ 实现计划**
> 规范描述「系统应该做什么」（行为契约），不是「代码怎么写」（实现细节）。内部类名、库选择、代码结构应该放在 design.md 中。

---

### 2.4 Delta 规范高级用法

Delta 机制是 OpenSpec 适配「存量项目改造」的核心能力。

#### ADDED：新增需求
```markdown
## ADDED Requirements

### 需求：双因素认证
系统 MUST 支持基于 TOTP 的双因素认证。

#### 场景：启用 2FA
- GIVEN 用户未启用 2FA
- WHEN 用户在设置页面启用 2FA
- THEN 显示二维码供 Authenticator App 扫描
- AND 用户需输入验证码确认激活
```
> 归档效果：追加到主规范末尾

#### MODIFIED：修改现有需求
```markdown
## MODIFIED Requirements

### 需求：会话过期时间
系统 MUST 在 15 分钟不活动后使会话过期。
（之前：30 分钟）

#### 场景：空闲超时
- GIVEN 已认证的会话
- WHEN 15 分钟内无任何操作
- THEN 会话被作废
- AND 用户需重新登录
```
> 归档效果：替换主规范中同名需求

#### REMOVED：删除需求
```markdown
## REMOVED Requirements

### 需求：记住我功能
（因支持 2FA 而废弃。用户应在每次会话重新认证。）
```
> 归档效果：从主规范中删除该需求

---

### 2.5 项目配置最佳实践

合理的 `config.yaml` 配置能显著提升 AI 产物质量。

#### 推荐配置模板
`openspec/config.yaml`
```yaml
schema: spec-driven

# 项目上下文 - AI 生成产物时会参考这些信息
context: |
  # 项目概述
  项目名称：MyApp
  项目类型：Web 应用

  # 技术栈
  前端：React 18 + TypeScript + Tailwind CSS
  后端：Node.js + Express + PostgreSQL
  测试：Jest + React Testing Library

  # 代码规范
  - 使用 ESLint + Prettier 进行代码格式化
  - 组件使用函数式组件 + Hooks
  - API 遵循 RESTful 设计
  - 所有公共 API 需保持向后兼容

  # 分支策略
  - main: 生产分支
  - develop: 开发分支
  - feature/*: 功能分支

# 每产物规则 - 针对特定产物的额外指导
rules:
  proposal:
    - 必须包含回滚计划
    - 说明对现有功能的影响
    - 列出需要协调的团队
  specs:
    - 使用 Given/When/Then 格式编写场景
    - 优先引用现有模式，避免重复发明
    - 包含边界条件和异常场景
  design:
    - 说明关键技术决策的理由
    - 列出受影响的文件和模块
    - 考虑性能和安全影响
  tasks:
    - 任务粒度适中（每个任务约 1-2 小时工作量）
    - 按模块分组，使用层级编号
    - 包含必要的测试任务
```

---

## Part 3: 从零开始实践

> 通过完整案例掌握 OpenSpec 工作流

### 3.1 环境准备

#### 1. 安装 OpenSpec
```bash
# 使用 npm 全局安装（推荐）
npm install -g @fission-ai/openspec@latest

# 验证安装
openspec --version
```

#### 2. 初始化项目
```bash
# 进入项目目录
cd your-project

# 交互式初始化（推荐）
openspec init

# 或非交互式，指定 AI 工具
openspec init --tools claude,cursor
```

#### 3. 配置项目上下文（可选但推荐）
```bash
# 编辑配置文件，添加项目上下文
# 参考上一节的配置模板
vim openspec/config.yaml
```

---

### 3.2 完整案例：为应用添加暗色模式

让我们通过一个完整案例，体验 OpenSpec 的工作流。

#### Phase 1: 启动变更
在 AI 编码助手的对话窗口中输入：
```
/opsx:propose add-dark-mode

我想为应用添加暗色模式功能，包括：
1. 在设置页面添加主题切换开关
2. 支持检测系统偏好（跟随系统）
3. 用户选择持久化到 localStorage
4. 所有页面即时切换，无需刷新
```

**AI 将创建**：
- `openspec/changes/add-dark-mode/proposal.md` — 提案文档
- `openspec/changes/add-dark-mode/specs/ui/spec.md` — Delta 规范
- `openspec/changes/add-dark-mode/design.md` — 设计文档
- `openspec/changes/add-dark-mode/tasks.md` — 任务清单

#### Phase 2: 审查产物（重要！）
在执行实现前，花几分钟审查 AI 生成的产物：

```bash
# 列出当前变更
openspec list

# 查看变更详情
openspec show add-dark-mode

# 或使用交互式仪表板
openspec view
```

**审查清单**：
- ☐ Proposal：意图和范围是否准确？
- ☐ Specs：场景是否覆盖了主要用例和边界情况？
- ☐ Design：技术方案是否合理？
- ☐ Tasks：任务拆分是否合理？粒度是否适中？

> **Pro Tip**：如果发现产物有问题，直接告诉 AI 修改即可，如：「请把 tasks.md 中的第 2 组任务拆分得更细一些」

#### Phase 3: 实现代码
```
/opsx:apply
```

AI 将按照 tasks.md 中的清单逐项实现：
```
✓ 1.1 创建 ThemeContext
✓ 1.2 添加 CSS 自定义属性
✓ 1.3 实现 localStorage 持久化
→ 2.1 创建 ThemeToggle 组件（进行中）
○ 2.2 添加到设置页面
○ 3.1 定义暗色调色板
```

> 💡 **可以随时暂停**
> 实现过程中如果需要暂停（下班、开会等），直接停止即可。下次继续时，AI 会从未完成的任务继续执行。

#### Phase 4: 验证实现（推荐）
```
/opsx:verify
```

AI 将检查实现是否与产物一致：
- **Completeness**：所有任务是否完成？所有需求是否实现？
- **Correctness**：实现是否符合规范意图？
- **Coherence**：代码是否反映了设计决策？

#### Phase 5: 归档变更
```
/opsx:archive
```

归档过程会：
1. 将 Delta 规范合并到 `openspec/specs/ui/spec.md`
2. 将变更文件夹移动到 `openspec/changes/archive/2025-xx-xx-add-dark-mode/`
3. 保留完整的产物作为审计轨迹

---

### 3.3 CLI 常用命令速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `openspec list` | 列出所有活动变更 | `openspec list --json` |
| `openspec show` | 查看变更/规范详情 | `openspec show add-dark-mode` |
| `openspec view` | 交互式仪表板 | `openspec view` |
| `openspec validate` | 验证产物格式 | `openspec validate --all` |
| `openspec status` | 查看产物完成状态 | `openspec status --change add-dark-mode` |
| `openspec archive` | 归档变更（CLI 方式） | `openspec archive add-dark-mode -y` |
| `openspec update` | 更新 AI 工具配置 | `openspec update` |
| `openspec config profile` | 配置工作流 profile | `openspec config profile core` |

---

## Part 4: 常见问题解答（FAQ）

> 实战中常见问题的解决方案

### Q: AI 生成的产物质量不高怎么办？

**解决方案**：

1. **完善项目配置**：在 `openspec/config.yaml` 中添加详细的项目上下文（技术栈、代码规范、架构约定等），AI 会参考这些信息
2. **添加产物规则**：为特定产物添加 rules，如要求 specs 必须使用 Given/When/Then 格式
3. **使用高质量模型**：OpenSpec 官方推荐使用 Claude Opus 4.5 或 GPT 5.2 等高推理能力模型
4. **提供更多上下文**：在 `/opsx:propose` 时提供更详细的描述

**示例：增强的提案描述**
```
/opsx:propose add-dark-mode

## 背景
- 用户调研显示 60% 用户希望有暗色模式
- 竞品 A 和 B 都已支持暗色模式

## 详细需求
1. 主题切换：设置页面添加 Toggle，支持「浅色/深色/跟随系统」三种选项
2. 即时切换：切换后所有页面立即生效，无需刷新
3. 持久化：使用 localStorage 存储，刷新后保持选择
4. 系统适配：首次访问时检测系统偏好

## 技术约束
- 使用 CSS Custom Properties 实现
- 使用 React Context 管理状态
- 不引入额外的 CSS-in-JS 库
```

---

### Q: AI 工具无法识别 `/opsx` 命令怎么办？

**可能原因及解决方案**：

1. **未初始化**：运行 `openspec init` 初始化项目
2. **配置过期**：升级 OpenSpec 后运行 `openspec update` 重新生成 AI 工具配置
3. **工具未选择**：检查初始化时是否选择了你使用的 AI 工具
4. **需要重启**：某些 AI 工具需要重启才能加载新的 skills/commands

**修复步骤**：
```bash
# 重新初始化，指定你的 AI 工具
openspec init --tools claude,cursor --force

# 或只更新配置
openspec update --force
```

---

### Q: 如何处理多个变更之间的冲突？

OpenSpec 支持并行变更，但当多个变更修改同一个规范时需要注意：

1. **使用 `/opsx:bulk-archive`**：它会自动检测规范冲突并按时间顺序合并
2. **先归档依赖变更**：如果变更 B 依赖变更 A 的结果，先归档 A
3. **手动解决**：如果冲突复杂，可以手动编辑 specs 文件后再归档

```
/opsx:bulk-archive

# AI 会检测冲突并提示：
# ⚠ add-dark-mode 和 update-theme-system 都修改 specs/ui/
# 将按创建时间顺序合并：add-dark-mode → update-theme-system
# 是否继续？
```

---

### Q: 如何在团队中推广 OpenSpec？

**推广策略**：

1. **从小处开始**：选择一个小功能作为试点，展示 OpenSpec 的价值
2. **统一配置**：将 `openspec/config.yaml` 提交到代码库，确保团队使用一致的配置
3. **建立规范模板**：创建团队专属的 Schema 和 templates，体现团队最佳实践
4. **结合 Code Review**：将产物审查纳入 CR 流程，提高规范质量

**团队配置建议**：
- 将 `openspec/` 目录纳入版本控制
- 在 `config.yaml` 中添加团队约定和代码规范
- 定期归档变更，保持 changes/ 目录整洁

---

### 其他常见问题

#### Q: OpenSpec 支持哪些 AI 工具？
OpenSpec 支持 20+ AI 编码助手，包括但不限于：Claude Code、Cursor、Windsurf、GitHub Copilot、Kiro、Cline、RooCode、Continue、Qoder、Gemini CLI、Amazon Q、Trae 等。完整列表请参考官方文档。

#### Q: 如何回滚或撤销一个已归档的变更？
OpenSpec 本身不提供回滚功能，但你可以：
1. **Git 回滚**：使用 `git revert` 回滚相关提交
2. **查看归档**：在 `openspec/changes/archive/` 中找到原变更的完整产物
3. **创建反向变更**：创建一个新变更，使用 REMOVED 来删除之前 ADDED 的内容

```
/opsx:propose revert-dark-mode

需要回滚暗色模式功能，原因是与第三方组件库存在兼容性问题。
参考归档：openspec/changes/archive/2025-01-24-add-dark-mode/
```

#### Q: 如何创建自定义 Schema？

**两种方式**：

1. **Fork 现有 Schema（推荐）**
```bash
# Fork 默认 Schema 进行自定义
openspec schema fork spec-driven my-workflow

# 编辑 schema.yaml 和 templates/
vim openspec/schemas/my-workflow/schema.yaml
```

2. **从零创建**
```bash
# 创建极简 Schema（只有 proposal + tasks）
openspec schema init rapid \
  --description "快速迭代工作流" \
  --artifacts "proposal,tasks" \
  --default
```

#### Q: OpenSpec 产物会占用太多磁盘空间吗？
不会。OpenSpec 产物都是轻量级 Markdown 文件：
- 一个完整变更通常只有 10-50KB
- 归档会保留完整产物，但仍然很小
- 可以定期清理不需要的历史归档

**磁盘管理建议**：
- 将 `openspec/` 纳入 Git，享受版本控制和压缩
- 可以将很久以前的归档移到外部存储
- 归档本质是审计轨迹，建议保留

---

## 总结

### 开始你的规范驱动开发之旅

OpenSpec 不仅仅是一个工具，它代表了一种全新的 AI 协作范式：**先对齐，再编码**。

#### 关键要点回顾

- **规范是契约**：定义系统「做什么」，而非「怎么做」
- **产物递进**：Proposal → Specs → Design → Tasks，逐步明确
- **Delta 机制**：增量描述变化，完美适配存量项目
- **可追溯**：完整的变更历史和审计轨迹
- **灵活工作流**：Core 快速路径 vs Expanded 精细控制

#### 下一步行动

1. 在一个小项目上尝试 OpenSpec
2. 完善你的 config.yaml 配置
3. 在团队中推广规范驱动开发

#### 更多资源

- [GitHub 仓库](https://github.com/Fission-AI/OpenSpec)
- [Discord 社区](#)
- [中文文档站](#)

---

> 📝 本文档基于 OpenSpec 官方英文文档翻译整理，内容会随官方版本迭代定期更新。如发现翻译错误或希望补充内容，欢迎通过 GitHub 提交 Issue 参与贡献。
