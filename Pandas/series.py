# SERIES
# What is a series?
# A Pandas series is like a column in a table.
# It is a one-dimensional array holding data of any type.

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

print(myvar[0])

# Create labels
# With the index argument, you can name your own labels.

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# When you have created labels, you can access an item by referring to the label.

print(myvar["y"])

# Key/Value Objects as Series
# You can also use a key/value objct, like a dictionary, when creating a series.

calories = {"day1":420, "day2":380, "day3":390}

myvar = pd.Series(calories)

print(myvar)

# Note: The keys of the dictionary become the labels.

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the series.

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

data = {
    "calories": [420, 380,390],
    "duration": [50,40,45]
}

myvar = pd.DataFrame(data)

print(myvar)
