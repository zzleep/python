# kwargs = parameter that will pack all arguments into a dictionary
#          useful so that a function can accept a varying amount of keyword argument
#          kwargs is also a short term for keyword arguments

def hello(**kwargs): # Same as args, you can change the name as long as you have the double asterisk
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ") # Add end=" " to make it print on the same line

hello(title="Sir",first="Zack",middle="FF",last="Fair")