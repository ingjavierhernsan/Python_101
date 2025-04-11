# DELETE FILE
# Delete a file 
# To delete a file, you must import the OS module, and run its os.remove() function:

import os

os.remove("demofile2.txt")

# Check if file exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete folder
# To delete an entire folder, use the os.rmdir() method:

os.rmdir("myfolder")

# Note: You can only remove empty folders.
