# Index operator [] = gives access to a sequence's element (str,list,tuples)

name = "jidey Sakalam!"

if(name[0].islower()):
    name = name.capitalize()

# Takes the first name starting from index 0 to index 5 and making it all uppercase
first_name = name[:5].upper()

# Takes the last name starting from index 6 to the last index and making it all lowercase
last_name = name[6:].lower()

# With the use of negative indexing, you can start from the end
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
