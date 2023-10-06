# while loop is a statement that will execute its block of code as long as it's condition remains true

name = None # name = ""

# while len(name) == 0:
#   name = input("Enter your name: ")

# Another way to do this is:
# Will continue to ask the user if name is blank
while not name:
    name = input("Enter your name: ")

print("Hello "+name)
