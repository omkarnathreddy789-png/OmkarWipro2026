from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print(self.name,"Salary is 40000")


m=Manager("Reddy")
m.salary()