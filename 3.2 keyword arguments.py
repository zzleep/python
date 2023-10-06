# keyword argument = arguments preceded by an identifier when we pass them to a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

# By adding an identifier you can choose which argument will be placed on the parameter desired
hello(last="Zackary", middle="D.", first="Luffy")
