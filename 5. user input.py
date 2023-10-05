# User Input

# We accept input in python using the input function
name = input("What is your name: ") # We assigned a variables value into our input function
age = int(input("How old are you? ")) # Assign the data type you would like to use and encase the existing input
height = float(input("How tall are you? ")) # Just like the int variable

age = age + 1 # or age += 1

print("Hello "+name) # Always note that we can only print out string data types alongside another string data type
print("You are "+str(age)+" years old.") # Don't forget to typecast!!
print("You are "+str(height)+"cm tall")
