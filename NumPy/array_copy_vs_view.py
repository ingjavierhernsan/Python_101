# ARRAY COPY VS VIEW
# The difference between copy and view
'''
The main difference a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''

# Copy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# The copy should not be affected by the changes made to the original array.

# View

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# The view should be affected by the changes made to the original array.

# Make changes in the view

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# The original array should be affected by the changes made to the view.

# Check if array owns its data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

# The copy returns None.
# The view returns the original array.
