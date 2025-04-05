# UNPACKING A TUPLE
# When we create a tuple, we normally assign values to it. This called packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called unpacking:
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# USING ASTERISK
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

