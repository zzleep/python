import os
import shutil

path = "test.txt"

try:
    # os.remove(path)     # Deletes a file
    # os.rmdir(path)      # Deletes a directory
    shutil.rmtree(path)   # Deletes a directory containing files
except FileNotFoundError: # Checks if file exists
    print("That file was not found")
except PermissionError: # Checks if you have enough user permissions to delete
    print("You do not have permission to delete that")
except OSError: # Checks if the directory contains files
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")