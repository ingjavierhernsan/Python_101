# DICTIONARY
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

# Print the "brand" value of the dictionary:

print(thisdict["brand"])

# Duplicates not allowed
# Dictionaries cannot have two items with teh same key:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}

print(thisdict)

# Duplicate values will overwrite existing values.

# Dictionary length

print(len(thisdict))

# Dictionary Items - Data types

# String, int, boolean, and list data types:
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964,
    "colors" : ["red", "white", "blue"]
}

# type()
print(type(thisdict))

# The dict() constructor
# Is is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

