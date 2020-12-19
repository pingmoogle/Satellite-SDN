import json
from pyecharts import options as opts
from topo.funs import seekFile


def dealjson(data: str):
    f = seekFile.seekJson(data)
    topo_data = f["topo"][0]["describe"]

    nodes = []
    link = []
    for i in topo_data:
        a = i['LeoID']
        nodes.append(opts.GraphNode(name=a))
        for j in i["neighbor"]:
            link.append({"source": a, "target": j["NbID"], "LocalPort": j["LocalPort"], "NbPort": j["NbPort"]})
    links = []
    for i in link:
        tmp = []
        tmp.append("image://static/svgs/3" + str(i["LocalPort"]) + "-20e3.svg")
        tmp.append("image://static/svgs/3" + str(i["NbPort"]) + "-20e3.svg")
        i["symbol"] = tmp
        del tmp
        links.append(opts.GraphLink(source=i["source"], target=i["target"], symbol=i["symbol"]))
    return nodes, links
