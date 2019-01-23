import logging
from pymongo import MongoClient

#database
client = MongoClient('localhost', 27017)
db = client.demo

#logger
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
log = logging

