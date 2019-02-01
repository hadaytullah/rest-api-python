import logging
from pymongo import MongoClient
import os


print(os.environ.get('SECRET'))
try:
    JWT_SECRET = os.environ.get('SECRET')
    DB_URL = os.environ.get('db_url')
    DB_PORT = os.environ.get('db_port')
    
    #database
    client = MongoClient(DB_URL, int(DB_PORT))
    db = client.demo
    
    #logger
    #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    log = logging
    
    #TODO: Store the key as an env variable on production machine
    jwt_config = {
        'secret': JWT_SECRET,
        'algo': 'HS256',
        'expiration_delta_seconds': 20
        
    }
except KeyError:
    print('Please fix the environment.')

