import pymongo

class AdvertModifier:
    def __init__(self):
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__initDB()

    def __initDB(self):
        dblist = self.__mongoClient.list_database_names()
        if "flatdb3" in dblist:
            print("The database exists.")
        else:
            self.__mongoClient["flatdb3"]

    def Insert(self, rawJson):
        collection = self.__mongoClient["flatdb3"]
        db = collection["flats"]

        db.insert_one(rawJson)