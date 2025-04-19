# NORMAL (GAUSSIAN) DISTRIBUTION

# Normal distribution
'''
The normal distribution is one of the most important distributions.

It is also called the Gaussian distribution after the German mathematician Carl Friedrich Gauss.

It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

Use the random.normal() method to get a Normal data distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.
scale - (Standard deviation) how flat the graph distribution should be.
size - The shape ofthe returned array.
'''

# Generate a random normal distribution of size 2x3:
from numpy import random

x = random.normal(size=(2, 3))

print(x)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# Visualization of normal distribution

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()

# Note: The curve of a normal distribution is also known as the bell curve because of the bell-shaped curve.
