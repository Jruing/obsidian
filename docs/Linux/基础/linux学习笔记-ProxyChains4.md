---
tags:
  - Linux
---
> ProxyChains4 是一款用于 Linux 系统的代理工具，能够通过 SOCKS 或 HTTP 代理加速网络访问，特别适用于国内服务器访问 GitHub 等国外网站时遇到的下载超时或速度慢的问题。
## 安装
```
sudo apt install proxychains4 -y
```
## 配置
```
sudo vi /etc/proxychains4.conf
[ProxyList]
# socks5 代理,修改以下内容，用户名和密码可为空
socks5 127.0.0.1 1080 用户名 密码
```
## 使用ProxyChains4
```
proxychains4 curl https://www.google.com.hk
```
## 全局终端代理
```
proxychains4 bash
```