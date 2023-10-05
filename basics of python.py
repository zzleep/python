# Dahil special kayo naka summmarize na ang python course ni BroCode
# Video Reference: https://www.youtube.com/watch?v=XKHEtdqhLK8

# Variables - a container for a value and behaves as the value it contains

# Strings
first_name = "Anakin"
last_name = "Skywalker"

# Adding two variables to form a constructed variable
full_name = first_name + last_name
# However, if you want the two variables separate then...
# Just add " " in between with a plus symbol => full_name = first_name + " " + last_name

# Printing your variable/s value
print("Hello "+full_name)
# Printing your variable data type
# This will output as <class 'data type'>
print(type(full_name))

# Integers
age = 19
age += 1 # Simple arithmetic operation that increments by 1 using +=
print("Your age is: "+str(age))
# Note!! You cannot print out a string with a different variable so we added +str (as +data type) so that...
# You will be able to print it as a string and this is call "Type Casting"
print(type(age)) # Will still print out as an integer even though we used type casting

# Floating Point Numbers
height = 105.5
print(height)
print("Your height is: "+str(height)+"cm") # We use type casting again to print out the float number
print(type(height))

# Booleans
human = False
print("Are you a human? "+str(human)) # Will print out the boolean value
print(type(human))




