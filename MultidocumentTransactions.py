# To demonstrate multidocument transactions in MongoDB
# Sample situation, where in a bank setting, a user A wants to send $100 to another user B

import os
import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

# Load environment variables
load_dotenv()

mongoURI = os.getenv("MONGOURI")

# Connect to a MongoDB cluster via a MongoClient instance
client = MongoClient(mongoURI)

db = client.banks
acc = db.accounts

# Corrected query for finding accounts
pprint.pprint(list(acc.find({"_id": {"$in": ["A1B2C3D4E5", "F6G7H8I9J0"]}})))

def callback(session, sender_id=None, receiver_id=None, transfer_id=None, transfer_amount=None):
    # Reference the accounts collection
    accounts_col = session.client.banks.accounts

    # Reference the transfers collection
    transfers_col = session.client.banks.transfers

    transfer_document = {
        "sender_acc_id": sender_id,
        "receiver_acc_id": receiver_id,
        "transfer_id": transfer_id,
        "transfer_amount": transfer_amount
    }

    # Transfer operations
    # We need to pass the session to each operation

    # Update sender's account
    accounts_col.update_one(
        {"_id": sender_id},
        {"$inc": {"balance": -transfer_amount}, "$push": {"transfers_completed": transfer_id}},
        session=session
    )

    # Update receiver's account
    accounts_col.update_one(
        {"_id": receiver_id},
        {"$inc": {"balance": transfer_amount}, "$push": {"transfers_completed": transfer_id}},
        session=session
    )

    # Add the transfer document to the transfers collection
    transfers_col.insert_one(transfer_document, session=session)

    print("Successfully completed transaction")

    # Print the updated accounts
    pprint.pprint(list(accounts_col.find({"_id": {"$in": ["A1B2C3D4E5", "F6G7H8I9J0"]}})))
    return

# Define wrapper function to pass the values
def callback_wrapper(session):
    callback(session, "A1B2C3D4E5", "F6G7H8I9J0", "SQDQD001", 100)

with client.start_session() as session:
    # Correct method for starting a transaction
    session.with_transaction(callback_wrapper)

client.close()