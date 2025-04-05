# PYTHON SETS
myset = {"apple", "banana", "cherry"}

# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchageable, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

print(myset)

# Sets are unordered, so you cannot be sure in which order the items will appear.

# Set items
# Set items are unordered, unchangeable, and do not allow duplicae values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Sets cannot have two items with the same values.
thisset = {"apple", "banana", "cherry", "apple"} # Duplicate values will be ignored
print(thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set items - data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

print(type(set1))

# THE SET() CONSTRUCTOR
# It is also possible to use set() constructor to make a set.

thisset = set(("apple", "banana", "cherry"))
print(thisset)
