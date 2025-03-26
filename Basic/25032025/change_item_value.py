# Change item value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)

print("\n")

# Change a range of item values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print("\n")

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "Watermelon"]
print(thislist)

print("\n")

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("\n")

#Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("\n")