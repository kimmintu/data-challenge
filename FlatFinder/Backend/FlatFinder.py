import pymongo

class FlatFinder:
    def __init__(self):
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__initDB()

    def __initDB(self):
        dblist = self.__mongoClient.list_database_names()
        if "flatdb" in dblist:
            print("The database exists.")
        else:
            self.__mongoClient["flatdb"]

    def FindByStandort(self, standort):
        mydb = self.__mongoClient["flatdb"]
        db = mydb["flats"]
        myquery = {"companyCity" : "Luzern"}

        return result