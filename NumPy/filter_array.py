# FILTER ARRAY
# Filtering arrays

# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.

# A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np

arr = np.array([41, 42, 43,44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# The example above will return [41, 43], why?
# Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.

# Creating the filter array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43,44])

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating filter directly from array
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

# We can directly substitute the array instead of the iterable variable in out condition and it will work just as we except it to.

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43,44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
