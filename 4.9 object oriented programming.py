from car import Car

# You can assume objects by its attribute = is/has ex. name, age, height
# And methods = actions ex. eat, sleep, make Random shiz

# In order to construct a car, you need the following parameters
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()