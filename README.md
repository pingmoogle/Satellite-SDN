# 天基网络SDN的可视化

Powered by Heroku

使用Heroku强力驱动：https://satellite-sdn.herokuapp.com/

## Contributers

- Soowin
- zdkk
- Rorsachach

## 文件结构层次

*文件夹加粗标识*

- **static** 存放静态文件，例如icon, js, css
- **templates**
  - **render** 用来生成拓扑图时的模板文件，将逐步弃用
  - **topos** 已生成的拓扑图，已包含模板的，直接可用的网页
    - highevel.html 高空卫星网络拓扑图base
    - lowlevel.html 低空卫星网络拓扑图base
    - surfacelevel.html 地面网络拓扑图base
  - about.html 关于页面，暂时不使用
  - contact.html 联系方式页面，暂时不使用
  - index.html 首页内容
  - layout.html 网站所有页面的基础模板，定义了导航栏、页脚等
  - terminal.html 用来生成一个tiny terminal
  - login.html 用户登录页面
- **topo**
  - **data** 存放json数据，已弃用
  - **funs** 存放用来生成拓扑图的python脚本
- app.py 启动flask的python脚本
- Procfile 用来启动Heroku的配置文件
- requirements.txt 需要的pypi包

## LICENSE
Distributed under the MIT License. See `LICENSE` for more information.