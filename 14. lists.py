# List is used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

# print(food[0])

food.append("ice cream") # adds ice cream at the end
food.remove("hotdog") # removes hotdog
food.pop() # removes the last value eg. pudding
food.insert(0, "cake") # changes (index, value)
food.sort() # sorts the list alphabetically
food.clear() # removes every element in the list

for x in food:
    print(x)