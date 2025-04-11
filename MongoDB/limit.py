# LIMIT THE RESULT

# To limit the result in MongoDB, we use the limit() method.
# The limit() method takes one parameter, a number defining how many documents to return.
# Consider you have a "customers" collection.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

for x in myresult:
    print(x)

