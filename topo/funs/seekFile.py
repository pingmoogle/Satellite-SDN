import json
import pymongo
import re


def seekJson(fileName) -> dict:
    """
    Get a dict by filename from Mongodb Data Server

    :param fileName: 文件名，无需路径
    :return: dict
    """
    client = pymongo.MongoClient(host='47.95.110.42', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    result = collection.find_one({"fileName": fileName})
    client.close()
    return result["fileRaw"]


def uploadFile(fileObj):
    fileRawinJSON = json.loads(str(fileObj.read(), encoding="utf-8"))
    newFileDict = {
        "fileRaw": fileRawinJSON,
        "fileVersion": "v1",
        "fileName": re.search('filename="(.*)"', fileObj.headers.get("Content-Disposition")).group(1)
    }

    client = pymongo.MongoClient(host='47.95.110.42', port=27017)

    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.jsonfiles
    result = collection.insert_one(newFileDict)
    client.close()

    return newFileDict["fileName"]



def fileHistroy() -> str:
    fh = ""
    client = pymongo.MongoClient(host='47.95.110.42', port=27017)

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
    pass








