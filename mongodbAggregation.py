import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pprint

load_dotenv()

MongoURI = os.getenv('MONGODBURI')

client = MongoClient(MongoURI)

db = client.banks

acc = db.accounts

# Say that we want to find the average of checkings and savings accounts for customers with balances less than $1000
conversion_rate = 1.33

# $match to filter accounts with balances less than 10000
select_balances = {"$match": {"balance": {"$lt": 10000}}}

# $group to group by account_type and calculate average balance
group_balances = {"$group": {"_id": "$account_type", "avg_bal": {"$avg": "$balance"}}}

# $project to return account_type, balance, and GBPbalance
return_only = {"$project": {"account_type": 1, "_id": 0, "balance": 1, "GBPbalance": {"$divide": ["$balance", conversion_rate]}}}

# $sort to organize results by balance in descending order
organize_by_balance = {"$sort": {"balance": -1}}

# Aggregation pipeline
pipeline = [select_balances, group_balances, organize_by_balance, return_only]

# Execute the aggregation pipeline
result = acc.aggregate(pipeline)

# Print results
for item in result:
    pprint.pprint(item)

client.close()