import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongoURI = os.getenv("MONGOURI")

client = MongoClient(mongoURI)

#referencing the 'banks' database
db = client.banks

#referencing the 'accounts' collection
accounts_collection = db.accounts

#the insert_many method takes an iterable list of documents
new_accounts = [
    {
      "account_id": "A1B2C3D4E5",
      "account_holder": "John Doe",
      "account_type": "Savings",
      "balance": 15000.75,
      "transfers_complete": ["TXN12345", "TXN67890"]
    },
    {
      "account_id": "F6G7H8I9J0",
      "account_holder": "Jane Smith",
      "account_type": "Checkings",
      "balance": 2500.50,
      "transfers_complete": ["TXN23456", "TXN78901"]
    },
    {
      "account_id": "K1L2M3N4O5",
      "account_holder": "Alice Johnson",
      "account_type": "Savings",
      "balance": 32000.00,
      "transfers_complete": ["TXN34567", "TXN89012"]
    },
    {
      "account_id": "P6Q7R8S9T0",
      "account_holder": "Bob Brown",
      "account_type": "Checkings",
      "balance": 500.00,
      "transfers_complete": ["TXN45678", "TXN90123"]
    },
    {
      "account_id": "U1V2W3X4Y5",
      "account_holder": "Carol White",
      "account_type": "Savings",
      "balance": 7800.25,
      "transfers_complete": ["TXN56789", "TXN01234"]
    },
    {
      "account_id": "Z6A7B8C9D0",
      "account_holder": "David Green",
      "account_type": "Checkings",
      "balance": 1200.00,
      "transfers_complete": ["TXN67890", "TXN12345"]
    },
    {
      "account_id": "E1F2G3H4I5",
      "account_holder": "Eva Black",
      "account_type": "Savings",
      "balance": 9500.50,
      "transfers_complete": ["TXN78901", "TXN23456"]
    },
    {
      "account_id": "J6K7L8M9N0",
      "account_holder": "Frank Blue",
      "account_type": "Checkings",
      "balance": 300.75,
      "transfers_complete": ["TXN89012", "TXN34567"]
    },
    {
      "account_id": "O1P2Q3R4S5",
      "account_holder": "Grace Yellow",
      "account_type": "Savings",
      "balance": 45000.00,
      "transfers_complete": ["TXN90123", "TXN45678"]
    },
    {
      "account_id": "T6U7V8W9X0",
      "account_holder": "Henry Orange",
      "account_type": "Checkings",
      "balance": 2200.25,
      "transfers_complete": ["TXN01234", "TXN56789"]
    }
  ]

#the insert_many method returns a result that gives us access to the _id of inserted documents
result = accounts_collection.insert_many(new_accounts)

documentIDs = result.inserted_ids

print(f"The number of inserted documents is: {str(len(documentIDs))}")
print(f"The IDs of the inserted documents are: {documentIDs}")

client.close()