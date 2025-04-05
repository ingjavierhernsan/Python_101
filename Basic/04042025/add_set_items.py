# ADD SET ITEMS
# Add items
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

# ADD SETS
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# ADD ANY ITERABLE
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries, etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

