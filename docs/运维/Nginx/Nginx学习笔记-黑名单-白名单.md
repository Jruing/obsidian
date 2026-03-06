---
tags:
  - Nginx
  - 反向代理
---

> 通过在nginx配置文件中加入指令或者配置文件来实现黑名单/白名单策略，它的作用域有`http`,`server`和`location`

## 常用黑名单/白名单指令
> 以下指令为黑名单/白名单指令，可以配合使用

```
# 不允许1.1.1.1访问
deny 1.1.1.1;
# 仅允许1.1.1.1访问
allow 1.1.1.1;
# 允许所有人访问
allow all;
# 禁止所有人访问
deny all;
#屏蔽整个段即从1.0.0.1到1.255.255.254访问的命令
deny 123.0.0.0/8
#屏蔽IP段即从1.2.0.1到1.2.255.254访问的命令
deny 1.2.0.0/16
#屏蔽IP段即从1.2.3.1到1.2.3.254访问的命令
deny 1.2.3.0/24
```
> 通过指令配置
```nginx

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
			allow 1.1.1.1 # 仅允许1.1.1.1访问根路径下的资源
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
        allow 1.1.1.1 # 仅允许1.1.1.1访问这个server块下的资源
    }
	allow 1.1.1.1 # 仅允许1.1.1.1访问这个http块下的资源
}

```

## 文件黑名单/白名单
> 通过文件导入的方式实现黑白名单，以`ip.black`文件为例，写入以下内容

```
allow 1.1.1.1;
allow 2.2.2.2;
```
> 文件类型的黑名单/白名单用法
### 导入
```nginx

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
	include       ip.black # 通过文件导入的方式实现黑白名单
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}

```

