# REGEX
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re

# RegEx in Python
# When you have imported the re module, you can start using regular expressions:

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# RegEx functions
# The re module offers a set of functions that allows us to search a string for a match:
'''
Function    Description
findall     Returns a list containing all matches.
search      Returns a Match object if there is a match anywhere in the string.
split       Returns a list where the string has been split at each match.
sub         Replaces one or many matches with a string.
'''

# Metacharacters
# ...

# Flags
# ...

# Special sequences
# ...

# Sets
# ...

# The findall() function
# The findall() function returns a list containing all matches.

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The list contains the matches in the order they are found. If no matches are found, an empty list is returned.

x = re.findall("Portugal", txt)
print(x)

# The search() function
# The search() function searches the string for a match, and returnsa Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned.

x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())

# If no matches are found, the value None is returned.

x = re.search("Portugal", txt)
print(x)

# The split() function
# The split() function returns a list where the string has been split at each match.

x = re.split("\s", txt)
print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:

x = re.split("\s", txt, 1)
print(x)

# The sub() function
# The sub() function replaces the matches with the text of your choice:

x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:

x = re.sub("\s", "9", txt, 2)
print(x)

# Match object
# A Match object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match object.

x = re.search("ai", txt)
print(x)

# The match object hasproperties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function.
# .group() returns the part of the string where there was a match.

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
x = re.search(r"\bS\w+", txt)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match object.
