# GETTING STARTED
# Installation of Pandas
# If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
# Install it using this command:

# pip install pandas

# Import Pandas
# Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas

mydataset = {
    'cars' : ["BMW","Volvo", "Ford"],
    'passings' : [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

# Pandas as pd
# Pandas is usually imported under the pd alias.

import pandas as pd

myvar = pd.DataFrame(mydataset)

print(myvar)

# Checking Pandas version
# The version string is stored under __version__ attribute.

print(pd.__version__)

