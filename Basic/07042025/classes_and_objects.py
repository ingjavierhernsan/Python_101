# CLASSES AND OBJECTS
# Python is an objext oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A class is like an object constructor, or a blueprint for creating objects.

# Create a class

class MyClass:
    x = 5

# Create object

p1 = MyClass()
print(p1.x)

# The __init__() function
'''
The examples above are classes and objects in their simples form, and are not really useful in real life applications.

To understandthe meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operationsthat are necessary to do when the object is being created.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the calss is being used to create a new object.

# The __str__() function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned.

# The string representationof an object without the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("John", 36)

print(p1)

# The string representation of an object with the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)

# Object methods
# Object can also contain methods. Methods in object are functions that belong to the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self parameter
# The self parameteris a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify object properties
# You can modify properties on objects like this:

p1.age = 40
print(p1.age)

# Delete object properties
# You can delete properties on objects by using the del keyword:

del p1.age
#print(p1.age) # Show a error.

# Delete objects
# You can delete objects by using the del keyword.

del p1

# The pass statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
    pass
