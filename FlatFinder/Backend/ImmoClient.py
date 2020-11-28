import json
from urllib.parse import urljoin
from AdvertModifier import AdvertModifier
import requests

# add &pa=30 to retrieve newest rental from the last 30 days
# param l is the id for the city (i.e. 2253 is Luzern, 4147 for Zürich etc.)
class ImmoClient:
    def __init__(self):
        self.__baseUrl = "https://rest-api.immoscout24.ch/v4/de/properties/"
        self.__url = 'https://rest-api.immoscout24.ch/v4/de/properties?l=2253&r=5&s=1&t=1'


    def InsertRawData(self):
        response = requests.get(self.__url)
        rawJson = response.json()
        totalPages = rawJson["pagingInfo"]["totalPages"]

        modifier = AdvertModifier()
        for page in range(totalPages-1):
            url2 = self.__url + "&pn="+str(page+1)
            response = requests.get(url2)
            rawJson = response.json()
            properties = rawJson["properties"]
            print("page " + str(page))
            for prop in properties:
                id = prop["id"]
                response = requests.get(urljoin(self.__baseUrl, str(id)))
                rawJson = response.json()
                modifier.Insert(rawJson)

        return "worked"

    def getDetailAd(self, id):
        response = requests.get(urljoin(self.__baseUrl, id))
        rawJson = response.json()
        return rawJson