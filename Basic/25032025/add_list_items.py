# Append items

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)

print("\n")

# Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
print(thislist)
print(tropical)
thislist.extend(tropical)
print(thislist)

print("\n")

# Add any iterable (add elements of a tuple to a list)
thislist = ["apple", "banana", "cherry"]
print(thislist)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("\n")
