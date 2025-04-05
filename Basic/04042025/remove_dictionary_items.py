# REMOVE DICTIONARY ITEMS
# Removing items
# The pop() method removes the item with the specified key name:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

del thisdict
#print(thisdict) # Show message error

# The clear() method empties the dictionary:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict.clear()
print(thisdict)
