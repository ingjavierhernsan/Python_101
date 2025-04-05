# ACCESS TUPLE ITEMS
# You can access tuple items by referring to the index number, inside square brackers:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])

# NEGATIVE INDEXING
print(thistuple[-1])

# RANGE OF INDEXES
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

# RANGE OF NEGATIVE INDEXES
print(thistuple[-4:-1])

# CHECK IF ITEM EXISTS
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

