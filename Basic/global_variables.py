'''
Variables that are created outside of a function (as in all the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
'''

x = "awesome"

def myfunc():
    print("1.- Python is " + x)

myfunc()

'''
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
'''

x = "awesome"

def myfunc():
    x = "fantastic"
    print("2.- Python is " + x)

myfunc()

print("3.- Python is " + x)

'''
The global keyword
Normally, when you create a variable inside a function, that vvariable is local, and can only be used inside that function."
To create a global variable inside a function, you can use the global keyword.
'''

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("4.- Python is " + x)

'''
Also, use the global keyword if you want to change a global variable inside a function.
'''

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("5.- Python is " + x)