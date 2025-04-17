# ANALYZING DATAFRAMES
# Viewing the data

# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

print(df.head())

# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail())

# Info about the data
# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info())

# Result explained
# The result tells us there are 169 rows and 4 columns. And the name of each column, with the data type.

# Null values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning dara, and you will learn more about that in the next chapters.
