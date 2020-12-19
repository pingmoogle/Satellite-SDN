import json
import pymongo


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

    result = collection.find_one({"fileName": "{0}".format(fileName)})
    json2dict = json.loads(result["fileRaw"])

    client.close()
    return json2dict


if __name__ == '__main__':
    pass
