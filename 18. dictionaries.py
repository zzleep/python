# Dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}


# You can change the values while the program is running
capitals.update({'Germany':'Berlin'})
# Overwrites the previous value with a different one
capitals.update({'USA':'Las Vegas'})

# Removes the key value pair from the dictionary
capitals.pop('China')

# Clears the whole Dictionary
capitals.clear()

# This code will not work because it does not exist in the dictionary
# print(capitals['Germany'])
# You can use this one v to avoid the one above ^
# print(capitals.get('Germany'))

# Only prints the keys
# print(capitals.keys())

# Only prints the values
# print(capitals.values())

# Prints both the keys and values
# print(capitals.items())

for key,value in capitals.items():
    print(key, value)