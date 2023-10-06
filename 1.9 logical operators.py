# Logical operators (and, or, not) are used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go Outside!")

# With the not logical operator you can surround one or more conditional statements with the not logical operator
# This acts as similar to != in C languages
# All it does is flip true to false and false to true

