---
tags:
  - Linux
---
## 准备工作
```bash
apt install zsh git curl -y
```
## 设置默认终端
```
chsh -s /bin/zsh
```
## 安装oh-my-zsh
```
sh -c "$(curl -fsSL https://install.ohmyz.sh/)"
# 国内
sh -c "$(curl -fsSL https://gitee.com/pocmon/ohmyzsh/raw/master/tools/install.sh)"
```
## 安装插件
```
# 自动建议
git clone https://gh.xmly.dev/https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# 语法高亮
git clone https://gh.xmly.dev/https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
## 修改配置文件
```
# ./zshrc
ZSH_THEME="robbyrussell"
# 加入该行
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```
## 目录跳转
```
apt install zoxide -y
# ./zshrc 最后一行加入
eval "$(zoxide init zsh)"
# 激活并生效
source ~/.zshrc
# 用法
z 目录名称
```
## 自动解压缩
```
# 安装常用解压缩
apt install -y unzip unrar p7zip-full tar gzip bzip2 xz-utils
# ./zshrc 最后一行加入
extract() {
    if [ -z "$1" ]; then
        # 无参数时提示用法
        echo "用法: extract <压缩包文件名>"
        echo "支持格式: zip, rar, tar, tar.gz, tar.bz2, tar.xz, 7z, gz, bz2, xz 等"
        return 1
    fi

    local filename="$1"
    local dirname="${filename%.*}"  # 解压到同名目录（去掉后缀）

    # 创建目录并解压（避免文件散落）
    mkdir -p "$dirname" && cd "$dirname" || exit

    case "$filename" in
        *.tar.gz|*.tgz) tar xzf "../$filename" ;;
        *.tar.bz2|*.tbz2) tar xjf "../$filename" ;;
        *.tar.xz|*.txz) tar xJf "../$filename" ;;
        *.tar) tar xf "../$filename" ;;
        *.zip) unzip "../$filename" ;;
        *.rar) unrar x "../$filename" ;;
        *.7z) 7z x "../$filename" ;;
        *.gz) gunzip "../$filename" ;;
        *.bz2) bunzip2 "../$filename" ;;
        *.xz) unxz "../$filename" ;;
        *) echo "不支持的压缩格式: $filename" && cd .. && rm -rf "$dirname" ;;
    esac

    echo "解压完成 → 目录: $(pwd)"
}
# 激活并生效
source ~/.zshrc
# 用法
extract test.zip
```
## 查看文件大小
```
# ./zshrc 最后一行加入
fsize() {
    if [ -z "$1" ]; then
        # 无参数时查看当前目录各子目录大小
        du -h --max-depth=1 | sort -hr
    else
        # 有参数时查看指定路径大小
        du -h "$1" | sort -hr
    fi
}
# 激活并生效
source ~/.zshrc
# 用法
fsize /var/log
```
## 批量替换文本
```
# 批量替换
replace() {
    if [ $# -lt 3 ]; then
        echo "用法: replace <旧文本> <新文本> <路径/文件>"
        return 1
    fi
    # 递归替换（仅替换文本文件，避免二进制文件出错）
    find "$3" -type f -not -name "*.bin" -not -name "*.zip" -exec sed -i "s/$1/$2/g" {} \;
    echo "替换完成！"
}
```
## 查看端口占用
```
# 查看端口占用
ports() {
    if [ -z "$1" ]; then
        # 无参数时查看所有监听端口
        ss -tulpn | grep LISTEN
    else
        # 有参数时查看指定端口
        ss -tulpn | grep ":$1"
    fi
}
```
## 查看内存
```
mem() {
    free -h | awk '/Mem/ {print "总内存: " $2 "\n已用: " $3 "\n可用: " $4}'
}
```
## 备份文件/目录
```
backup() {
    if [ -z "$1" ]; then
        echo "用法: backup <文件/目录路径>"
        return 1
    fi
    local src="$1"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local dest="${src}_backup_${timestamp}"
    
    if [ -f "$src" ]; then
        cp -v "$src" "$dest"  # 备份文件
    elif [ -d "$src" ]; then
        tar -czvf "$dest.tar.gz" "$src"  # 备份目录（压缩）
    else
        echo "错误：$src 不存在！"
        return 1
    fi
    echo "备份完成 → $dest"
}
```
## 根据端口停止应用
```
killport() {
    if [ -z "$1" ]; then
        echo "用法: killport <端口号>"
        return 1
    fi
    local port="$1"
    # 查找端口对应的PID并杀死
    local pid=$(lsof -ti:"$port")
    if [ -z "$pid" ]; then
        echo "端口 $port 未被占用！"
        return 0
    fi
    kill -9 "$pid"
    echo "端口 $port 对应的进程($pid)已终止！"
}
## 用法
killport 8000
```
## 扫描端口占用
```
portscan() {
    local start=${1:-8000}
    local end=${2:-8010}
    echo "=== 端口扫描 ($start-$end) ==="
    for port in $(seq "$start" "$end"); do
        if lsof -ti:"$port" &> /dev/null; then
            local pid=$(lsof -ti:"$port")
            local cmd=$(ps -p "$pid" -o comm=)
            echo "❌ $port: 被 $cmd (PID:$pid) 占用"
        else
            echo "✅ $port: 可用"
        fi
    done
}
# 用法
portscan 8000 8200
```
## 根据PID找文件
```
pid2files() {
    if [ -z "$1" ]; then
        echo "用法: pid2files <PID>"
        echo "示例: pid2files 12345"
        return 1
    fi
    local pid="$1"
    # 检查PID是否存在
    if ! ps -p "$pid" > /dev/null 2>&1; then
        echo "错误：PID $pid 不存在！"
        return 1
    fi

    echo "=== PID $pid 核心信息 ==="
    # 1. 可执行文件路径
    local exe_path=$(readlink -f /proc/"$pid"/exe)
    echo "1. 可执行文件：$exe_path"
    # 2. 进程启动目录
    local cwd=$(readlink -f /proc/"$pid"/cwd)
    echo "2. 启动工作目录：$cwd"
    # 3. 进程命令行
    local cmd=$(cat /proc/"$pid"/cmdline | tr '\0' ' ' | sed 's/ $//')
    echo "3. 完整启动命令：$cmd"

    echo -e "\n=== PID $pid 打开的关键文件（前20行）==="
    # 4. 进程打开的所有文件（lsof 过滤关键类型）
    lsof -p "$pid" | grep -E "REG|DIR" | grep -v "mem" | head -20 | awk '{print $9}'
    # 5. 进程打开的网络端口（辅助定位服务）
    echo -e "\n=== PID $pid 占用的端口 ==="
    lsof -p "$pid" | grep -E "TCP|UDP" | awk '{print $8 " → " $9}'
}
```
## 卸载
```
uninstall_oh_my_zsh
```