# DATAFRAMES
# What is a DataFrame?
# A Pandas DataFram is a 2 dimensional data structure, like a 2 dimensional array, or atable with rows and columns.

import pandas as pd

data = {
    "calories": [420, 380,390],
    "duration": [50,40,45]
}

df = pd.DataFrame(data)

print(df)

# Locate row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s).

print(df.loc[0])

# Note: This example returns a Pandas series.

print(df.loc[[0, 1]])

# Note: When using [], the resultis a Pandas DataFrame.

# Name indexes
# With the index argument, you can name your own indexes.

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

# Locate Named indexes
# Use the named index in the loc attribute to return the specified row(s).

print(df.loc["day2"])

# Load files into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

df = pd.read_csv('data.csv')

print(df)
