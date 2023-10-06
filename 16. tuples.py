# Tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Zack", 19, "male")

print(student.count("Zack")) # Counts how many times "Zack" was used
print(student.index("male")) # Shows which index the mentioned element is located in

for x in student: # Iterates all the elements
    print(x)

if "Zack" in student: # If the element is found then it will execute the block of code
    print("Miss ko na siya")