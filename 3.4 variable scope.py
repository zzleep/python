# scope = The region that a variable is recognized
#         A variable is only available from the inside the region it is created.
#         A global and locally scoped versions of a variable can be created.s

name = "Zayn" # global scope/variable (available inside and outside functions)

def display_name():
    name = "David" # local scope/variable (available only inside this function)
    print(name)

# print(name) -> this will not work because it is outside of the function and name will not be determined

display_name()
print(name)

# Remember that python follows this:
# L = Local

# E = Enclosing
# G = Global
# B = Built-in