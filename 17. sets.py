# Set is a collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# Add napkin to the set
utensils.add("napkin")

# Removes fork from the set
utensils.remove("fork")

# All elements within the set gets cleared
utensils.clear()

# Adds all the elements within the dishes set to the utensils set
utensils.update(dishes)

# Creates a different set with the combination of two other sets
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

# Comparison of different sets
# Shows what utensils has that dishes doesn't
print(utensils.difference(dishes))

# Shows which elements they have in common
print(utensils.intersection(dishes))