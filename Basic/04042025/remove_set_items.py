# REMOVE SET ITEMS
# REMOVE ITEM
# To remove an item in a set, use the remove(), or the discar() method.

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)

# If the item remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.discard("banana")
print(thisset)

# If the item to remove does not exist, discard() will not raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Sets are unorded, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset
#print(thisset) # Shows a error
