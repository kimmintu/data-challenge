
import json
import pymongo
from bson import json_util

class FlatFinder:
    def __init__(self):
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__initDB()
        self.__collection = "flatdb3"

    def __initDB(self):
        dblist = self.__mongoClient.list_database_names()
        if "flatdb3" in dblist:
            print("The database exists.")
        else:
            self.__mongoClient[self.__collection]

    def FindAll(self):
        mydb = self.__mongoClient[self.__collection]
        db = mydb["flats"]
        documents = db.find()
        images = []
        return self.__PreparePictureHtml(documents, "all")

    def FindSeniors(self):
        mydb = self.__mongoClient[self.__collection]
        db = mydb["flats"]
        query = {"propertyDetails.attributesInside.wheelChairAccessible": True}
        documents = db.find(query)
        return self.__PreparePictureHtml(documents, "wheelchair accessible")

    def __PreparePictureHtml(self, documents, criteria):
        images = []
        descs = []
        i = 0
        for doc in documents:
            i += 1
            prop = doc["propertyDetails"]
            try:
                imageProp = prop["images"]
                desc = prop["shortDescription"]
            except:
                continue
            if len(imageProp) > 0:
                images.append(imageProp[0]["url"])
                descs.append(desc)
            else:
                print("no picture")
        html = "<html><h1>Number of flats found with search criteria \"" + criteria + "\": " + str(i) + "</h1>"
        counter = 0
        for img in images:
            html += "<li>" + descs[counter] + "<br><br>"

            url = img.replace("{width}x{height}/{resizemode}/{quality}", "300x200/3/9")
            html += "<img src=" + url + ">"
            html += "</li><br><br>"
            print(url)
            counter +=1
        html += "</html>"
        print(html)

        return html

    def FindTest(self, test):
        mydb = self.__mongoClient[self.__collection]
        db = mydb["flats"]
        myquery = {"propertyDetails.id": 6282529 }
        #{"instock": {qty: 5, warehouse: "A"}}
        query = {"propertyDetails.attributesInside.wheelChairAccessible":True}
        foo = db.find(myquery)

        #return json.dumps(foo, sort_keys=True, indent=4, default=json_util.default)

        #"wheelChairAccessible": true, "cellar": true}

        results = {"results": []}
        for f in foo:
            result = json.dumps(f, sort_keys=True, indent=4, default=json_util.default)
            results["results"].append(result)

        #return results