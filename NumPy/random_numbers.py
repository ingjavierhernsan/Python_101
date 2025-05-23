# RANDOM NUMBERS

# What is a random number?
# Random number does not mean a different number every time. Random means something that can not be predicted logically.

# Generate random number
# NumPy offers the random module to work with random numbers.

from numpy import random

x = random.randint(100)

print(x)

# Generate random float
# The random module's rand() method returns a random float between 0 and 1.

x = random.rand()

print(x)

# Generate random array
# In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

# Integers
# The randit() method takes a size parameter where you can specify the shape of an array.

x = random.randint(100, size=(5))

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

x = random.randint(100, size=(3, 5))

print(x)

# Floats
# The rand() method also allows you to specify the shape of the array.

# Generae a 1-D array containing 5 random floats:
x = random.rand(5)

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)

print(x)

# Generate random number from array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

# Return one of the values in a array:
x = random.choice([3, 5, 7, 9])

print(x)

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

