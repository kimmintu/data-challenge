import time
import datetime
import urllib
import json
import flask
from shutil import copyfile
from ImmoClient import ImmoClient
from AdvertModifier import AdvertModifier
from FlatFinder import FlatFinder

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/insertlatest', methods=['GET'])
def insertLatestData():
    client = ImmoClient()
    rawdata = client.InsertRawData()

@app.route('/standort/<standort>', methods=['GET'])
def getByStandort(standort):
    finder = FlatFinder()
    return finder.FindByStandort(standort)

@app.route('/', methods=['GET'])
def getAll():
    client = ImmoClient()
    rawdata = client.InsertRawData()
    return rawdata

@app.route('/<id>', methods=['GET'])
def getFlatById(id):
    client = ImmoClient()
    print(str(id))
    rawdata = client.getDetailAd(id)
    return rawdata

#client = ImmoClient()
#rawdata = client.getRawJson()
#print(rawdata)

app.run()