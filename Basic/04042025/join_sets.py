# JOIN SETS
# Join sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# UNION
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print(set1)
print(set2)

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print(set1)
print(set2)

set3 = set1 | set2
print(set3)

# Join multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

print(set1)
print(set2)
print(set3)
print(set4)

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3 | set4
print(myset)

# Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

print(x)
print(y)

z = x.union(y)
print(z)

# The | operator only allows you to join sets with sets, and not with other data types like you can with the union() method.

# UPDATE
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print(set1)
print(set2)

set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

# INTERSECTION
# Keep ONLY the duplicates.
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set3 = set1 & set2
print(set3)

# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The intersection_update() method will alseo keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set1.intersection_update(set2)
print(set1)

# The values True and 1 are condidered the same value. The same goes for False and 0.

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

print(set1)
print(set2)

set3 = set1.intersection(set2)
print(set3)

# DIFFERENCE
# The difference() method will retunr a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set3 = set1 - set2
print(set3)

# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set1.difference_update(set2)
print(set1)

# SYMMETRIC DIFFERENCES
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you vill get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set3 = set1 ^ set2
print(set3)

# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1)
print(set2)

set1.symmetric_difference_update(set2)
print(set1)
