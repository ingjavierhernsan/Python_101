# JSON
# JSON is a syntax for storing and exchanging data. JSON is text, written with JavaScript object notation.

# JSON in Python
# Python hasa built-in package called json, which can be used to work with JSON data.

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.

x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)

# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, True, False, None

print(json.dumps({"name":"John", "age":30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON equivalent:
'''
Python      JSON
dict        Object
list        Array
tuple       Array
str         String
int         Number
float       Number
True        true
False       false
None        null
'''

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# Format the result
# The example above prints a JSON string, but it not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result.

print(json.dumps(x, indent=4))

# You can also define the separators, default value is (",",":"), which means using a comma and a space to separate each object, and a colon and a space to separate each object, and a colon and a space to separate keys from values.

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the result
# The json.dumps() method has parameters to order the keys in the result:

print(json.dumps(x, indent=4, sort_keys=True))
