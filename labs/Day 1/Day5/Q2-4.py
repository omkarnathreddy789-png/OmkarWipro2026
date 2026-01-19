# Base class
class Calculator:
    def calculate(self, a, b):
        print("Calculator: Sum =", a + b)

# Derived class 1
class ScientificCalculator(Calculator):
    def calculate(self, a, b):
        print("ScientificCalculator: Product =", a * b)

# Derived class 2
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvancedCalculator: Difference =", a - b)


# Demonstrating polymorphism
calculators = [Calculator(), ScientificCalculator(), AdvancedCalculator()]

for calc in calculators:
    calc.calculate(10, 5)
