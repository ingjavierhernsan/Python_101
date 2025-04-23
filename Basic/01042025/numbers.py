# There are three numeric types in Pytho:
# int
# float
# complex

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

print("\n")
print("Integer")

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("\n")
print("Float")

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.73100

print(type(x))
print(type(y))
print(type(z))

print("\n")
print("Complex")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type conversion
print("\n")
print("Convert")

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))