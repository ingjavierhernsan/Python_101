# CREATE COLLECTION
# A collection in MongoDB is the same as a table in SQL databases.

# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
# MongoDB will create the collection if it does not exist.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

# Check if collection exists
# You can check if a collection exist in a database by listing all collections:

print(mydb.list_collection_names())

# Or you can check a specific collection by name:

collist = mydb.list_collection_names()

if "customers" in collist:
    print("The collection exists.")

