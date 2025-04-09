# ARRAYS
# Note: Python does not have built-in support for arrays, but Python lists can be used instead.
# Note: This page shows you how to use lists as arrays, however, to work with arryas in Python you will have to import a library, like the NumPy library.

# Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

# Access the elements of an array
# You refer to an array element by referring to the index number.

# Get the value of the first array item:
x = cars[0]

# Modify the value of the first array item:
cars[0] = "Toyota"

# The length of an array

x = len(cars)

# Looping array elements
# You can usethe for in loop to loop through all the elements of an array.

for x in cars:
    print(x)

# Adding array elements

cars.append("Honda")

# Removing array elements
# Delete the second element of the cars array:

cars.pop(1)

# You can also use the remove() method to remove an element from the array.

cars.remove("Volvo")

# Array methods
# Python has a set of bult-in methods that you can use on lists/arrays.
'''
Method      Description
append()    Adds an element at the end of the list.
clear()     Removes all the elements from the list.
copy()      Returns a copy of the list.
count()     Returns the number of elements with the specified value.
extend()    Add the elements of a list (or any iterable),to the end of the current list.
index()     Return the index of the first element with the specified value.
insert()    Adds an element at the specified position.
pop()       Removes the element at the specified position.
remove()    Removes the first item with the specified position.
reverse()   Reverse the order of the list.
sort()      Sorts the list.
'''