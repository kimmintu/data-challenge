import pymongo
import json
import pymongo
from bson import json_util

class FlatFinder:
    def __init__(self):
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__initDB()

    def __initDB(self):
        dblist = self.__mongoClient.list_database_names()
        if "flatdb3" in dblist:
            print("The database exists.")
        else:
            self.__mongoClient["flatdb3"]

    def FindByStandort(self, standort):
        mydb = self.__mongoClient["flatdb3"]
        db = mydb["flats"]
        myquery = {"cityName" : standort}
        query2 = {"attributesInside":{"wheelChairAccessible":True,"cellar":True}}
        foo = db.find_one(query2)

        return json.dumps(foo, sort_keys=True, indent=4, default=json_util.default)