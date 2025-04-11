# SORT
# Sort the result

# Use the sort() method to sort the result in ascending of descending order.
# The sort() method takes one parameter for "fildname" and one parameter for "direction" (ascending is the default direction).

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

# Sort descending
# Use the value -1 as the second parameter to sort descending.

# sort("name", 1) #ascending
# sort("name", -1) #descending

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)
