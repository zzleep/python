# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args): # *args can be any name as long as you have the asterisk
    sum = 0
    args = list(args) # if you want to modify a specific number in the parameter then cast it to the corresponding type
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))