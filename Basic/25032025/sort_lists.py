# Sort list alphanumerically
thislist = ["apple", "banana", "kiwi", "mango"]
thislist.sort()
 
print(thislist)

print("")

thislistNum = [100, 50, 65, 82, 23]
thislistNum.sort()
 
print(thislistNum)

print("")

# Sort descending
thislist = ["apple", "banana", "kiwi", "mango"]
thislist.sort(reverse = True)
 
print(thislist)

print("")

thislistNum = [100, 50, 65, 82, 23]
thislistNum.sort(reverse = True)
 
print(thislistNum)

print("")

#Customize sort function
def myfunc(n):
    return abs(n - 50)

thislistNum = [100, 50, 65, 82, 23]
thislistNum.sort(key = myfunc)
 
print(thislistNum)

print("")

# Case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
 
print(thislist)

print("")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
 
print(thislist)

print("")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
 
print(thislist)

print("")
