# 天基网络SDN的可视化

Powered by Heroku

使用Heroku强力驱动：https://satellite-sdn.herokuapp.com/

Contributers:
- Soowin
- zdkk
- Rorsachach

## FHS

*文件夹加粗标识*

- **static** 存放静态文件，例如icon
- **templates**
  - **render** 用来生成拓扑图时的模板文件
  - **topos** 已生成的拓扑图，已包含模板的，直接可用的网页
  - about.html 关于页面，暂时不使用
  - contact.html 联系方式页面，暂时不使用
  - index.html 首页内容
  - layout.html 网站所有页面的基础模板，定义了导航栏、页脚等
- **topo**
  - **data** 存放json数据
  - **funs** 存放用来生成拓扑图的python脚本
- app.py 启动flask的python脚本
- Procfile 用来启动Heroku的配置文件
- requirements.txt 需要的pypi包

