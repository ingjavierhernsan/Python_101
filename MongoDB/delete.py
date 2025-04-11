#DELETE DOCUMENT

# To delete one document, we use the delete_one() method.
# The first parameter of the delete_one() method is a query object defining which document to delete.

# Note: If the query finds more than one document, only the first occurrence is deleted.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

# Delete many documents
# To delete more than one document, use the delete_many() method.
# The first parameter of the delete_many() method is a query object defining which documents to delete.

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

# Delete all documents in a collection
# To delete all documents in a collection, pass an empty query object to the delete_many() method:

x = mycol.delete_many({})

print(x.deleted_count, " docuemnts deleted.")

