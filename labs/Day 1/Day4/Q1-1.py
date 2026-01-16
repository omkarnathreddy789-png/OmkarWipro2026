class Student:
    name = ""
    roll_no = ""

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


s1 = Student()
s1.name = "ROHIT"
s1.roll_no = "001"

s2 = Student()
s2.name = "VIRAT"
s2.roll_no = "002"

s1.display_details()
print()
s2.display_details()
