# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ") # Will continue to ask for your name if its left blank
    if name != "":
        break

phone_number = "135-125-1215"

for i in phone_number: # Removes the dash from the phone number
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):

    if i == 13: # If 13 is found in the loop, the pass function will skip the number designated.
        pass
    else:
        print(i)
