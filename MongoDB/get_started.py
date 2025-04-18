# MONGODB

# Pyhon can be used in database applications.
# One of the most popular NoSQL database is MongoDB

'''
MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.
To be able to experiment with the code examples in this tutorial, you will need access to a MongoDB database.
You can download a free MongoDB database at https://www.mongodb.com.
Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.
'''
'''
PyMongo
Python needs a MongoDB driver to access the MongoDB database.
In this tutorial we will use the MongoDB driver "PyMongo".
We recommend that you use PIP to install "PyMongo"
PIP is most likely already installed in your Python environment.
Navigate your command line to the location of PIP, and type the following:
'''

# python3 -m pip install pymongo

# Test PyMongo
# To testif the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:

# demo_mongodb_test.py:

import pymongo
