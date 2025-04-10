# MODULES
# What is a module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you wants to include in your application.

# Create a module
# To create a module just save the code you want in a file with the file extension .py:

# mymodule.py
def geeting(name):
    print("Hello, " + name)

# Now we can use the module we just created, by using the import statement:
import mymodule

mymodule.greeting("Jonathan")

# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in module
# The module can contain functions, as already described, but also variables of all type (arrays, dictionaries, objects etc):

# mymodule.py
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Import the module named mymodule, and access the person1 dictionary:
import mymodule

a = mymodule.person1["age"]
print(a)

# Naming a module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a module
# You can create an alias when you import a module, by using the as keyword:

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in modules
# There are several built-in modules in Python, which you can import whenever you like.

import platfrom

x = platform.system()
print(x)

# Using the dir() function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import platform

x = dir(platform)
print(x)

# Note: The dir() function can be used on all modules, also the oners you create yourself.

# Import from module
# You can choose to import only parts from a module, by using the from keyword.

#mymodyle.py

def greeting(name):
    print("Hello" + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Import only the person1 dictionary from the module:

from mymodule import person1

print(person1["age"])

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["ate"], not mymodule.person1["age"]
