import hashlib

import pymongo


def userCheck(username, userpassword):
    pswdHash = hashlib.sha256(userpassword.encode("utf8")).hexdigest()
    username = username.lower()
    client = pymongo.MongoClient(host='soowin.icu', port=27017)
    db = client.topos
    db.authenticate("topouser1", "123456")
    collection = db.users
    result = collection.find_one({"userName": username})
    if result is not None and result["userPassword"] == pswdHash:
        return username
    else:
        return False
