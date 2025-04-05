thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

# CREATE TUPLE WITH ONE ITEM
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# NOT A TUPLE
thistuple = ("apple")
print(type(thistuple))

# TUPLE ITEMS - DATA TYPES
# Tuple items can be of anay data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

# THE TUBPLE() CONSTRUCTOR
# It is also possible to use the tuple() constructor to ake a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

