import json
from pyecharts import options as opts
from topo.funs import seekFile


def dealjson(data: str, index: int):
    f = seekFile.seekJson(data)
    topo_data = f["topo"][index]["describe"]

    nodes = []
    link = []
    for i in topo_data:
        a = str(int(i['LeoID']))
        nodes.append(opts.GraphNode(name=a))
        for j in i["neighbor"]:
            link.append({"source": a, "target": str(int(j["NbID"])), "LocalPort": int(j["LocalPort"]), "NbPort": int(j["NbPort"])})
    links = []
    for i in link:
        tmp = []
        tmp.append("image://static/svgs/3" + str(i["LocalPort"]) + "-20e3.svg")
        tmp.append("image://static/svgs/3" + str(i["NbPort"]) + "-20e3.svg")
        i["symbol"] = tmp
        del tmp
        ce = opts.GraphLink(source=i["source"], target=i["target"], symbol=i["symbol"])
        print(i["source"], i["target"], i["symbol"])
        links.append(ce)
    return nodes, links
