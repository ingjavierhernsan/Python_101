# Python conditions and if statements
'''
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

# If statement
a = 33
b = 200

if b > a:
    print("b is greater than a")

# Identation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# Elif
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Also
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# Short hand if
if a > b: print ("a is greater than b")

# Short hand if ... else
a = 2
b = 330
print("A") if a > b else print("B")

# This technique is kwon as Ternary operators, or Conditional expressions.

# You can also have multiple else statements on the same line:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
a = 200
b = 33
c = 500
if a > b or c > a:
    print("At least one of the conditions are True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested if
x = 41
if x > 10:
    print("Above then, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass statement
# if statement cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass
