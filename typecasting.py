# Type casting is a way to convert the data type of a value to another data type

x = 1 # int
y = 2.0 #float
z = "3" #str

# In order to convert a value data type into another data type, you must:
# datatype(y)

x = float(x)
y = int(y) # Will convert the actual variable without performing typecasting on the print function
z = int(z) # Converts the string into an int so that it can perform a mathematics operation

print(x)   # Converting the int > float will allow the variable to have a decimal point
print(y)   # The float will lose its decimal point because of the float > int conversion
print(z*3)

z = str(z) # Conversion of int > string
print(z*3) # Will print out the string 3 times instead of multiplying the value by 3
           # Strings cannot be performed to do a mathematical operation or equation

# When should you use typecasting?
# When you normally print out strings, you cannot add a different data type like an int alongside it since...
# We are using a string concatenation

print("X is "+str(x))
print("Y is "+str(y))