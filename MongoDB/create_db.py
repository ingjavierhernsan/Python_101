# CREATE DATABASE
# Creating a database
# To create a database in MongoDB, start by creating a MOngoClient object, then specify a connection URL with the correct ip address and the name of he database you want to create.
# MongoDB will create the database if it does not exist, and make a connection to it.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

# Important: In MongoDB, a database is not created until it gets content!

# MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (ans collection).

# Check if database exists
# You can check if a database exist by listing all databases in your system:

print(myclient.list_database_names())

# Or you can check a specific database by name:

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("The database exists.")

