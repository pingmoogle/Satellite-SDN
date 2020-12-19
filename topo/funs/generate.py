from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.globals import CurrentConfig
from topo.funs import dealJSON

def newgraph():
    # TODO: json文件如何解析？

    str = "topo66.json"
    nodes, links = dealJSON.dealjson(str)
    CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("templates"))
    c = (
        Graph(init_opts={
            "chart_id": "graph1",
            "width": "1108px",
            "height": "800px"
        })
        .add("", nodes, links, repulsion=3000, gravity=0.6, symbol_size=50
             , symbol="image://static/svgs/orange.svg")
        .set_global_opts(title_opts=opts.TitleOpts(title="Satellite-sdn topo"))
        .render("templates/topos/graph_page.html",
                template_name="render/simple_chart.html")
    )


if __name__ == '__main__':
    pass
