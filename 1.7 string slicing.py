# String slicing is used to create a substring by extracting elements from another string
# Indexing[] or slice()
# [start:stop:step] 3 Arguments to use for indexing

name = "Tyler Johnson"

# Always remember that start is inclusive and stopping is exclusive!!
first_name = name[0:6] # First letter is always index 0 and always add 1 for stopping
                       # Short Hand way for doing this is: name[:6]
last_name = name[6:14] # Starts from after the first name then proceeds to take the second name
                       # Short Hand way for doing this is: name[6:]
funky_name = name[0:14:2] # Will print out every second character because the value of step is 2
                          # Short Hand way for doing this is: name[::2]
reversed_name = name[::-1] # Reversing a string

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # Remember that the first value is inclusive and the second value is exclusive
                    # This will only take "google" without http and .com
                    # With this, you can use a combination of positive and negative values for slicing

print(website1[slice])
print(website2[slice])

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
