# Base class
class Calculator:
    def calculate(self, a, b):
        print("Base Calculator: Sum =", a + b)

# Derived class overrides the calculate method
class ScientificCalculator(Calculator):
    def calculate(self, a, b):
        print("Scientific Calculator: Product =", a * b)


# Creating objects
calc1 = Calculator()
calc2 = ScientificCalculator()

# Calling methods
calc1.calculate(5, 3)
calc2.calculate(5, 3)
