# SEABORN
# Visualize distributions with Seaborn

# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

# Install Seaborn
# If you have Python and PIP already installed on a system, install it using this command:

# pip install seaborn

# If you use Jupyter, install Seaborn using this command:

#!pip install seaborn

# Displots
# Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# Plotting a displot

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a displot without the histogram

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

# Note: We will be using: sns.displot(arr, kind="kde") to visualize random distributions in this tutorial.
