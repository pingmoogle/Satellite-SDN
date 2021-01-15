from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.globals import CurrentConfig
from topo.funs import dealJSON


def newgraph(filename="topo66.json", timeSlice: int = 0):
    nodes, links = dealJSON.dealjson(filename, timeSlice)
    CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("templates"))
    c = (
        Graph(init_opts={
            "chart_id": "graph1"
        }).add("", nodes, links, repulsion=500, gravity=0.1, symbol_size=50
                 , symbol="image://static/svgs/orange.svg")
        .set_global_opts(title_opts=opts.TitleOpts(title="Satellite-sdn topo"))
        .render("templates/topos/graph_page.html",  # 目标文件
                    template_name="render/simple_chart.html")  # 模板
    )


if __name__ == '__main__':
    pass
