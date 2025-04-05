# ACCESSING ITEMS
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:

x = thisdict.get("model")
print(x)

# Get keys
# The keys() method will return alist of all the keys in the dictionary.

x = thisdict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

# Get values
# The values() method will return a list of all the values in the dictionary.
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.values()
print(x)

car["year"] = 2020
print(x)

# Add a new item to the original dictionary, and see that the values list gets updated as well:

x = car.values()
print(x)

car["color"] = "red"
print(x)

# Get items
# The items() method will return each item in a dictionary, as tuples in a list.
# The returned list is a view of the items of the dictionary, meaning taht any cnages done to the dictionary will be reflected in the items list.

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.items()
print(x)

car["year"] = 2020
print(x)

# Add a new item item to the original dictionary, and see that the items list gets updated as well:

x = car.items()
print(x)

car["color"] = "red"
print(x)

# Check if key exists
# To determine if a specified key is present in a dictionary use the in keyword:

thisdic = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

if "model" in thisdict :
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

