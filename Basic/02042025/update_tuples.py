# UPDATE TUPLES
'''
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some  workarounds.
'''
# CHANGE TUPLE VALUES
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# ADD ITEMS
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# REMOVE ITEMS
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Ore you can delete the tuple completely:
del thistuple
#print(thistuple) # this will raise an error because the tuple no longer exists.
