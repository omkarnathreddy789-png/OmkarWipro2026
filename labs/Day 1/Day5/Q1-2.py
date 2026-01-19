class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# Creating object of Car
c = Car()

# Calling inherited and own methods
c.start()
c.drive()
