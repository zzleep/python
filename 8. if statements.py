# if statements are a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

# This is very simple to understand and always remember that the order of your if statements matter when executing conditions
# Use elif after if statement