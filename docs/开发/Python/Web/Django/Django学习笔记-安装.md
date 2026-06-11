---
title: "Django 安装"
date: 2026-06-09
tags:
  - 开发
  - Python
  - Web
  - Django
  - 数据库迁移
  - 开发环境
---

## 安装
```
uv add django
```
## 创建项目
```
django-admin startproject mysite mysite01
```
### 目录结构
```
   C:\django_admin_backend\
   ├───.gitignore
   ├───.python-version
   ├───main.py
   ├───pyproject.toml
   ├───README.md
   ├───uv.lock
   ├───.git\...
   ├───.venv\...
   └───mysite01\
       ├───db.sqlite3
       ├───manage.py
       └───mysite\
           ├───__pycache__\
           ├───__init__.py
           ├───asgi.py
           ├───settings.py
           ├───urls.py
           └───wsgi.py
```
## 创建数据库迁移文件（注意目录，必须在这个目录下运行）
```
(django_admin_backend) PS C:\workspace\django_admin_backend\mysite01> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
## 创建超级管理员（注意目录，必须在这个目录下运行）
```
(django_admin_backend) PS C:\workspace\django_admin_backend\mysite01> python .\manage.py createsuperuser
Username (leave blank to use 'jruing'): admin # 输入用户
Email address: admin@123.com = # 输入邮箱
Password: # 输入密码
Password (again): # 输入密码
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
## 启动项目
```
cd mysite01
# 启动项目
python manage.py runserver
```
## 访问
```
http://127.0.0.1:8000/admin/
```