# Normal code
fruits = ["apple", "banana", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("")

# With list comprehension
newlist = [x for x in fruits if "a" in x]

print(newlist)

print("")

# The syntax
# newlist = [expression for item in iterable if condition == true]

# Condition
# The condition is like a filter that only accepts the items that evaluate to True

newlist = [x for x in fruits if x != "apple"]

print(newlist)

print("")

# Iterable

newlist = [x for x in fruits]

print(newlist)

print("")

newlist = [x for x in range(10)]

print(newlist)

print("")

newlist = [x for x in range(10) if x < 5]

print(newlist)

print("")

# Expression

newlist = [x.upper() for x in fruits]

print(newlist)

print("")

newlist = ['hello' for x in fruits]

print(newlist)

print("")

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

print("")