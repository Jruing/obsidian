#!/usr/bin/env python3
"""
MkDocs Nav Sync - 自动同步文档目录结构与导航配置

功能：
- 扫描 docs 目录，按层级生成导航
- 排除隐藏目录和指定目录
- readme.md 优先排序
- 支持 index.md 索引页
- 增量合并现有导航
"""

import argparse
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Union

# 尝试导入 yaml，如果没有则提示安装
try:
    import yaml
except ImportError:
    print("错误: 需要安装 PyYAML 库")
    print("请运行: pip install pyyaml")
    sys.exit(1)


# 默认排除的目录
DEFAULT_EXCLUDE = {'.obsidian', '.git', '.github', '.vscode', '__pycache__', 'node_modules'}


def is_hidden(path: Path) -> bool:
    """检查路径是否为隐藏文件/目录"""
    parts = path.parts
    return any(part.startswith('.') for part in parts)


def get_display_name(name: str) -> str:
    """
    获取显示名称
    - 去掉 .md 后缀
    - 处理特殊文件名
    """
    if name.lower() == 'readme.md':
        return '简介'
    if name.lower() == 'index.md':
        return '概览'
    # 去掉 .md 后缀
    return name[:-3] if name.lower().endswith('.md') else name


def scan_docs_directory(
    docs_dir: Path,
    exclude_dirs: Set[str]
) -> Dict[str, Union[str, Dict]]:
    """
    扫描 docs 目录，返回导航树结构
    
    返回结构示例:
    {
        'readme.md': 'readme.md',  # 顶层文件
        '开发': {  # 目录
            '前端': {
                'React-安装.md': '开发/前端/React-安装.md'
            }
        }
    }
    """
    nav_tree: Dict[str, Union[str, Dict]] = OrderedDict()
    
    def scan_recursive(current_dir: Path, tree: Dict, relative_path: str = ""):
        items = []
        
        try:
            for item in current_dir.iterdir():
                items.append(item)
        except PermissionError:
            return
        
        # 分离文件和目录
        files = []
        dirs = []
        
        for item in items:
            # 排除隐藏目录和指定排除目录
            if item.name.startswith('.'):
                continue
            if item.name in exclude_dirs or item.name in DEFAULT_EXCLUDE:
                continue
            
            if item.is_file() and item.suffix.lower() == '.md':
                files.append(item)
            elif item.is_dir():
                dirs.append(item)
        
        # 排序：readme.md 最前，其他按字母排序
        files.sort(key=lambda x: (0 if x.name.lower() == 'readme.md' else 1, x.name.lower()))
        dirs.sort(key=lambda x: x.name.lower())
        
        # 处理文件
        for file_item in files:
            display_name = get_display_name(file_item.name)
            file_relative_path = f"{relative_path}/{file_item.name}" if relative_path else file_item.name
            tree[display_name] = file_relative_path
        
        # 处理目录
        for dir_item in dirs:
            dir_name = dir_item.name
            dir_relative_path = f"{relative_path}/{dir_name}" if relative_path else dir_name
            
            # 检查是否有 index.md
            index_file = dir_item / 'index.md'
            
            sub_tree: Dict[str, Union[str, Dict]] = OrderedDict()
            scan_recursive(dir_item, sub_tree, dir_relative_path)
            
            if sub_tree:  # 只有当目录不为空时才添加
                tree[dir_name] = sub_tree
    
    scan_recursive(docs_dir, nav_tree)
    return nav_tree


def nav_tree_to_yaml(nav_tree: Dict) -> List:
    """
    将导航树转换为 YAML nav 格式
    
    输入:
    {
        'readme.md': 'readme.md',
        '开发': {
            'React-安装.md': '开发/React-安装.md'
        }
    }
    
    输出:
    [
        {'简介': 'readme.md'},
        {'开发': [
            {'React-安装': '开发/React-安装.md'}
        ]}
    ]
    """
    result = []
    
    for key, value in nav_tree.items():
        if isinstance(value, dict):
            # 是目录
            sub_nav = nav_tree_to_yaml(value)
            if sub_nav:
                result.append({key: sub_nav})
        elif isinstance(value, str):
            # 是文件
            result.append({key: value})
    
    return result


