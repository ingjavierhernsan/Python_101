# JOINING ARRAY
# Joining NumPy arrays

# Joining means putting contents of two or more arrays in single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicity passed, it is taken as 0.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# Join two 2-D arrays along rows (axis=1):

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

# Joining arrays using stack functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# Stacking along rows
# NumPy provides a helper function: hstack() to stack along rows.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

# Stacking along columns
# NumPy provides a helper function: vstack() to stack along columns.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

# Stacking along height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
