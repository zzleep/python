import os

path = "C:\\Users\\96654\\Desktop\\folder"

if os.path.exists(path): # Checks the existence of the path
    print("That location exists!")
    if os.path.isfile(path): # Checks if the path is a file
        print("That is a file")
    elif os.path.isdir(path): # Checks if the path is a directory
        print("That is a directory!")
else:
    print("That location doesn't exist!")