# INHERITANCE
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a parent class
# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Create a child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", "Olse")
x.printname()

# Add the __init__() function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).

class Student(Person):
    def __init__(self, fname, lname):
        print("Hello")

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Use the super() function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(self, fname, lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add properties

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(self, fname, lname)
        self.graduationyear = 2019

# In the example below, the year 2019 should be a variable,and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(self, fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olse", 2019)

# Add methods

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(self, fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Add methods

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(self, fname, lname)
        self.graduationyear = year

def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# If you add a methodin the child class with the same name as a function in the parent class, the inheritance of the parent method will be overriden.

