# SORTING ARRAYS
# Sorting arrays

# Sorting means putting elements in an ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

arr = np.array([3, 2, 0, 1])

print(arr)

print(np.sort(arr))

# Note: This method returns a copy of the array, leaving the original array unchanged.

# You can also sort arrays of strings, or any other data type:

arr = np.array(['banana', 'cherry', 'apple'])

print(arr)

print(np.sort(arr))

arr = np.array([True, False, True])

print(arr)

print(np.sort(arr))

# Sorting a 2-D array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(arr)

print(np.sort(arr))
