from pyecharts import options as opts
from pyecharts.charts import Graph


if __name__ == '__main__':

    nodes = [
        {"name": "1", "symbolSize": 20},
        {"name": "2", "symbolSize": 20},
        {"name": "3", "symbolSize": 20}
    ]
    links = [
        {"source": "1", "target": "2", "symbol": ["triangle", "triangle"], "symbolSize": 20},
        {"source": "1", "target": "3"}
    ]

    c = (
        Graph()
            .add("", nodes, links, repulsion=800,)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .render("../../templates/topos/graph_base.html")
    )
