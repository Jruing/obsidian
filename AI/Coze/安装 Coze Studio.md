## 部署并启动
```
git clone https://github.com/coze-dev/coze-studio.git
cd docker
cp .env.example .env
docker compose -f ./docker/docker-compose.yml up
```
## 注册
通过访问 `http://localhost:8888/sign`，输入你的用户名和密码，然后点击注册按钮来注册一个账号。
## 配置模型
在 `http://localhost:8888/admin/#model-management` 处配置模型，通过添加新模型。
## 访问服务
访问 Coze Studio，地址为 `http://localhost:8888/`。