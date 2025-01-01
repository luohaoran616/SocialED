import subprocess
import sys
import os
 
def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        sys.exit(1)
 
def download_miniconda():
    # 定义下载链接
    miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
    print("正在下载 Miniconda...")
    run_command(f"wget {miniconda_url}")
 
def install_miniconda():
    print("正在安装 Miniconda...")
    run_command("bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda")
 
def initialize_conda():
    print("正在初始化 Conda...")
    run_command("source $HOME/miniconda/bin/activate")
    run_command("conda init")
 
def create_conda_env(env_name, python_version="3.8"):
    # 创建 Conda 环境
    print(f"正在创建 Conda 环境: {env_name}")
    run_command(f"conda create -n {env_name} python={python_version}")
 
def activate_conda_env(env_name):
    # 激活 Conda 环境
    print(f"正在激活 Conda 环境: {env_name}")
    run_command(f"conda activate {env_name}")
 
def install_packages(env_name, packages):
    # 在 Conda 环境中安装包
    print(f"正在安装包...")
    run_command(f"conda activate {env_name}")
    run_command(f"conda install {' '.join(packages)}")
 
def main():
    env_name = "env"
    packages = ["numpy", "pandas", "scipy"]  # 
 
    download_miniconda()
    install_miniconda()
    initialize_conda()
    create_conda_env(env_name)
    activate_conda_env(env_name)
    install_packages(env_name, packages)
 
if __name__ == "__main__":
    main()