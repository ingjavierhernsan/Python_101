# PIP
# POP is a package manager for Python packages, or modules if you like.
# Note: If you have Python version 3.4 or later, PIP is included by default.

# What is a package?
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# Check if PIP is installed
# Navigate your command line to the location of Python's script directory, and type the following:

#pip --version

# Install PIP
# If you do not have PIP installed, you can download and install it from this page:
# https://pypi.org/project/pip/

# Download a package
# Downloading a package is very easy.
# Open the command line interface and tell PIP to download the package you want.
# Navigate your command line to the location of Python's script directory, and type the following:

# pip install camelcase

# Using a package
# Once the package is installed, it is ready to use.
# Import the "camelcase" package into your project.

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# Find packages
# Find more packages at https://pypi.org/

# Remove a package
# Use the uninstall command to remove a package:

# pip unistall camelcase

# The PIP package manager will ask you to confirm that you want to remove the camelcase package.
# Press y and the package will be removed.

# List packages
# Use the list command to list all the packages installed on your system:

# pip list
