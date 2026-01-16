class Student:
    name = ""
    roll_no = ""

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


student1 = Student()
student1.name = "Siddharth"
student1.roll_no = 201

student2 = Student()
student2.name = "Priya"
student2.roll_no = 202

student1.display_details()
print()
student2.display_details()
