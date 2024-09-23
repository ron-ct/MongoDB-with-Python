import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

mongoURI = os.getenv("MONGOURI")

client = MongoClient(mongoURI)

#reference the 'banks' database
db = client.banks

#reference the 'accounts' collection
accountsCollection = db.accounts

#some synthetic data for testing purposes only
new_account = {
      "accountNumber": "1234567890",
      "accountHolderName": "John Doe",
      "accountType": "Savings",
      "balance": 15000.75,
      "branch": "Downtown",
      "createdAt": "2023-01-15T10:00:00Z"
    }

#the insert_one method returns a result that gives us access to the _id of the inserted document
result = accountsCollection.insert_one(new_account)

documentID = result.inserted_id

print(f"The id of the document is {documentID}")

client.close()

