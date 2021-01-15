from topo.funs import seekFile
def json2jsseries(filename,timeSlice=0):
    f = seekFile.seekJson(filename)
    topo_data = f["topo"][timeSlice]["describe"]
    nodes = []
    link = []

    for i in topo_data:
        nodeDict = {}
        a = str(int(i['LeoID']))
        nodeDict["name"] = a
        # nodeDict["fixed"] = False
        nodes.append(nodeDict)
        for j in i["neighbor"]:
            link.append({"source": a, "target": str(int(j["NbID"])), "LocalPort": int(j["LocalPort"]), "NbPort": int(j["NbPort"])})
    links = []
    for i in link:
        tmp = []
        tmp.append("image://static/svgs/3" + str(i["LocalPort"]) + "-20e3.svg")
        tmp.append("image://static/svgs/3" + str(i["NbPort"]) + "-20e3.svg")
        i["symbol"] = tmp
        ce = {"source":i["source"], "target":i["target"], "symbol":i["symbol"]}
        links.append(ce)
        del ce

    return nodes, links