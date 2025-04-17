# ARRAY INDEXING
# Access array elements
# Array indexing is the same as accessing an array element. You can access an array element by reffering to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1, etc.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])

print(arr[2] + arr[3])

# Access 2-D arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st row: ', arr[0, 1])
print('5nd element on 2nd row: ', arr[1, 4])

# Access 3-D arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr[0, 1, 2])

# Negative indexing

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr[1,-1])

