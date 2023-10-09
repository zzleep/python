from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

# You can change the default amount
Car.wheels = 2
car_1.wheels = 6

print(Car.wheels)
print(car_1.wheels)