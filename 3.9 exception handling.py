# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: # as e serves as a placeholder for the exception error
    print(e) # prints out the error
    print("You can't divide by zero! Dummy!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result) # Will only execute if there are no errors
finally: # Whether we catch an exception it will execute the block of code, always at the end!
    print("This will always execute")