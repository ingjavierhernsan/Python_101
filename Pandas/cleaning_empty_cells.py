# CLEANING EMPTY CELLS
# Empty cells

# Empty cells can potentially give you a wrong result when you analyze data.

# Remove rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the orginal DataFrame.

# Replace empty values
# Another way of dealing with empty cells is to insert a new value instead.
# The fillna() method allows us to replace empty cells with a value:

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# Replace only for specified columns
# The example above replaces all empty cells in the whole Data frame.
# To only replace empty values for one column, specify the column name for the DataFrame:

df = pd.read_csv('data.csv')

df.fillna({"Calories":130}, inplace = True)

print(df.to_string())

# Replace using mean, median or mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean(), median() and model() methods to calculate the respective values for a specified column:

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

# Mean = the average value (the sum of all values divided by number of values).

# Calculate the MEDIAN, and replace any empty values with it:

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

# Median = the value in the middle, after you have sorted all values ascending.

# Calculate the MODE, and replace any empty values with it:

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

# Mode = the value that appears most frequently.
