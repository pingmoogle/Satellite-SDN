# 天基网络SDN的可视化

Powered by Heroku

使用Heroku强力驱动：https://satellite-sdn.herokuapp.com/



## 文件结构层次

*文件夹加粗标识*

- **static** 存放静态文件，例如icon, js, css
- **templates**
  - **render** 用来生成拓扑图时的模板文件
      - layout.html 网站所有页面的基础模板，定义了导航栏、页脚等
      - terminal.html 用来生成一个tiny terminal，无具体功能
  - **topos** 已生成的拓扑图，作为模板，直接可用的网页
    - highevel.html 高空卫星网络拓扑图base
    - lowlevel.html 低空卫星网络拓扑图base
    - diy.html 自定义网络拓扑图base
  - login.html 用户登录页面
- **topo**
  - **funs** 存放用来生成拓扑图，与数据库连接等功能的函数
- app.py 启动flask的python脚本
- Procfile 用来启动Heroku的配置文件
- requirements.txt 需要的pypi包



## Usage
### 环境准备

系统：

Windows 10 Professional Version 20H2 Build 19042.844

Ubuntu 20.04.2 LTS

开发工具：

JetBrains Pycharm 2020.3.2

Navicat Premium 15

数据库：

MongoDB Community Server Version 4.4.4

其他环境：

Python 3.9

pypi packages：pymongo, Flask, networkx, gunicorn



### 部署过程

#### 项目主体

1. 使用Windows，安装Python 3.9，PyCharm等工具

2. 使用pip工具安装requiremens.txt 内的包：

   ```
   pip install -r requirements.txt
   ```

   或者：

   ```
   pip install flask networkx pymongo
   ```

   如果使用Linux 系统，可选安装gunicorn

   ```
   pip install gunicorn
   ```

3. 创建工作区，复制代码，并使用Pycharm打开：

   ```
   git clone https://github.com/Soowin/Satellite-SDN.git
   ```

4. 项目导入Pycharm后，修改启动配置文件

   在Run/Debug Configruations设置中，添加新的启动配置文件。其中，Script Path指向app.py文件，Working Directory选择为项目文件夹，并选择Python解释器等

使用python时，也可以创建虚拟环境，在虚拟环境中安装requirements.txt中的包，将项目在虚拟环境中启动。

#### 数据库

使用Windows或Linux系统，安装MongoDB Server，并配置管理员登录授权，开放HTTP 27017端口。本项目使用的数据库结构如下：

```
数据库名称：topos
数据库用户：topousers1
数据库用户密码：1234567
用户角色：readWrite
```

在topos数据库中新建两个集合jsonfiles和users

```
集合名：jsonfiles
文档类型：
	_id: 自动生成的文档ID
	fileName: 文件名
	fileVersion: 文件版本
	fileRaw: 文件数据
```

在jsonfiles集合中，json文件的文件数据以Document类型保存，其他文件类型以String类型保存。

jsonfiles中应该默认保存两个json文件：topo.json和topo66.json，分别对应高空网络与低空网络拓扑图结构文件。

```
集合名：users
文档类型：
	_id: 自动生成的文档ID
	userName: 用户名，应该保持为小写
	userPassword: 用户密码，以SHA256形式保存
	isActive: 用户是否已激活
	isAdmin：用户是否为管理员
```

### Web服务

使用Flask自带的服务器可作为开发和测试环境使用，在生产环境中，需要替换为性能更高的WSGI服务器。

在Linux系统，使用gunicorn：

```
pip install gunicorn
gunicorn app:app 
```

在服务器上，还可以使用nginx作为反向代理，将来自外部的请求转发到gunicorn上。



## Contributers

- Soowin
- zdkk
- Rorsachach



## LICENSE
Distributed under the MIT License. See `LICENSE` for more information.