import networkx as nx

from topo.funs import seekFile


def json2jsseries(filename, timeSlice=0):
    """
    功能：把json里的数据格式化成echarts的js形式

    :param filename: 文件名（预设topo.json, topo66.json）
    :param timeSlice: 时间戳，topo.json会用到
    :return: 返回nodes的js形式[{"name": NodeName, "symbol": SymbolGraph}, ...]
    links的js形式：[{"source": nodeA, "target": nodeB, "symbol": [出口端口svg, 入口端口svg]}, ...]
    """

    f = seekFile.seekFile(filename)
    topo_data = f["topo"][timeSlice]["describe"]
    nodes = []
    link = []

    for i in topo_data:
        nodeDict = {}
        a = str(int(i['LeoID']))
        nodeDict["name"] = a
        # nodeDict["fixed"] = False
        nodeDict['symbol'] = "image://static/svgs/lowlevel.svg"
        nodes.append(nodeDict)
        for j in i["neighbor"]:
            link.append({"source": a, "target": str(int(j["NbID"])), "LocalPort": int(j["LocalPort"]),
                         "NbPort": int(j["NbPort"])})
    links = []
    for i in link:
        tmp = []
        tmp.append("image://static/svgs/3" + str(i["LocalPort"]) + "-20e3.svg")
        tmp.append("image://static/svgs/3" + str(i["NbPort"]) + "-20e3.svg")
        i["symbol"] = tmp
        ce = {"source": i["source"], "target": i["target"], "symbol": i["symbol"]}
        links.append(ce)
        del ce

    return nodes, links


def txt2jsseries(filename, timeSlice=0):
    f = seekFile.seekFile(filename)
    # f = open(filename, mode="r", encoding="utf-8")
    # file = f.readlines()
    file = f.strip().splitlines()

    node = {}
    link = []
    for i in file:
        line = i.split()
        node[line[0]] = line[0]
        link.append({"source": line[0], "target": line[1]})
    nodes = []
    for i in node:
        nodeDict = {"name": i}
        nodeDict['symbol'] = "image://static/svgs/lowlevel.svg"
        nodes.append(nodeDict)
    return nodes, link


def gml2jsseries(filename, timeSlice=0):
    fileRaw = seekFile.seekFile(filename)
    g = nx.parse_gml(fileRaw)
    nodesList = []
    nodes = []
    edges = []
    nodes_id = dict()
    # nodes_label = dict()
    for id, label in enumerate(g.nodes()):
        # print(id, label)
        nodes_id[label] = id
        # nodes_label[id] = label
        nodesList.append(id)
    for i in nodesList:
        nodes.append({"name": str(i), 'symbol': "image://static/svgs/lowlevel.svg"})

    for (v0, v1) in g.edges():
        edges.append({'source': str(nodes_id[v1]), 'target': str(nodes_id[v0])})
        # edges.append(nodes_id[v0], nodes_id[v1])
    return nodes, edges

# if __name__ == '__main__':
# line = '4031 4038\n'
# a = line.split()
# a = '1 2\n'.split()
# print(a)
# nodes,links = json2jsseries("topo66.json")
# nodes,links = txt2jsseries("D:\\Document\\satellite-sdn\\topo\data\\topo2.txt")
# print(nodes)
# print(links)
# nodes, links = gml2jsseries("D:\\Document\\satellite-sdn\\topo\data\\topo2.gml")
# print(links)
