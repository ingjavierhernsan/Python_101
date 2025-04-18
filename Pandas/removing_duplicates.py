# REMOVING DUPLICATES
# Discovering duplicates

# Duplicate rows that have been registered more than one time.

# By taking look at our test data set, we can assume that row 11 and 12 are duplicates.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

# Returns True for every row that is a duplicate, otherwise False:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())

# Removing duplicates
# To remove duplicates, use the drop_duplicates() method.

# Remove all duplicates:
df.drop_duplicates(inplace = True)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.


