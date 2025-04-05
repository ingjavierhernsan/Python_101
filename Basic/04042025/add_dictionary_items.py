# ADD DICTIONARY ITEMS
# Adding items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict["color"] = "red"
print(thisdict)

# Update dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argumet must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict.update({"color" : "red"})
print(thisdict)
