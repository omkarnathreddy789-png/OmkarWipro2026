class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
s1 = Student("Ohmkar", 101)
s2 = Student("Reddy", 102)

s1.display_details()
print()
s2.display_details()

