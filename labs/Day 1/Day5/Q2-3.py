# Custom class
class Number:
    def __init__(self, value):
        self.value = value

    # Overloading the + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    # To display object nicely
    def display(self):
        print("Value =", self.value)


# Creating objects
num1 = Number(10)
num2 = Number(20)

# Adding objects using overloaded +
num3 = num1 + num2

# Displaying results
num1.display()
num2.display()
num3.display()
