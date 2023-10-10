class Animal:

    def eat(self):
        print("This animal is eating.")

class Rabbit(Animal):
# Basically, what you're doing is changing the original function from the parent class and modifying it in the child class
    def eat(self):
        print("This rabbit is eating a carrot.")


rabbit = Rabbit()
rabbit.eat()
