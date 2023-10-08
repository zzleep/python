# In order to avoid exception errors, you must apply the try and except functions
try:
    with open('C:\\Users\\96654\\Desktop\\test.tx') as file:
        print(file.read())
except FileNotFoundError: # If file does not exist
    print("That file was not found :(")
