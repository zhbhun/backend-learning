- conda
- virtualenv

## conda

- [Conda使用指南](https://zhuanlan.zhihu.com/p/44398592)

### 环境管理

- 创建环境：`conda create --name py35 python=3.5`
- 激活环境：

    ```shell
    conda activate py35
    # 激活时系统做的事情就是把默认 2.7 环境从 PATH 中去除，再把 3.5 对应的命令加入 PATH
    ```

- 返回主环境：

    ```shell
    conda deactivate py35
    ```

- 删除环境：`conda remove --name py35 --all`
- 查看环境：`conda info -e`
- 更新 conda：`conda update conda`
- 更新 python：`conda update python`

    ps：假设当前环境是 python 3.5, conda 会将python升级为 3.5.x 系列的当前最新版本

### 包管理

- 安装库：`conda install numpy`
- 查看已经安装的库：`conda list`
- 搜索库的信息：`conda search numpy`
- 更新库：`conda update -n py35 numpy`
- 删除库：`conda remove -n py35 numpy`
- 安装库到指定的环境：`conda install -n py35 numpy`
- 查看某个环境的已安装包：`conda list -n py35`

### 设置镜像

- [Anaconda - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
