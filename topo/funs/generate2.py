import json

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
        tmp.append(i["LocalPort"])
        tmp.append(i["NbPort"])
        i["ports"] = tmp
        ce = {"source": i["source"], "target": i["target"], "ports": i["ports"], "tooltip": i["source"]+": "+str(tmp[0])+" -- "+i["target"]+": "+str(tmp[1])
        }
        links.append(ce)
        del ce

    return nodes, links


def txt2jsseries(filename, timeSlice=0):
    # txt转json函数，返回新json文件名
    newFilename = txt2json(filename)
    # 处理新json，返回nodes和links数据
    return json2jsseries(newFilename)

def txt2json(filename):
    file = seekFile.seekFile(filename)
    newFilename = filename.split('.')[0] + "txt.json"
    # print(newFilename)
    newFile = {}
    newFile["topo"] = [{"timeSlice": 0, "describe": []}]

    # 节点统计
    nodes = {}
    # 统计各节点端口
    allPorts = {}
    for i in file:
        line = i.split()
        if line[0] not in nodes:
            nodes[line[0]] = {"LeoID": int(line[0]), "neighbor": []}
            allPorts[line[0]] = 0
        if line[1] not in nodes:
            nodes[line[1]] = {"LeoID": int(line[1]), "neighbor": []}
            allPorts[line[1]] = 0
    print(nodes)
    file.seek(0)
    for i in file:
        line = i.split()
        allPorts[line[0]] = allPorts[line[0]] + 1
        allPorts[line[1]] = allPorts[line[1]] + 1
        nodes[line[0]]["neighbor"].append(
            {"LocalPort": allPorts[line[0]], "NbID": int(line[1]), "NbPort": allPorts[line[1]]})
        nodes[line[1]]["neighbor"].append(
            {"LocalPort": allPorts[line[1]], "NbID": int(line[0]), "NbPort": allPorts[line[0]]})

    # print(nodes)
    for i in nodes.values():
        newFile["topo"][0]["describe"].append(i)
    # print(newFile)

    jsonFile = json.dumps(newFile)
    # ToDo 存储新的json文件 文件名：newFilename, 内容：jsonFile
    return newFilename


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


def appendAction(filename, changes):

    seekFile.uploadFile("name")
    return filename
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
