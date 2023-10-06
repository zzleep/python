# Nested loops = The "inner loop" will finish all of its iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("How manu rows?: "))
columns = int(input("How manu columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # Added end="" to avoid cursor going to next line
    print()
