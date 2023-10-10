# The child classes can inherit the parent class's attributes and functions and
# The child classes can have their own set of functions and modify what's within the parent function
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

# Rabbit is the child class and Animal is the parent class
# Rabbit will inherit what Animal class has
class Rabbit(Animal):

    def run(self):
        print("This rabbit is running.")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming.")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()