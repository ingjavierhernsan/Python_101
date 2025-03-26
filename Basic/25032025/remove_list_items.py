# Remove specified item

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)

print("")

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)

print("")

# Remove specified index

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)

print("")

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop()
print(thislist)

print("")

thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)

print("")

thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist
#print(thislist) # error, the list is deleted

print("")

# Clear the list
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)

print("")
