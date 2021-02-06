import json
import re
import time

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
        nodeDict = {
            "ports": []
        }
        a = str(int(i['LeoID']))
        nodeDict["name"] = a
        # nodeDict["fixed"] = False
        nodeDict['symbol'] = "image://static/svgs/lowlevel.svg"
        # nodes.append(nodeDict)
        for j in i["neighbor"]:
            nodeDict["ports"].append(int(j["LocalPort"]))
            link.append({"source": a, "target": str(int(j["NbID"])), "LocalPort": int(j["LocalPort"]),
                         "NbPort": int(j["NbPort"])})
        nodes.append(nodeDict)

    links = []
    for i in link:
        tmp = []
        tmp.append(i["LocalPort"])
        tmp.append(i["NbPort"])
        i["ports"] = tmp
        ce = {"source": i["source"], "target": i["target"], "ports": i["ports"],
              "tooltip": i["source"] + ": " + str(tmp[0]) + " -- " + i["target"] + ": " + str(tmp[1])
              }
        links.append(ce)
        del ce

    return nodes, links


def txt2jsseries(filename, timeSlice=0):
    # txt转json函数，返回新json文件名
    findThisName = filename.split('.')[0] + ".txt.json"
    if seekFile.seekFile(findThisName) == None:
        newFilename = txt2json(filename)
        return json2jsseries(newFilename)
    else:
        return json2jsseries(findThisName)


def txt2json(filename):
    file = seekFile.seekFile(filename)
    newFilename = filename.split('.')[0] + ".txt.json"
    # print(newFilename)
    newFile = {}
    newFile["topo"] = [{"timeSlice": 0, "describe": []}]

    # 节点统计
    nodes = {}
    # 统计各节点端口
    allPorts = {}
    file = file.splitlines()
    for i in file:
        line = i.split()
        if line[0] not in nodes:
            nodes[line[0]] = {"LeoID": int(line[0]), "neighbor": []}
            allPorts[line[0]] = 0
        if line[1] not in nodes:
            nodes[line[1]] = {"LeoID": int(line[1]), "neighbor": []}
            allPorts[line[1]] = 0
    # print(nodes)
    # file.seek(0)
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

    seekFile.uploadFileWithName(newFile, newFilename)
    return newFilename


def gml2jsseries(filename, timeSlice=0):
    # gml转json函数，返回新json文件名
    findThisName = filename.split('.')[0] + ".gml.json"
    if seekFile.seekFile(findThisName) == None:
        newFilename = gml2json(filename)
        return json2jsseries(newFilename)
    else:
        return json2jsseries(findThisName)


def gml2json(filename):
    file = seekFile.seekFile(filename)
    g = nx.parse_gml(file)
    # g = nx.read_gml(filename)

    newFilename = filename.split('.')[0] + ".gml.json"

    newFile = {}
    newFile["topo"] = [{"timeSlice": 0, "describe": []}]
    # 节点统计
    nodes = {}
    # 统计各节点端口
    allPorts = {}

    # 处理gml，得到edges列表，每一项都是一个字典，内含"source"和"target"
    edges = []
    nodes_id = dict()
    # nodes_label = dict()
    for id, label in enumerate(g.nodes()):
        nodes_id[label] = id
    for (v0, v1) in g.edges():
        edges.append({'source': str(nodes_id[v1]), 'target': str(nodes_id[v0])})

    for i in edges:
        if i['source'] not in nodes:
            nodes[i['source']] = {"LeoID": int(i['source']), "neighbor": []}
            allPorts[i['source']] = 0
        if i['target'] not in nodes:
            nodes[i['target']] = {"LeoID": int(i['target']), "neighbor": []}
            allPorts[i['target']] = 0
    # print(nodes)
    for i in edges:
        allPorts[i['source']] = allPorts[i['source']] + 1
        allPorts[i['target']] = allPorts[i['target']] + 1
        nodes[i['source']]["neighbor"].append(
            {"LocalPort": allPorts[i['source']], "NbID": int(i['target']), "NbPort": allPorts[i['target']]})
        nodes[i['target']]["neighbor"].append(
            {"LocalPort": allPorts[i['target']], "NbID": int(i['source']), "NbPort": allPorts[i['source']]})
    for i in nodes.values():
        newFile["topo"][0]["describe"].append(i)

    seekFile.uploadFileWithName(newFile, newFilename)
    return newFilename


def appendAction(filename, changes):
    originFileRaw = seekFile.seekFile(filename)
    originFileRaw["action"] = changes
    newfilename = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + "_" + filename
    seekFile.uploadFileWithName(originFileRaw, newfilename)
    return newfilename

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
