import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGOURI")

client = MongoClient(uri)

db = client.banks
acc = db.accounts

#delete all documents in the collection

acc.delete_many({})
client.close()