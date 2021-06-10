# Files and Directories
# To print all files in the given directory
# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# ===================================================================
# # First Way to Read File
# file = open('Day24/file.txt')
# # Reading the the Content of File
# contents = file.read()
# # printing Content of File
# print(contents)
# # Close the file when we are done
# file.close()

# Second Way to Read File
# Using with keyword in this case no need to close the file

# with open('Day24/file.txt') as file:
#     # reading file
#     contents = file.read()
#     print(contents)

# When We want to write in a file then we need to pass mode 
# Note: w for write
#       r for read(default)
#       a for append

with open('Day24/file.txt', mode="w"):
    # read file
    contents= file.read()
    # write in file
    file.write("File Writing Done")

# Using Append Mode Instead of Write Mode
with open('Day24/file.txt', mode="a") as file:
    # write in file
    file.write("File Appending Done")

# Difference Betweeen Write and Append Mode
  # When we use write mode it clears all pre-exisiting data and writes to it
  # While append mode keeps all pre-exisiting data and writes to the end of file