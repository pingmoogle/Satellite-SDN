from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.globals import CurrentConfig


def newgraph():
    nodes = [
        {"name": "1", "symbolSize": 20},
        {"name": "2", "symbolSize": 20},
        {"name": "3", "symbolSize": 20}
    ]
    links = [
        {"source": "1", "target": "2", "symbol": ["triangle", "triangle"], "symbolSize": 20},
        {"source": "1", "target": "3"}
    ]

    CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("templates"))
    c = (
        Graph(init_opts={
            "chart_id": "graph1",
            "width": "1108px"
        })
            .add("", nodes, links, repulsion=800)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .render("templates/topos/graph_page.html",
                    template_name="render/simple_chart.html")

    )


if __name__ == '__main__':
    pass
