---
name: mkdocs-nav-sync
description: 自动扫描 MkDocs 项目的 docs/ 目录，生成或更新 mkdocs.yml 中的 nav 导航配置。当用户需要同步文档结构与导航配置、批量更新导航、或初始化新项目的导航时使用此 skill。支持按目录层级生成导航、排除隐藏目录、readme 优先排序、index.md 索引页等功能。
---

# MkDocs Nav Sync

自动同步 MkDocs 文档目录结构与 `mkdocs.yml` 导航配置。

## 快速开始

```bash
uv run python scripts/sync_nav.py --docs-dir <docs路径> --config <mkdocs.yml路径>
```

**示例：**

```bash
# 基本用法
uv run python scripts/sync_nav.py --docs-dir ./docs --config ./mkdocs.yml

# 预览模式（不实际修改文件）
uv run python scripts/sync_nav.py --docs-dir ./docs --config ./mkdocs.yml --dry-run

# 指定排除目录
uv run python scripts/sync_nav.py --docs-dir ./docs --config ./mkdocs.yml --exclude ".obsidian,.git"
```

## 功能特性

- **按目录层级生成导航**：根据 docs/ 目录结构自动生成嵌套导航
- **排除隐藏目录**：自动排除 `.obsidian`、`.git` 等隐藏目录
- **readme 优先**：将 `readme.md` 放在导航最前面
- **支持索引页**：识别 `index.md` 作为目录索引页
- **增量合并**：保留手动添加的自定义导航项
- **字母排序**：按文件名/目录名字母顺序排序

## 参数说明

| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `--docs-dir` | 是 | - | docs 目录路径 |
| `--config` | 是 | - | mkdocs.yml 文件路径 |
| `--dry-run` | 否 | false | 预览模式，不修改文件 |
| `--exclude` | 否 | `.obsidian` | 额外排除的目录（逗号分隔） |

## 导航生成规则

1. **目录层级**：每个子目录生成一个导航分组
2. **显示名称**：使用目录名/文件名（去掉 `.md` 后缀）
3. **文件路径**：相对于 docs 目录的路径
4. **排序规则**：
   - `readme.md` 始终在最前
   - 其他文件按字母顺序排序
5. **索引页**：如果目录包含 `index.md`，使用 `navigation.indexes` 特性

## 工作流程

1. 扫描 docs 目录，收集所有 `.md` 文件
2. 排除隐藏目录和指定排除的目录
3. 按目录层级构建导航树结构
4. 读取现有 mkdocs.yml，保留非自动生成的导航项
5. 合并新旧导航，生成最终配置
6. 写入 mkdocs.yml（dry-run 模式仅预览）
