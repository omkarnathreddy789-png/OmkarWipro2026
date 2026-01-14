class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # For now, no checks

# Example usage
e1 = Employee("Reddy", 35000)
print(e1.name, e1.salary)
