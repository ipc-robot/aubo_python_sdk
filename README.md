# AUBO Python SDK 安装指南 
```
git clone https://github.com/ipc-robot/aubo_python_sdk.git
```
Python SDK 安装之前需要确保 ROS Noetic 正确安装：<https://github.com/MIOS9/aubo_robot>

## setup 1. 安装 anaconda
### 1.1 下载 anaconda  
Anaconda下载地址(清华镜像)：<https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/> 
### 1.2 安装 anaconda  
```
bash Anaconda3-2024.06-1-Linux-x86_64.sh
```
* 进入注册信息页面，输入yes   
* 然后一直按回车，直到再次出现输入框，然后输入yes。  
* 确认好anaconda3的安装路径后，回车安装。  
**安装完成后，收到加入环境变量的提示信息，输入no**  
### 1.3 设置手动激活conda的工作空间  
```
sudo gedit ~/.bashrc
```  
在文件最后添加  
```
alias setconda='. ~/anaconda3/bin/activate'
```
这样，终端默认使用ROS的python路径，在需要时可以通过`setconda`来进入conda工作空间。

## setup 2. 配置 libpyaubo
### 2.1 创建一个conda环境，python版本为3.11。
```
setconda
conda create -n pyaubo python=3.11
```
### 2.2 将python依赖库复制到相应的环境中
```
cd ~/aubo_python_sdk
cp ~/aubo_python_sdk/dependants/* ~/anaconda3/envs/pyaubo/lib/python3.11/site-packages
conda activate pyaubo
```

### 2.3 测试SDK
```
python3 robotcontrol.py
```
