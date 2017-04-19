import sys
print(sys.version)
import json
import urllib.request
import math
import time


#Function to sanitize and build api call to server
def generateApiCall(callType, increment, startTime, itemID):
    url = "https://api.rsbuddy.com/grandExchange?"
    multipleParams = False
    #TODO: sanitize all parameters
    if(callType is not None):
        if(callType == 'graph'):
            stub = "a="
            url = url + stub + callType
            if(increment is not None):
                stub = "&g="
                url = url + stub + increment
            if(startTime is not None):
                stub = '&start='
                url = url + stub + startTime
            if(itemID is not None):
                stub = '&i='
                url = url + stub + itemID
            else: return False
            return url
    else: return False

def getSummary():
    url = "https://rsbuddy.com/exchange/summary.json"
    jsonBlob = apiCall(url)
    return jsonBlob


def getItemHistory(id):
    startTime = "1474615279000"
    # startTime = str( math.floor(startTime) )#Get the current time we want to start at
    itemID = id #Eventually we will want this to come from input
    increment = "1440"
    callType = "graph"
    url = generateApiCall(callType, increment, startTime, itemID)
    json = apiCall(url)
    return json

def apiCall(url):
    r = urllib.request.urlopen(url)
    jsonBlob = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    return jsonBlob

def getIDbyName(name):
    summary = getSummary()
    for key, value in summary.items():
        if summary[key]["name"] == name:
            return key
    return -1


itemHistory = getItemHistory(getIDbyName("Salmon"))
for dataPoint in itemHistory:
    print(dataPoint)
