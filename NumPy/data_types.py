# DATA TYPES
# Datatypes in Python
'''
By default Python have these data types:
strings - used to represent text data, the text is given under quotes marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''

# Data types in NumPy
'''
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type (void)
'''

# Checking the data type of an array
# The NumPy array object has a property called dtype that returns the data type of the array:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# Creating arrays with a defined data type
# We use the array() function to create arrays, this function can take an iptional argument: dtype that allows us to define the expected deta type of the array elements:

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

# What if a value can not be converted?
# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# arr = np.array(['a', '2', '3'], dtype='i') #Error

# Converting data type on existing arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
