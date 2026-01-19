class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

# List of objects
obj = [Dog(), Cat()]

# Loop through objects and call sound()
for a in obj:
    a.sound()
