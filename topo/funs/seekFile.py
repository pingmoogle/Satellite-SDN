import json
import re
import time

import pymongo


def seekFile(fileName):
    """
    Get a dict by filename from Mongodb Data Server

    :param fileName: 文件名，无需路径
    :return: dict
    """
    client = pymongo.MongoClient(host='soowin.icu', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    result = collection.find_one({"fileName": fileName})
    client.close()
    return result["fileRaw"]


def uploadFile(fileObj):
    fs = str(fileObj.read(), encoding="utf-8")
    try:
        fileRawData = json.loads(fs)
    except json.decoder.JSONDecodeError:
        fileRawData = fs
    newFileDict = {
        "fileRaw": fileRawData,
        "fileVersion": "v1",
        "fileName": re.search('filename="(.*)"', fileObj.headers.get("Content-Disposition")).group(1)
    }

    client = pymongo.MongoClient(host='soowin.icu', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    result = collection.insert_one(newFileDict)
    client.close()

    return newFileDict["fileName"]


def uploadFileWithName(fileObj, fileName):

    newFileDict = {
        "fileRaw": fileObj,
        "fileVersion": "v1",
        "fileName": fileName + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    }
    client = pymongo.MongoClient(host='soowin.icu', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    collection.insert_one(newFileDict)
    client.close()


def fileHistroy() -> str:
    fh = ""
    client = pymongo.MongoClient(host='soowin.icu', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    result = collection.find()
    for i in result:
        thisname = i["fileName"]
        fh = fh + "<option>" + thisname + "</option>"
    client.close()
    return fh


if __name__ == '__main__':
    f = seekFile("topo.json")
    print(type(f))
