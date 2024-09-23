import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
mongouri = os.getenv("MONGOURI")

client = MongoClient(mongouri)

for dbNames in client.list_database_names():
    print(dbNames)