---
tags:
  - Traefik
  - 反向代理
---
## 路由匹配器

| 匹配器                       | 说明                 | 示例                                         |
| ------------------------- | ------------------ | ------------------------------------------ |
| Host(hostname)            | 匹配请求的 Host 头       | Host(example.com)                          |
| HostRegexp(pattern)       | 使用正则匹配 Host        | HostRegexp({subdomain:[a-z]+}.example.com) |
| Path(path)                | 精确匹配路径（区分大小写）      | Path(/admin)) → 只匹配 /admin                 |
| PathPrefix(prefix)        | 路径前缀匹配             | PathPrefix(/api)) → 匹配 /api, /api/v1/users |
| Method(method)            | 匹配 HTTP 方法         | Method(GET), Method(POST, PUT)             |
| Header(name, value)       | 匹配请求头（精确）          | Header(Content-Type, application/json)     |
| HeaderRegexp(name, regex) | 请求头正则匹配            | HeaderRegexp(User-Agent, Chrome/.+)        |
| Query(key, value)         | 匹配查询参数（精确）         | Query(token, abc123)                       |
| ClientIP(ip)              | 匹配客户端 IP（需启用真实 IP） | ClientIP(192.168.1.0/24)                   |


