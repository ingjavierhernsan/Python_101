# FILE WRITE
# Write to an existing file
# To write to an existing file, you must add a parameter to the open() function:
# a - Append - will append to the end of the file.
# w - Write - will overwrite any existing content.

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

# Note: the w method will overwrite the entire file.

# Create a new file
# To create a new file in Python, use the open() method, with one of the following parameters:
# x - Create - Will create a file, returns an error if the file exists.
# a - Append - Will create a file if the specified file does not exists.
# w - Write - will create a file if hte specified file does not exists.

f = open("myfile.txt", "x")

# Result: a new empty file created!

# Create a new file if it does not exist:

f = open("myfile.txt", "w")
