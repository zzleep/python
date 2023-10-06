import time

# for loop = a statement that will execute it's block of code
#          = a limited amount of times
#
#          while loop = unlimited
#          for loop = limited

for i in range(10): # Counts from 0
    print(i+1) # Incrementing by 1 will start the number from 1

for i in range(50,100+1,2): # Still follows the argument from slice (start:stop:step)
    print(i)                # Skips by 2

for i in "Bro Code": # Prints each letter
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
