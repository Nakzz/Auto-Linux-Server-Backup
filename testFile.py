import json
import datetime
import os
from packageTracker import  packageTracker
import logging

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

print(data['includeDir'])

for x in data['includeDir']:
    print(x)

print(data['ftp']['host'])

# dateFormat =  str(date.today().year) + str(date.today().month) + str(date.today().day)
# print(dateFormat)

print(len(data['includeDir']))



def f(first, second=None):
  print(first, second)
  if(second and os.path.exists("bac")):
    print(second)


f("abc", "cbd")


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

print(BASE_DIR)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
deploymentHistoryList = BASE_DIR + "/deploymentHistoryList.json"





logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)


# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

bt = packageTracker(["cbc", "ebd"])

remove = bt.getFileToRemove()

logger.debug(remove)

text = "/var/boxBackupDeployment/sqlDumps/20181126_mysqlDump.sql"

name = text.split("/")
print(name)
print(len(name))
print("File to deploy: " + name[len(name)])
