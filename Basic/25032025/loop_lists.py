# Loop through a list
thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

print("")

for i in range(len(thislist)):
    print(thislist[i])

print("")

# Using a while loop

i = 0

while i < len(thislist):
    print(thislist[i])
    i = i + 1

print("")

# Looping using list complehension

[print(x) for x in thislist]

print("")
