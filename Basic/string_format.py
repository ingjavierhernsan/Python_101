# F-Strings
'''
F-String was introduced in Python 3.6, and is noew the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
'''

age = 36
txt = f"My name is John, I am {age}"

print(txt)

price = 59
txt = f"The price is {price} dollars"

print(txt)

txt = f"The price is {price:.2f} dollars"

print(txt)

txt = f"The price is {20 * 59} dollars"

print(txt)