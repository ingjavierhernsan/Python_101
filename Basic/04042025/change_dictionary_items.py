# CANGE DICTIONARY ITEMS
# Change values

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

thisdict["year"] = 2018
print(thisdict)

# Update dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:valye pairs.

print(thisdict)

thisdict.update({"year" : 2020})
print(thisdict)