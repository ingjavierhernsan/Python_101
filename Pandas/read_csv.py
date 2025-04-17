# READ CSV
# Read CSV Files

# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contiains plain text and is a well know format that can be read by everyone including Pandas.
# In our examples we eill be using a CSV file called 'data.csv'.

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

# Tip: use to_string() to print the entire DataFrame.

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

print(df)

# max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check you system's maximum rows with the pd.options.display.max_rows statement.

print(pd.options.display.max_rows)

# You can change the maximum rows number with the same statement.

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)
