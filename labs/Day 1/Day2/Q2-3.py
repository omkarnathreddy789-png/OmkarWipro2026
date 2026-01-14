class PositiveSalary:
    def __init__(self):
        self._salaries = {}  # store salary per instance

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._salaries.get(id(instance), 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary must be positive")
        self._salaries[id(instance)] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Creating multiple employees
emp1 = Employee("Omkar", 28000)
emp2 = Employee("Reddy", 27500)
emp3 = Employee("Sunny", 25000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
print(emp3.name, emp3.salary)

# Uncommenting next line will raise error
# emp2.salary = -5000
