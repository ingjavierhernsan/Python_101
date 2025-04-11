# INSERT DOCUMENT
# A document in MongoDB is the same as a record in SQL databases.

# To inset a record, of document as it is called in MongoDB, into acollection, we use the insert_one() method.
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

# Return the _id field
# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)

# If you do not specify an _id field, then MongoDB will add one for you and assign aunique id each document.
# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).

# Insert multiple documets
# To insert multiple documentsinto a collection in MongoDB, we use the insert_many() method.
# The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 45"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)

# The insert_many() method returns a InsertManyResult object, which hasa property, inserted_ids, that holds the ids of the inserted documents.

# Insert multiple documents, with specified ids

# If you do not want MongoDB to assign unique ids for your document, you can specify the _id field when you insert the document(s).
# Remember that the values has to be unique. Two documents cannot have the same _id.

mylist = [
    { "_id": 1, "name": "John", "address": "Higway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
