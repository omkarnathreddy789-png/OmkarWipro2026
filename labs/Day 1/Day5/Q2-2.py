# Base class
class Calculator:
    def calculate(self, a, b):
        print("Base Calculator: Sum =", a + b)

# First derived class overrides calculate
class ScientificCalculator(Calculator):
    def calculate(self, a, b):
        print("Scientific Calculator: Product =", a * b)

# Second derived class overrides calculate
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("Advanced Calculator: Difference =", a - b)


# Creating objects
base_calc = Calculator()
sci_calc = ScientificCalculator()
adv_calc = AdvancedCalculator()

# Calling methods
base_calc.calculate(10, 5)   # Base class method
sci_calc.calculate(10, 5)    # Overridden in ScientificCalculator
adv_calc.calculate(10, 5)    # Overridden in AdvancedCalculator
