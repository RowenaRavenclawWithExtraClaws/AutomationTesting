import requests
import json
from datetime import datetime


# A class for saving the response of every http request to the signup api in a json-like format.
class HttpInterceptor:

    @staticmethod
    def intercept(url):
        response = requests.get(url)
        data = {}  # A dictionary for holding some meta-data for http request.
        data['response'] = str(response)
        data['url'] = response.request.url
        data['time'] = str(datetime.now())

        try:
            with open("logs.txt", 'a') as outFile:
                json.dump(data, outFile)
                outFile.write('\n')
        except:
            print('unable to open the logs file!')

    @staticmethod
    def getLogs():
        log = {}
        logList = []
        try:
            with open("logs.txt") as inputFile:
                for jsonObj in inputFile:
                    log = json.loads(jsonObj)
                    logList.append(log)
        except:
            print('unable to open the logs file!')

        return logList
