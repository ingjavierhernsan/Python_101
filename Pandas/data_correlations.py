# DATA CORRELATIONS
# Finding relationships

# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.
# The examples in this page uses a CSV file called: 'data.csv'

import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())

# Note: The corr() method ignores "not numeric" columns.

# Result explained
# The result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

# The number varies from -1 to 1.

# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
# 0.2 means not a good relationship, meaning that if one value goes up does not mean that the other will.

# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

# Perfect correlation:
# We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relatiionship with itself.

# Good correlation:
# "Duration" and "Calories" got a 0.922721 correlation, which is a very good correlacion, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

# Bad correlation:
# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work, and vice versa.
