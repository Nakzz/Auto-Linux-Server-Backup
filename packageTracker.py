import json
import os
from datetime import datetime as dt

class packageTracker:
    removeFiles = []
    def __init__(self, newfilenames):
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        deploymentHistoryList = BASE_DIR + "/deploymentHistoryList.json"

        if ((os.path.isfile(deploymentHistoryList)) != True):
            print("DeploymentFile DNE")
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

        self.backupMySql = configData["backupMySql"]
        self.backupDir = (configData["backupDir"])
        self.incrementalNum = configData["numberOfBackups"]
        self.head = int(data['head'])
        self.tail = int(data['tail'])
        self.filenames = data['deployedFilenames'] # compressed and dump file names, date
        self.packageTime = str(dt.now())
        self.removeFiles = []

        self.add(newfilenames)

        if(self.tail - self.head > self.incrementalNum):
            self.remove()

        self.saveFile()



    def getFileToRemove(self):
        return self.removeFiles

    def add(self, filename):
        if(self.tail == 0):
            index=0
        else:
            index = self.tail +1

        if(self.backupDir == "True" and self.backupMySql == "True"):
            self.filenames[index] =filename[0], filename[1], self.packageTime
        if (self.backupDir == "True" or self.backupMySql == "True"):
            self.filenames[index] = filename[0], self.packageTime
        else:
            self.tail = self.tail - 1
        self.tail = self.tail + 1

    def remove(self):
        length = len(self.filenames[str(self.head)])
        # print(length)
        for i in range(length-1):
            # print(i)
            # print(self.filenames[str(self.head)][i])
            self.removeFiles.append(self.filenames[str(self.head)][i])
        # self.removeFiles = self.filenames[str(self.head)]
        self.head = self.head +1


    def saveFile(self):
        data= {'head':self.head, 'tail':self.tail, 'deployedFilenames':self.filenames}

        with open('deploymentHistoryList.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
