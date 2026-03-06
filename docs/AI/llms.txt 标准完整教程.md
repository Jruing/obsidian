---
tags:
  - AI
---
为大语言模型提供网站信息的标准化文件格式

---

**官方网站：** https://llmstxt.org/

**GitHub：** https://github.com/AnswerDotAI/llms-txt

---

## 目录

- [什么是 llms.txt](#什么是-llmstxt)
- [为什么需要 llms.txt](#为什么需要-llmstxt)
- [核心概念](#核心概念)
- [文件格式规范](#文件格式规范)
- [完整示例](#完整示例)
- [实施指南](#实施指南)
- [最佳实践](#最佳实践)
- [工具和集成](#工具和集成)
- [与其他标准的关系](#与其他标准的关系)
- [常见问题](#常见问题)
- [快速检查清单](#快速检查清单)

---

## 什么是 llms.txt

### 定义

**llms.txt** 是一个放置在网站根目录的标准化 Markdown 文件（`/llms.txt`），用于帮助大语言模型（LLM）在推理时更好地使用网站信息。

### 核心目标

```
让 AI 更容易理解和使用你的网站内容
```

**主要用途：**

- 📚 提供网站/项目的简洁概述
- 🔗 指向详细文档的链接
- 📝 为 LLM 提供结构化、易读的信息
- 🎯 帮助 AI 快速定位关键内容

---

## 为什么需要 llms.txt

### 当前的问题

#### 1. 上下文窗口限制

```
❌ 问题：
大多数网站太大 → LLM 上下文窗口装不下 → AI 无法处理完整网站
```

**示例：**

- 一个中型文档网站：500+ 页面
- Claude 3.5 上下文窗口：200K tokens
- 完整网站内容：可能超过 1M tokens

#### 2. HTML 转换困难

```
复杂的 HTML
├─ 导航菜单
├─ 广告
├─ JavaScript
├─ CSS 样式
└─ 嵌套结构
    ↓
转换为纯文本
    ↓
❌ 困难且不精确
```

#### 3. 信息分散

对于 AI 来说：

- ❌ 需要爬取多个页面
- ❌ 需要理解网站结构
- ❌ 需要过滤无关内容
- ❌ 浪费时间和资源

### llms.txt 的解决方案

```
✅ 单一文件集中信息
✅ Markdown 格式（AI 和人类都易读）
✅ 结构化、可解析
✅ 指向详细内容的链接
✅ 可选的精简版本
```

---

## 核心概念

### 双文件策略

llms.txt 提案包含两个核心概念：

#### 1. `/llms.txt` 文件

**位置：** 网站根目录

**格式：** Markdown

**内容：** 概述 + 链接列表

```
https://example.com/llms.txt
```

#### 2. `.md` 版本的页面

**格式：** 在原始 URL 后添加 `.md`

**目的：** 提供纯 Markdown 版本的页面内容

```
原始页面：https://example.com/docs/guide.html
Markdown：https://example.com/docs/guide.html.md

无文件名：https://example.com/docs/
Markdown：https://example.com/docs/index.html.md
```

### 使用场景

llms.txt 特别适用于：

| 场景 | 说明 | 示例 |
|------|------|------|
| 🔧 开发工具文档 | API 文档、编程库指南 | FastHTML, React |
| 💼 企业网站 | 公司结构、产品说明 | 公司官网 |
| 📚 教育机构 | 课程信息、资源导航 | 大学网站 |
| 🛒 电商网站 | 产品信息、政策说明 | 在线商店 |
| 👤 个人网站 | 简历、作品集 | 个人博客 |
| ⚖️ 法律文档 | 法规解读、政策说明 | 政府网站 |

---

## 文件格式规范

### 基本结构

llms.txt 文件必须按以下**特定顺序**包含以下部分：

```markdown
# [必需] H1 标题：项目/网站名称

> [可选] 引用块：项目简短摘要

[可选] 详细说明段落
可以包含多个段落、列表等
但不能包含标题（H2 除外）

## [可选] 分类名称

- [链接标题](URL): 可选的链接说明
- [另一个链接](URL): 说明文字

## Optional（特殊分类）

- [次要信息链接](URL): 可在需要简短上下文时跳过
```

### 详细规范

#### 1. H1 标题（必需）

```markdown
# 项目名称
```

**要求：**

- ✅ 必须是第一行
- ✅ 只能有一个 H1
- ✅ 使用项目或网站的正式名称

#### 2. 引用块摘要（推荐）

```markdown
> 简短的项目描述，包含理解后续内容所需的关键信息
```

**要求：**

- ✅ 使用 `>` 引用块语法
- ✅ 保持简洁（1-3 句话）
- ✅ 包含最关键的背景信息

**示例：**

```markdown
# FastHTML

> FastHTML 是一个 Python 库，它将 Starlette、Uvicorn、HTMX
> 和 fastcore 的 FT "FastTags" 结合在一起，用于创建服务器渲染的
> 超媒体应用程序。
```

#### 3. 详细信息部分（可选）

```markdown
重要说明：
- 项目的特殊特性
- 注意事项
- 兼容性信息

可以包含：
- 段落
- 列表
- 代码块
- 但不能有 H2-H6 标题
```

#### 4. 文件列表分类（可选但推荐）

使用 **H2 标题** 创建不同的文件分类：

```markdown
## 文档 (Docs)

- [快速入门指南](https://example.com/quickstart.html.md): 5 分钟上手
- [API 参考](https://example.com/api.html.md): 完整 API 文档

## 教程 (Tutorials)

- [初学者教程](https://example.com/beginner.html.md): 从零开始
- [高级技巧](https://example.com/advanced.html.md): 深入了解

## 示例 (Examples)

- [Todo 应用](https://example.com/todo.py): 完整的 CRUD 示例

## Optional（可选内容）

- [完整规范](https://example.com/full-spec.html.md): 详细技术规范
```

#### 5. 链接格式

每个链接必须遵循以下格式：

```markdown
- [链接标题](URL): 可选的描述文字
```

**组成部分：**

- `[链接标题]` - 必需，简洁的标题
- `(URL)` - 必需，可以是内部或外部链接
- `: 描述文字` - 可选，简短说明链接内容

**示例：**

```markdown
✅ 正确：
- [快速入门](https://example.com/start.md): 10 分钟入门教程
- [API 文档](https://example.com/api.md)

❌ 错误：
- 快速入门：https://example.com/start.md （缺少 Markdown 链接格式）
- [快速入门] （缺少 URL）
```

#### 6. Optional 分类（特殊含义）

```markdown
## Optional

- [次要文档](https://example.com/secondary.md): 补充信息
- [详细规范](https://example.com/spec.md): 完整技术细节
```

**特殊用途：**

- ✅ 包含可跳过的次要信息
- ✅ 当需要更短的上下文时可以忽略
- ✅ 适合放置详细但非必需的内容

---

## 完整示例

### 示例 1：软件项目（FastHTML）

这是 FastHTML 项目的真实 llms.txt 文件（简化版）：

```markdown
# FastHTML

> FastHTML 是一个 Python 库，它将 Starlette、Uvicorn、HTMX
> 和 fastcore 的 FT "FastTags" 结合在一起，用于创建服务器渲染的
> 超媒体应用程序。

重要说明：
- 虽然它的 API 部分受到 FastAPI 的启发，但它**不兼容** FastAPI 语法，
  也不针对创建 API 服务
- FastHTML 兼容 JS 原生 Web 组件和任何原生 JS 库，但不兼容 React、
  Vue 或 Svelte

## Docs

- [FastHTML 快速入门](https://fastht.ml/docs/tutorials/quickstart_for_web_devs.html.md): FastHTML 功能的简要概述
- [HTMX 参考](https://github.com/bigskysoftware/htmx/blob/master/www/content/reference.md): HTMX 所有属性、CSS 类、标头、事件、扩展、JS 库方法和配置选项的简要描述

## Examples

- [Todo 列表应用](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py): 完整的 CRUD 应用详细演练，展示 FastHTML 和 HTMX 模式的惯用用法

## Optional

- [Starlette 完整文档](https://gist.githubusercontent.com/jph00/809e4a4808d4510be0e3dc9565e9cbd3/raw/9b717589ca44cedc8aaf00b2b8cacef922964c0f/starlette-sml.md): 对 FastHTML 开发有用的 Starlette 文档子集
```

**查看真实文件：** https://www.fastht.ml/docs/llms.txt

### 示例 2：电商网站

```markdown
# TechStore - 专业电子产品商城

> TechStore 是一家专注于高端电子产品的在线零售商，
> 提供笔记本电脑、手机、配件等产品，覆盖全国配送。

重要信息：
- 所有产品提供 30 天无理由退货
- 支持多种支付方式：支付宝、微信、信用卡
- 会员享受额外 5% 折扣

## 产品分类 (Products)

- [笔记本电脑](https://techstore.com/products/laptops.html.md): 包含规格、价格和评价
- [智能手机](https://techstore.com/products/phones.html.md): 最新款式和促销信息
- [配件](https://techstore.com/products/accessories.html.md): 充电器、保护壳等

## 购物指南 (Guides)

- [如何选购笔记本](https://techstore.com/guides/laptop-buying.html.md): 根据需求选择合适的笔记本
- [支付和配送](https://techstore.com/guides/payment-shipping.html.md): 支付方式和配送时间说明

## 客户服务 (Support)

- [退换货政策](https://techstore.com/support/returns.html.md): 详细的退换货流程
- [常见问题](https://techstore.com/support/faq.html.md): 最常见的 50 个问题解答

## Optional

- [公司历史](https://techstore.com/about/history.html.md): TechStore 的发展历程
- [技术博客](https://techstore.com/blog/index.html.md): 科技资讯和产品评测
```

### 示例 3：个人简历网站

```markdown
# 张伟 - 全栈开发工程师

> 拥有 8 年全栈开发经验的软件工程师，专注于 Web 应用开发、
> 云架构和团队领导。擅长 Python、JavaScript 和 AWS。

## 工作经历 (Experience)

- [完整简历](https://zhangwei.com/resume.html.md): 详细的工作经历和技能
- [项目作品集](https://zhangwei.com/portfolio.html.md): 代表性项目展示

## 技术博客 (Blog)

- [React 性能优化](https://zhangwei.com/blog/react-optimization.html.md): 实战经验分享
- [微服务架构实践](https://zhangwei.com/blog/microservices.html.md): 在生产环境中的应用

## 开源贡献 (Open Source)

- [GitHub 项目](https://github.com/zhangwei): 我的开源项目列表
- [技术演讲](https://zhangwei.com/talks.html.md): 在各种技术会议上的演讲

## Optional

- [个人爱好](https://zhangwei.com/hobbies.html.md): 摄影和登山
- [联系方式](https://zhangwei.com/contact.html.md): 如何联系我
```

### 示例 4：API 文档网站

```markdown
# PaymentAPI - 支付集成 API

> PaymentAPI 提供简单、安全的支付集成解决方案，支持信用卡、
> 借记卡和数字钱包。符合 PCI-DSS 标准。

关键特性：
- 多币种支持（150+ 种货币）
- 实时交易处理
- 强大的欺诈检测
- RESTful API 设计

## 快速开始 (Getting Started)

- [5 分钟集成指南](https://paymentapi.com/docs/quickstart.html.md): 最快的上手方式
- [认证和 API 密钥](https://paymentapi.com/docs/auth.html.md): 如何获取和使用 API 密钥

## API 参考 (API Reference)

- [支付端点](https://paymentapi.com/api/payments.html.md): 创建、查询和退款支付
- [客户管理](https://paymentapi.com/api/customers.html.md): 客户信息 CRUD 操作
- [Webhooks](https://paymentapi.com/api/webhooks.html.md): 接收实时事件通知

## SDK 和库 (SDKs)

- [Python SDK](https://paymentapi.com/sdks/python.html.md): Python 集成库
- [Node.js SDK](https://paymentapi.com/sdks/nodejs.html.md): Node.js 集成库
- [PHP SDK](https://paymentapi.com/sdks/php.html.md): PHP 集成库

## 示例代码 (Examples)

- [完整电商集成](https://github.com/paymentapi/examples/ecommerce): 端到端示例
- [订阅计费](https://github.com/paymentapi/examples/subscriptions): 定期付款示例

## Optional

- [错误代码完整列表](https://paymentapi.com/docs/errors.html.md): 所有可能的错误代码
- [API 变更日志](https://paymentapi.com/docs/changelog.html.md): 版本更新历史
- [测试卡号](https://paymentapi.com/docs/testing.html.md): 用于测试环境的卡号
```

---

## 实施指南

### 步骤 1：创建 llms.txt 文件

#### 方法 A：手动创建

- 在网站根目录创建 `llms.txt` 文件
- 按照规范编写内容
- 确保文件可通过 `https://yourdomain.com/llms.txt` 访问

#### 方法 B：使用构建工具

如果你使用静态网站生成器：

**Jekyll 示例：**

```yaml
# _config.yml
include:
  - llms.txt
```

**Hugo 示例：**

```toml
# config.toml
[outputs]
home = ["HTML", "RSS", "LLMSTXT"]
```

**Next.js 示例：**

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/llms.txt',
        destination: '/api/llms-txt',
      },
    ];
  },
};
```

### 步骤 2：创建 .md 版本的页面

#### 选项 A：手动维护

为重要页面创建 `.md` 版本：

```
docs/
├─ guide.html          # 原始 HTML 页面
├─ guide.html.md       # Markdown 版本
├─ api.html
└─ api.html.md
```

#### 选项 B：自动生成

**使用 nbdev（Python）：**

所有 nbdev 项目自动生成 `.md` 版本。

**自定义脚本示例：**

```python
# generate_md.py
from bs4 import BeautifulSoup
import html2text

def html_to_markdown(html_file):
    with open(html_file, 'r') as f:
        html = f.read()

    # 移除导航、广告等
    soup = BeautifulSoup(html, 'html.parser')
    main_content = soup.find('main') or soup.find('article')

    # 转换为 Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown = h.handle(str(main_content))

    # 保存为 .md 文件
    md_file = html_file + '.md'
    with open(md_file, 'w') as f:
        f.write(markdown)

# 使用
html_to_markdown('docs/guide.html')
```

### 步骤 3：测试 llms.txt

#### 验证清单

```
□ llms.txt 文件可访问
  → 访问 https://yourdomain.com/llms.txt

□ 格式正确
  → H1 标题存在
  → 链接格式正确
  → 没有语法错误

□ 链接有效
  → 所有链接可以访问
  → .md 文件存在且内容正确

□ 内容清晰
  → 摘要简洁明了
  → 链接描述准确
  → 组织结构合理

□ AI 测试
  → 在 ChatGPT/Claude 中测试
  → 询问关于你网站的问题
  → 验证 AI 能否找到信息
```

#### 实际测试方法

**方法 1：ChatGPT/Claude 测试**

```
提示词：
请阅读 https://yourdomain.com/llms.txt 文件，
然后回答：[你的网站]的主要功能是什么？

检查：
- AI 是否能正确读取文件
- 回答是否准确
- 是否遵循了链接
```

**方法 2：使用工具验证**

```bash
# 使用 llms_txt2ctx 工具
pip install llms-txt

# 生成上下文文件
llms_txt2ctx https://yourdomain.com/llms.txt

# 检查生成的文件
cat llms-ctx.txt
```

### 步骤 4：优化和维护

#### 定期更新

```
每月检查：
□ 链接是否仍然有效
□ 内容是否需要更新
□ 是否有新的重要页面需要添加

每季度审查：
□ 结构是否仍然合理
□ 是否需要重新组织分类
□ 用户反馈是否有改进建议
```

#### 内容策略

**包含什么：**

- ✅ 最重要的文档和指南
- ✅ 核心 API 参考
- ✅ 常见用例示例
- ✅ 快速入门资源

**不包含什么：**

- ❌ 过于详细的内部文档
- ❌ 频繁变化的内容（除非能自动更新）
- ❌ 营销材料（除非与理解产品直接相关）
- ❌ 个人博客文章（除非是重要教程）

---

## 最佳实践

### 1. 保持简洁

```markdown
❌ 不好：
> 我们的项目是一个革命性的、创新的、下一代的云原生
> 微服务架构框架，它利用最先进的人工智能和机器学习
> 技术，为企业提供前所未有的可扩展性和灵活性...

✅ 好：
> 云原生微服务框架，简化分布式应用开发。
> 支持多语言、自动扩展和内置监控。
```

### 2. 使用清晰的链接描述

```markdown
❌ 不好：
- [文档](https://example.com/docs.md)
- [这里](https://example.com/guide.md): 点击查看

✅ 好：
- [快速入门指南](https://example.com/quickstart.md): 10 分钟上手教程
- [API 参考手册](https://example.com/api.md): 完整的 API 端点文档
```

### 3. 避免行话和模糊术语

```markdown
❌ 不好：
> 本框架利用先进的范式和抽象层

✅ 好：
> 本框架使用组件化架构，简化代码组织
```

### 4. 合理组织分类

```markdown
✅ 推荐的分类名称：
- Docs / Documentation（文档）
- Tutorials（教程）
- Examples（示例）
- API Reference（API 参考）
- Guides（指南）
- Getting Started（入门）
- FAQ（常见问题）
- Optional（可选内容）

❌ 避免的分类：
- 模糊的名称（"其他"、"更多"）
- 过于具体的技术术语
- 内部代号或缩写
```

### 5. 链接到 Markdown 版本

```markdown
✅ 好：
- [用户指南](https://example.com/guide.html.md)

⚠️ 可接受（如果没有 .md 版本）：
- [用户指南](https://example.com/guide.html)

❌ 不推荐：
- [用户指南](https://example.com/guide.pdf)（PDF 难以解析）
```

### 6. 提供上下文

```markdown
❌ 不够：
- [教程](https://example.com/tutorial.md)

✅ 好：
- [React 初学者教程](https://example.com/tutorial.md): 使用 Hooks 构建 Todo 应用，适合有基本 JavaScript 知识的开发者
```

### 7. 使用 Optional 分类

```markdown
## Optional

- [完整 API 规范](https://example.com/full-spec.md): 2000+ 页详细文档，仅在需要时参考
- [历史版本](https://example.com/legacy.md): v1.x 的文档，用于维护旧项目
- [设计决策](https://example.com/decisions.md): 架构设计背后的思考过程
```

### 8. 测试 AI 理解

定期测试：

```
测试场景：

1. 让 AI 总结你的项目
   提示：阅读 llms.txt 并用一段话总结这个项目

2. 让 AI 回答具体问题
   提示：如何使用 X 功能？需要哪些步骤？

3. 让 AI 找到特定信息
   提示：在哪里可以找到关于 Y 的文档？

评估标准：
✅ AI 能找到正确信息
✅ 回答准确且完整
✅ 能够遵循链接获取详细信息

❌ 回答模糊或错误
❌ 无法找到关键信息
```

---

## 工具和集成

### 官方和社区工具

#### 1. llms_txt2ctx（Python CLI）

**功能：** 将 llms.txt 展开为 LLM 上下文文件

**安装：**

```bash
pip install llms-txt
```

**使用：**

```bash
# 基本用法
llms_txt2ctx https://example.com/llms.txt

# 生成两个文件：
# - llms-ctx.txt（不包含 Optional 链接）
# - llms-ctx-full.txt（包含 Optional 链接）

# 自定义输出
llms_txt2ctx https://example.com/llms.txt --output my-context.txt

# 仅生成简洁版
llms_txt2ctx https://example.com/llms.txt --skip-optional
```

**输出示例：**

生成的文件使用 XML 风格的结构，适合 Claude 等 LLM：

```xml
<doc title="项目名称">
  <summary>项目简短摘要</summary>
  <section title="快速入门">
    [快速入门指南的完整 Markdown 内容]
  </section>
  <section title="API 参考">
    [API 参考的完整 Markdown 内容]
  </section>
</doc>
```

#### 2. llmstxt-js（JavaScript）

**功能：** JavaScript 实现的 llms.txt 解析器

**安装：**

```bash
npm install llmstxt
```

**使用：**

```javascript
import { parseLLMsTxt } from 'llmstxt';

// 解析 llms.txt
const llmsTxt = await fetch('https://example.com/llms.txt').then((r) => r.text());
const parsed = parseLLMsTxt(llmsTxt);

console.log(parsed.title);       // "项目名称"
console.log(parsed.description); // "简短摘要"
console.log(parsed.sections);    // 分类数组

// 获取所有链接
parsed.sections.forEach((section) => {
  console.log(section.name);  // 分类名称
  section.links.forEach((link) => {
    console.log(link.title, link.url, link.description);
  });
});
```

**官方文档：** https://llmstxt.org/llmstxt-js.html

#### 3. VitePress Plugin

**功能：** 自动为 VitePress 网站生成 llms.txt

**安装：**

```bash
npm install vitepress-plugin-llms
```

**配置：**

```javascript
// .vitepress/config.js
import { defineConfig } from 'vitepress';
import { llmsPlugin } from 'vitepress-plugin-llms';

export default defineConfig({
  // ... 其他配置
  vite: {
    plugins: [
      llmsPlugin({
        title: '项目名称',
        description: '项目简短描述',
        sections: [
          {
            name: 'Docs',
            pattern: '/docs/**/*.md',
          },
          {
            name: 'API',
            pattern: '/api/**/*.md',
          },
        ],
      }),
    ],
  },
});
```

#### 4. Docusaurus Plugin

**功能：** 为 Docusaurus 网站生成 llms.txt

**安装：**

```bash
npm install docusaurus-plugin-llms
```

**配置：**

```javascript
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      'docusaurus-plugin-llms',
      {
        title: '项目名称',
        description: '项目描述',
        sections: {
          'Getting Started': ['/docs/intro', '/docs/installation'],
          'API Reference': ['/api/overview', '/api/endpoints'],
          Optional: ['/docs/advanced'],
        },
      },
    ],
  ],
};
```

#### 5. Drupal LLM Support

**功能：** Drupal 10.3+ 的完整 llms.txt 支持

**安装：**

```bash
composer require drupal/llm_support
drush en llm_support
```

**特性：**

- 自动生成 llms.txt
- 为内容类型生成 .md 版本
- 可配置的内容选择
- 集成到 Drupal 管理界面

**官方页面：** https://www.drupal.org/project/llm_support

---

## 与其他标准的关系

### llms.txt vs robots.txt

| 特性 | robots.txt | llms.txt |
|------|------------|----------|
| 目的 | 控制爬虫访问权限 | 提供 LLM 友好的内容概览 |
| 使用时机 | 索引时（训练前） | 推理时（用户查询时） |
| 内容 | 允许/禁止规则 | 内容摘要和链接 |
| 目标用户 | 搜索引擎爬虫 | LLM 和 AI 助手 |
| 关系 | 互补，可共存 | 提供爬取内容的上下文 |

**示例：共同使用**

```
网站根目录/
├─ robots.txt      # 控制哪些内容可以被爬取
├─ llms.txt        # 说明如何理解已爬取的内容
├─ sitemap.xml     # 列出所有可索引页面
└─ ...
```

### llms.txt vs sitemap.xml

| 特性 | sitemap.xml | llms.txt |
|------|-------------|----------|
| 格式 | XML | Markdown |
| 内容 | 所有可索引页面的完整列表 | 精选的重要页面 |
| 目的 | 帮助搜索引擎发现页面 | 帮助 LLM 理解网站 |
| 范围 | 可能数千个 URL | 精选的 10-50 个关键 URL |
| 外部链接 | ❌ 不包含 | ✅ 可以包含 |
| 上下文信息 | ❌ 无 | ✅ 提供描述和组织 |

**关键区别：**

```xml
<!-- sitemap.xml：列出所有页面 -->
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/page1.html</loc></url>
  <url><loc>https://example.com/page2.html</loc></url>
  <url><loc>https://example.com/page3.html</loc></url>
  <!-- ... 可能有数千个 URL -->
</urlset>
```

```markdown
# llms.txt：精选关键页面，带描述

## Getting Started

- [快速入门](https://example.com/quickstart.md): 10 分钟上手
- [核心概念](https://example.com/concepts.md): 理解关键概念

## API Reference

- [REST API](https://example.com/api.md): 完整 API 端点文档
```

---

## 常见问题

### Q1: llms.txt 是否会被用于训练 AI？

**A:** 主要用于推理（inference），而非训练。

- 🎯 **主要用途：** 用户查询时帮助 AI 理解网站
- 🔮 **未来可能：** 如果广泛采用，可能用于训练
- ⚠️ **当前：** 主要在推理时使用

### Q2: 我的网站很小，还需要 llms.txt 吗？

**A:** 视情况而定。

**适合小网站的情况：**

- ✅ 个人简历/作品集
- ✅ API 文档（即使只有几个端点）
- ✅ 教程网站
- ✅ 产品文档

**可能不需要的情况：**

- ❌ 纯静态单页网站（所有内容都在首页）
- ❌ 图片/视频为主的网站（少量文字）
- ❌ 没有结构化信息的个人博客

### Q3: llms.txt 会影响 SEO 吗？

**A:** 不会负面影响，可能有轻微正面影响。

**SEO 影响：**

- ✅ 提供额外的结构化信息
- ✅ 清晰的网站地图对爬虫友好
- ⚠️ 不会直接提升排名
- ✅ 改善 AI 搜索结果（如 Perplexity）

### Q4: 必须为每个页面创建 .md 版本吗？

**A:** 不必须，但推荐为重要页面创建。

**优先级：**

- 🔴 **必需：** 核心文档、API 参考
- 🟡 **推荐：** 教程、指南、FAQ
- 🟢 **可选：** 博客文章、次要页面
- ⚪ **不需要：** 营销页面、关于页面

### Q5: llms.txt 应该多长？

**A:** 建议 50-200 行。

**参考标准：**

- 📏 **最小：** 只有标题和几个链接（~10 行）
- 📏 **理想：** 包含摘要、详细说明和分类链接（~50-100 行）
- 📏 **最大：** 避免超过 200-300 行（太长难以维护）

**示例：**

```
小型项目：  ~30 行
中型项目：  ~80 行
大型项目：  ~150 行
超大项目：  ~200 行（考虑拆分）
```

### Q6: 可以链接到外部网站吗？

**A:** 可以！这是 llms.txt 的一个优势。

```markdown
## 相关资源

- [Python 官方文档](https://docs.python.org/3/): 我们使用的编程语言
- [PostgreSQL 指南](https://postgresql.org/docs/): 数据库文档
- [HTMX 参考](https://htmx.org/reference/): 前端库文档
```

### Q7: 如何处理多语言网站？

**A:** 为每种语言创建单独的 llms.txt。

**方法 A：子域名**

```
https://en.example.com/llms.txt  # 英文
https://zh.example.com/llms.txt  # 中文
https://ja.example.com/llms.txt  # 日文
```

**方法 B：路径**

```
https://example.com/en/llms.txt
https://example.com/zh/llms.txt
https://example.com/ja/llms.txt
```

**方法 C：主文件 + 语言分类**

```markdown
# My Project

> Available in multiple languages

## English Documentation

- [Quick Start (EN)](https://example.com/en/start.md)
- [API Reference (EN)](https://example.com/en/api.md)

## 中文文档

- [快速入门](https://example.com/zh/start.md)
- [API 参考](https://example.com/zh/api.md)
```

### Q8: llms.txt 需要频繁更新吗？

**A:** 取决于网站更新频率。

**更新建议：**

```
每周更新：     频繁变化的 API 文档
每月更新：     活跃的开源项目
每季度更新：   稳定的产品文档
每年更新：     企业网站、个人网站
发布时更新：   大版本发布时
```

---

## 快速检查清单

### 实施检查清单

```
□ 创建 llms.txt 文件
  □ 包含 H1 标题
  □ 添加引用块摘要
  □ 组织合理的分类
  □ 添加链接和描述

□ 创建 .md 版本
  □ 为核心页面创建 .md 版本
  □ 确保格式正确
  □ 内容清晰易读

□ 测试
  □ 文件可访问（/llms.txt）
  □ 所有链接有效
  □ 在 AI 中测试
  □ 格式验证通过

□ 优化
  □ 简洁明了的描述
  □ 合理的信息组织
  □ 避免行话和模糊术语

□ 维护
  □ 设置更新计划
  □ 定期检查链接
  □ 根据反馈改进
```

---

## 延伸阅读

### 官方资源

- **官方网站：** https://llmstxt.org/
- **GitHub 仓库：** https://github.com/AnswerDotAI/llms-txt
- **Discord 社区：** https://discord.gg/aJPygMvPEN

### 相关标准

- **robots.txt：** https://www.robotstxt.org/
- **sitemap.xml：** https://www.sitemaps.org/
- **Schema.org：** https://schema.org/

### 示例实现

- **FastHTML：** https://www.fastht.ml/docs/llms.txt
- **fastcore：** https://fastcore.fast.ai/docments.html.md
- **nbdev：** https://nbdev.fast.ai/

---

## 总结

### 核心要点

- **llms.txt 的目的**
  - 帮助 LLM 在推理时理解网站
  - 提供结构化、易读的内容导航
  - 补充而非替代现有标准

- **实施要素**
  - `/llms.txt` 文件（概述 + 链接）
  - `.md` 版本的页面（详细内容）
  - 清晰的组织和描述

- **最佳实践**
  - 保持简洁明了
  - 使用清晰的链接描述
  - 合理组织分类
  - 定期测试和更新

- **价值**
  - 改善 AI 对网站的理解
  - 提升 AI 搜索结果质量
  - 帮助开发者快速集成
  - 未来可能的更广泛应用

### 记住

llms.txt 不是一个复杂的标准，而是一个简单、实用的约定。从最基础的版本开始，逐步完善，重点是帮助 AI 更好地理解和使用你的内容。

**开始你的 llms.txt 之旅吧！** 🚀

---

**文档信息**

- **版本：** 1.0
- **更新日期：** 2025-11-02
- **基于：** https://llmstxt.org/ 官方提案

**免责声明**

本教程基于 llms.txt 官方提案，仅供教育和参考。规范可能随时间演进，请参考官方网站获取最新信息。实施前请根据自己的具体需求进行调整。
