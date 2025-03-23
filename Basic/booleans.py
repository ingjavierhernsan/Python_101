# Booleans represent one of two values: True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print(bool(None))
print(bool(0))
print(bool(""))

'''
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
