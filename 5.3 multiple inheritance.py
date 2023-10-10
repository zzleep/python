# multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal is fleeing.")


class Predator:

    def hunt(self):
        print("This animal is hunting.")

# Rabbit only inherits from the Prey class
class Rabbit(Prey):
    pass

# Hawk only inherits from the Predator class
class Hawk(Predator):
    pass

# Fish inherits from both Prey and Predator class
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()