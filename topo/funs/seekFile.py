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
    result = collection.find_one({"fileName": fileName})
    client.close()
    return result["fileRaw"]


if __name__ == '__main__':
    pass








