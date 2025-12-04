---
tags:
  - Ubuntu
  - Linux
---
## Ubuntu系统配置
### 一键换源
```
bash <(curl -sSL https://linuxmirrors.cn/main.sh)
```
### 设置时区
```
timedatectl set-timezone Asia/Shanghai
```
### zsh终端美化
```
sh -c "$(curl -fsSL https://gitee.com/pocmon/ohmyzsh/raw/master/tools/install.sh)"

# 设置默认终端
chsh -s /bin/zsh

# 主题
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# 安装命令提示插件
git clone https://gitee.com/Jruing/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 安装命令语法校验
git clone https://gitee.com/Jruing/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# 编辑~/.zshrc
// 启用插件
plugins=(git zsh-autosuggestions zsh-syntax-highlighting z extract)
// 设置主题
ZSH_THEME="powerlevel10k/powerlevel10k"
```
## 开发环境
### uv python安装
```
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

### golang 环境安装
```

```