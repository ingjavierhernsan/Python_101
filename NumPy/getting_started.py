# NumPy getting started
#Installation of NumPy

# If you have Python and PIP already installed on a system, then installation of NumPy is very easy.
# Install it using this command:

# pip install numpy

# Import NumPy

import numpy

# NOw NumPy is imported and ready to use.

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

# NumPy as np
# NumPy is usually imported under the np alias.

import numpy as np

# Now the NumPy package can be referred to as np instead of numpy.

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# Checking NumPy version
# The version string is stored under __version__ attribute.

print(np.__version__)
