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

@app.route('/all', methods=['GET'])
def getAll():
    finder = FlatFinder()
    return finder.FindAll()

@app.route('/seniors', methods=['GET'])
def getSeniors():
    finder = FlatFinder()
    return finder.FindSeniors()

@app.route('/test/<test>', methods=['GET'])
def FindTest(test):
    finder = FlatFinder()
    return finder.FindTest(test)

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