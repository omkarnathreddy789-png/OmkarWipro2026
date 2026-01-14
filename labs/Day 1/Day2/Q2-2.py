class PositiveSalary:
    def __init__(self):
        self._salary = 0

    def __get__(self, instance, owner):
        return self._salary

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary must be positive")
        self._salary = value

class Employee:
    salary = PositiveSalary()  # Descriptor used here

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Will trigger descriptor

e1 = Employee("Omkar", 35000)
print(e1.name, e1.salary)

# e2 = Employee("Bob", -1000)  # This will raise ValueError
