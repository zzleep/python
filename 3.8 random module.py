import random

# Making a pseudo-random program

# Getting a random number from n to n
x = random.randint(1,6)
# Gives a random number between 0 and 1
y = random.random()

# Chooses a random choice from the list
myList = ['rock','paper','scissors']
z = random.choice(myList)

# Shuffles a list/tuple/dictionary/etc
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)