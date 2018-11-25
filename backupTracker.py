import json
import os
from datetime import datetime as dt

class backupTracker:
    def __init__(self, newfilenames):
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        deploymentHistoryList = BASE_DIR + "/deploymentHistoryList.json"

        if ((os.path.isdir(deploymentHistoryList)) != True):
            data={'head': 0,
                  'tail': 0,
                  'deployedFilenames':{
                      #0: ['', '', ''] # compressed and dummp file names, date
                  },
                  }

            with open('deploymentHistoryList.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)


        with open('deploymentHistoryList.json') as json_data_file:
            data = json.load(json_data_file)

        # read from config
        with open('config.json') as json_data_file:
            configData = json.load(json_data_file)

        self.incrementalNum = configData["numberOfBackups"]
        self.head = data['head']
        self.tail = data['tail']
        self.filenames = data['deployedFilenames'] # compressed and dump file names, date
        self.packageTime = str(dt.now())

        self.add(newfilenames)

        if(self.tail - self.head > self.incrementalNum):
            self.remove()
        self.saveFile()


    def add(self, filename):
        if(self.head == 0):
            index=0
        else:
            index = self.tail +1
        self.filenames[index] =filename[0], filename[1], self.packageTime
        self.tail = self.tail + 1

    def remove(self):
        self.head = self.head +1

    def saveFile(self):
        data= {'head':self.head, 'tail':self.tail, 'deployedFilenames':self.filenames}

        with open('deploymentHistoryList.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)