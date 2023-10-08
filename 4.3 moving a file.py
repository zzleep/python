import os

source = "text.txt" # You can also move folders
destination = "C:\\Users\\96654\\Desktop\\testing.txt"

try:
    if os.path.exists(destination): # Checks if the file already exists in the destination
        print("There is already a file there")
    else:
        os.replace(source,destination) # Moves the file to the destination if it does not exist
        print(source+" was moved.")
except FileNotFoundError: # Exception handling
    print(source+" was not found.")