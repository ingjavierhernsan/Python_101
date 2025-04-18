# ARRAY RESHAPING
# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions of change number of elements in each dimension.

# Reshape from 1-D to 2-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr)

newarr = arr.reshape(4, 3)

print(newarr)

# Reshape from 1-D to 3-D

print(arr)

newarr = arr.reshape(2, 3, 2)

print(newarr)

# Can we reshape into any shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

#newarr = arr.reshape(3, 3)
#print(newarr)

# Returns copy or view?

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

# The example above returns the orifinal array, so it is a view.

# Unknown dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# Note: We can not pass -1 to more than one dimension.

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud, etc. These fall under intermediate to advanced section of numpy.
