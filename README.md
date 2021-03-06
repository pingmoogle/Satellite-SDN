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
  - 

## Usage


## Contributers

- Soowin
- zdkk
- Rorsachach

## LICENSE
Distributed under the MIT License. See `LICENSE` for more information.