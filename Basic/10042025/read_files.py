# FILE OPEN
# Open a file on the server
# Assume we have he following file, locate in the same folder as Python:

# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# If the file is located a different location, you will have to specify the file path, like this:

#f = open("D:\\myfiles\welcome.txt", "r")
#print(f.read())

# Read only parts of the file
# By default the read() method returns the whole text, butyou can also specify how many characters you wnat to return:

f = open("demofile.txt", "r")
print(f.read(5))

# Read lines
# You can return one line by using the readline() method:

f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() two times, you can read the twon first lines:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:

f = open("demofile.txt", "r")

for x in f:
    print(x)

# Close files
# It isa good practice to always close the file when you are done with it.

f = open("demofile.txt", "r")

print(f.readline())

f.close()

# Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.