def read_mkdocs_config(config_path: Path) -> Dict:
    """读取 mkdocs.yml 配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def write_mkdocs_config(config_path: Path, config: Dict):
    """写入 mkdocs.yml 配置文件"""
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def merge_nav(
    existing_nav: Optional[List],
    new_nav: List
) -> List:
    """
    合并现有导航和新生成的导航
    
    策略：
    - 新导航完全替换现有导航
    - 但保留手动添加的特殊项（如果需要的话）
    
    目前采用完全替换策略
    """
    return new_nav


def find_nav_section(content: str) -> Tuple[int, int]:
    """
    在 YAML 文件中找到 nav 部分的起始和结束位置
    返回 (start_line, end_line)，如果没找到返回 (-1, -1)
    """
    lines = content.split('\n')
    nav_start = -1
    nav_end = -1
    in_nav = False
    indent_level = 0
    
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        
        if stripped.startswith('nav:'):
            nav_start = i
            in_nav = True
            indent_level = len(line) - len(stripped)
            continue
        
        if in_nav:
            # 检查是否还在 nav 部分
            if stripped and not stripped.startswith('#'):
                current_indent = len(line) - len(stripped)
                # 如果缩进回到 nav 级别或更低，说明 nav 部分结束了
                if current_indent <= indent_level and not stripped.startswith('-'):
                    nav_end = i
                    break
            elif i == len(lines) - 1:
                nav_end = i + 1
                break
    
    return nav_start, nav_end


def format_nav_yaml(nav: List, indent: int = 2) -> str:
    """将导航列表格式化为 YAML 字符串"""
    lines = ['nav:']
    
    def format_item(item: Union[Dict, str], level: int = 0):
        prefix = '  ' * (level + 1)
        
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, list):
                    lines.append(f'{prefix}- {key}:')
                    for sub_item in value:
                        format_item(sub_item, level + 1)
                else:
                    lines.append(f'{prefix}- {key}: {value}')
        elif isinstance(item, str):
            lines.append(f'{prefix}- {item}')
    
    for item in nav:
        format_item(item)
    
    return '\n'.join(lines)


def update_mkdocs_yml(config_path: Path, new_nav: List, dry_run: bool = False) -> bool:
    """
    更新 mkdocs.yml 文件
    
    直接替换 nav 部分，保持其他配置不变
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 nav 部分
    nav_start, nav_end = find_nav_section(content)
    
    # 生成新的 nav YAML
    new_nav_yaml = format_nav_yaml(new_nav)
    
    if nav_start >= 0:
        # 替换现有的 nav 部分
        lines = content.split('\n')
        new_content = '\n'.join(lines[:nav_start]) + '\n' + new_nav_yaml + '\n'
        if nav_end > 0 and nav_end < len(lines):
            new_content += '\n'.join(lines[nav_end:])
    else:
        # 在文件末尾添加 nav 部分
        new_content = content.rstrip() + '\n\n' + new_nav_yaml + '\n'
    
    if dry_run:
        print("\n=== 预览模式 ===")
        print("以下是将要写入的 nav 配置:\n")
        print(new_nav_yaml)
        print("\n=== 文件不会被修改 ===")
        return True
    
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ 已更新: {config_path}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='同步 MkDocs 文档目录与导航配置',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --docs-dir ./docs --config ./mkdocs.yml
  %(prog)s --docs-dir ./docs --config ./mkdocs.yml --dry-run
  %(prog)s --docs-dir ./docs --config ./mkdocs.yml --exclude ".obsidian,custom"
        """
    )
    
    parser.add_argument(
        '--docs-dir',
        required=True,
        help='docs 目录路径'
    )
    parser.add_argument(
        '--config',
        required=True,
        help='mkdocs.yml 文件路径'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式，不修改文件'
    )
    parser.add_argument(
        '--exclude',
        default='',
        help='额外排除的目录，逗号分隔 (默认: .obsidian)'
    )
    
    args = parser.parse_args()
    
    docs_dir = Path(args.docs_dir).resolve()
    config_path = Path(args.config).resolve()
    
    # 验证路径
    if not docs_dir.exists():
        print(f"错误: docs 目录不存在: {docs_dir}")
        sys.exit(1)
    
    if not docs_dir.is_dir():
        print(f"错误: {docs_dir} 不是目录")
        sys.exit(1)
    
    if not config_path.exists():
        print(f"错误: 配置文件不存在: {config_path}")
        sys.exit(1)
    
    # 解析排除目录
    exclude_dirs = DEFAULT_EXCLUDE.copy()
    if args.exclude:
        exclude_dirs.update(x.strip() for x in args.exclude.split(',') if x.strip())
    
    print(f"扫描目录: {docs_dir}")
    print(f"配置文件: {config_path}")
    print(f"排除目录: {', '.join(sorted(exclude_dirs))}")
    
    # 扫描目录
    nav_tree = scan_docs_directory(docs_dir, exclude_dirs)
    
    if not nav_tree:
        print("警告: 没有找到任何 .md 文件")
        sys.exit(0)
    
    # 转换为 YAML 格式
    new_nav = nav_tree_to_yaml(nav_tree)
    
    # 更新配置文件
    update_mkdocs_yml(config_path, new_nav, args.dry_run)


if __name__ == '__main__':
    main()
