---
tags:
  - Vibe-coding
  - AI
  - Agent
---
	## 准备工作
- IFlow CLI
## 安装skills-creator
```
# 激活iflow cli
ifow

# 进入交互式技能市场
/skills online

# 找到skills-creator回车
根据实际情况选择安装到全局或者项目

# 刷新
/skills refresh


# 安装其他skill安装到全局
iflow skill add [skill-id] --scope global
# 安装其他skill到项目
iflow skill add [skill-id] --scope project
```
## 创建一个数据库查询skills
```
基于 skills-creator 框架，设计一个专用于 MySQL 数据库查询的技能（Skill），该技能严格限定为只读操作，仅允许执行 SELECT 查询，禁止任何形式的数据修改（如INSERT、UPDATE、DELETE）或结构变更（如 ALTER、DROP 等）。
数据库连接参数（包括主机、端口、用户名、密码等）通过外部 .ini 配置文件管理，确保敏感信息与代码分离。可访问的数据库名称及允许查询的表范围由 models.py文件明确定义——该文件采用 Pydantic 模型格式，每个模型对应一张数据库表，并精确声明其字段名、类型及约束。所有查询请求（包括目标表、查询字段及过滤条件）必须严格遵循 models.py 中定义的模型结构：
1.仅允许查询已注册的表；
2.所有字段必须存在于对应模型中；
3.过滤条件的键和值需符合模型字段的语义与类型规范
```
## skills目录存放于`.iflow\skills`目录下
```
.iflow\skills\mysql-query-skill
	├── scripts\              # 脚本目录
	│   └── query.py          # 查询执行脚本
	├── .gitignore            # Git 忽略文件配置
	├── config.ini            # 数据库连接配置文件
	├── main.py               # 主技能脚本
	├── models.py             # Pydantic 模型定义
	├── query_builder.py      # 安全查询构建器
	├── README.md             # 使用指南
	├── requirements.txt      # Python 依赖
	├── SKILL.md              # 技能说明文档
	└── validator.py          # 查询验证器
```
## 修改部分文件
由于skills只能读取该目录下的文件，在cli中指定文件是无效的，所以需要手动修改`models.py`中的模型信息以及`config.ini`数据库配置信息
## IFlow查询使用
**input**
```
使用 mysql-query-skill 来查询用户表的数据条数
```
**output**
```
✦ 查询结果显示：
   - 数据总数 (total): 10 条
   - 当前返回 (count): 10 条
   - 查询的字段: id
   - 返回了 ID 从 1 到 10 的所有用户记录
```