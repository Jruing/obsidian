---
title: CLIProxyAPI 配置文件详解
date: 2026-03-09
tags:
  - AI
  - CLI
  - 代理
---
参考文档：https://linux.do/t/topic/1011966
仓库地址： https://github.com/router-for-me/CLIProxyAPI 
## 配置文件详解
温馨提示：配置文件支持热重载，修改配置文件是即时生效的，不需要重启程序。
```
# 端口号，CLIProxyAPI运行了个HTTP服务器，需要端口号来进行访问
port: 8317

# 远程管理配置，配合EasyCLI或者WebUI来使用
remote-management:
  # 启用远程管理的开关，如果你部署在服务器上
  # 那么需要设置为true，才能使用EasyCLI或者WebUI连接到CLIProxyAPI进行管理
  # 如果只是本地使用API进行管理的，可以保持false不动
  allow-remote: false

  # 如果想使用EasyCLI或者WebUI通过API对CLIProxyAPI进行管理，必须设置Key
  # 如果不设置，视同关闭了API管理功能，就无法使用EasyCLI或者WebUI进行连接了
  # 如果你不需要使用EasyCLI或者WebUI进行管理，可以留空
  secret-key: ""

  # 是否集成WebUI的开关
  # 设置为false，可以通过http://YOUR_SERVER_IP:8317/management.html打开WebUI
  disable-control-panel: false

# 认证文件存放目录，用于存放Gemini CLI、Gemini Web、Qwen Code、Codex的认证文件
# 默认设置，是在你当前账户目录下的.cli-proxy-api文件夹，适配Windows和Linux环境
# 程序首次启动时会自动创建该文件夹
# Windows下默认为C:\Users\你的用户名\.cli-proxy-api
# Linux下默认为/home/你的用户名/.cli-proxy-api
# 如果在Windows环境下使用非默认位置，需要参照这样的格式修改填写"Z:\\CLIProxyAPI\\auths"
auth-dir: "~/.cli-proxy-api"

# 是否在日志中启用Debug信息，默认不启用，需要作者配合排错的时候打开就行
debug: false

# 是否将日志重定向到日志文件中
# 默认启用，日志会保存在程序目录下的logs文件夹中
# 如果关闭的话，会在控制台显示日志
logging-to-file: true

# 开关使用统计，默认启用
# 需要使用API来查看使用量，可以用EeasyCLI或者WebUI来查看
usage-statistics-enabled: true

# 如果你要使用代理，那么需要进行以下的设置，支持socks5/http/https协议
# 按照这样的格式"socks5://user:pass@192.168.1.1:1080/"填写
proxy-url: ""

# 当请求碰到403, 408, 500, 502, 503, 504这些错误码的时候，程序自动重试请求的次数
request-retry: 3

# 模型受到限制之后的处理行为
quota-exceeded:
  # 多账号轮询的核心配置
  # 设置为true时，例如一个账号触发了429，程序会自动切换到下一个账号重新发起请求
  # 设置为false时，程序会把429的错误信息发给客户端，结束当前请求
  # 也就是说，当设置为true时，只要轮询的账号里至少有一个号是正常的，客户端这里就不会报错
  # 而设置false时，则需要客户端来进行重试或中止操作
  switch-project: true 
  # Gemini CLI独占配置，适用于Gemini 2.5 Pro和Gemini 2.5 Flash模型
  # 当正式版配额用完之后，会自动切换到Preview模型，保持开启即可
  switch-preview-model: true

# 各种AI客户端访问CLIProxyAPI所需要填写的Key，就在这里设置，和后边的各种Key不要弄混淆了
# 通俗点讲，这里的Key是CLIProxyAPI作为服务器所需要设置的
# 后边的各种Key是CLIProxyAPI作为客户端去访问服务器所需要的
api-keys:
  - "your-api-key-1"
  - "your-api-key-2"

# Gemini的官方API Key，如果你已经配了Gemini CLI，那么不建议填
# 因为Gemini CLI是满血的，而官方Key是残血的，填了的话会一起参与轮询
generative-language-api-key:
  - "AIzaSy...01"
  - "AIzaSy...02"
  - "AIzaSy...03"
  - "AIzaSy...04"

# Codex的API Key，各种中转站提供的Codex的key和base-url参数，填在这里就可以接入了
codex-api-key:
  - api-key: "sk-atSM..."
    base-url: "https://www.example.com"

# Claude的API Key，使用官方Key的时候，不要填base-url，使用第三方中转的，填base-url
claude-api-key:
  - api-key: "sk-atSM..."
  - api-key: "sk-atSM..."
    base-url: "https://www.example.com"

# 各种OpenAI兼容的都可以在这里接入，不多解释了
openai-compatibility:
  - name: "openrouter"
    base-url: "https://openrouter.ai/api/v1"
    api-keys:
      - "sk-or-v1-...b780"
      - "sk-or-v1-...b781"
    models:
    	# OpenAI兼容供应商提供的模型名称
      - name: "moonshotai/kimi-k2:free"
      	# 模型别名
        alias: "kimi-k2"

# Gemini Web的相关设置，可以忽略掉，用默认值就行
gemini-web:
    # 此选项用于状态化会话，由于Gemini Web是逆向的
    # 因而如果设置false的话，每条发送的消息程序会携带之前的所有上下文发送给服务器
    # 设置true的话，程序会按客户端发送的报文，根据最长匹配寻找之前的会话
    # 如果已有会话，则只发送当前的消息，而不携带所有上下文
    # 如果使用Nano Banana模型，请务必保持此选项为true，否则无法进行连续会话修图
    # 如果还有不理解的，可以开始切换开关后，在Gemini Web官方网页查看效果
    context: true
    # 最大发送的字符，保持为默认值即可
    max-chars-per-request: 1000000
    # 程序默认超出最大字符，会进行截断，分批发送，截断时，会在报文最后附加一条让模型等待的消息
    # 如果设置true，则不会在报文最后附加这条消息
    # 建议保持false即可，因为只有截断才会附加消息，非截断情况是不会附加的
    disable-continuation-hint: false
    # 编程模式，不用来进行编程，请不要启用，使用Nano Banana模型，请务必关闭
    # 设置ture，会有以下效果
    ## 使用系统自带的编码助手Gem进行对话
    ## 对话时如有思考内容，会把思考内容并入正文
    ## 在报文最后附加一条关于XML的消息
    code-mode: false
```

