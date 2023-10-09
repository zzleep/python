class Car: # Common naming convention always starts with the first letter being capitalized

    # Class variables are inside the class but outside the constructor
    wheels = 4 # Class variable

    # Special method that creates objects for us. This is also called as a constructor
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")