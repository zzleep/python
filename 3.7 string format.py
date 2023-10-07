# str.format = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
# More elegant method of writing the same code above
print("The {} jumped over the {}".format(animal,item))
# THe curly braces are called format fields and acts as a placeholder for a value or variable
print("The {1} jumped over the {0}".format(animal,item)) # Positional arguments
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon")) # Keyword argument
# You can reuse the arguments in the same statements

# More elegant way of doing this:
text = "The {} jumped over the {}"
print(text.format(animal,item))

# Adding a padding using the format method

name = "Chopper"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # Allocating 10 spaces for your line
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # Left align
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Right align
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Center align

# Formattz`ing numbers

number = 3.14159
number2 = 1000

# Displaying only the first 2 digits after the decimal point
print("The number pi is {:.2f}".format(number)) # Meaning .2 floating point
print("The number pi is {:,}".format(number2)) # Adds a comma for every thousand places
print("The number pi is {:b}".format(number2)) # Displays the binary representation of your number
print("The number pi is {:o}".format(number2)) # Displays the octal representation of your number
print("The number pi is {:x}".format(number2)) # Displays the hexadecimal representation of your number
                                               # (x for lowercase, X for uppercase)
print("The number pi is {:e}".format(number))# Displays the scientific notation of your number
                                               # (e for lowercase, E for uppercase)

