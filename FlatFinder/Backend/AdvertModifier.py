import pymongo

class AdvertModifier:
    def __init__(self):
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__initDB()

    def __initDB(self):
        dblist = self.__mongoClient.list_database_names()
        if "flatdb" in dblist:
            print("The database exists.")
        else:
            self.__mongoClient["flatdb"]

    def Insert(self, rawJson):
        properties = rawJson["properties"]
        collection = self.__mongoClient["flatdb"]
        db = collection["flats"]

        for obj in properties:
            db.insert_one(obj)