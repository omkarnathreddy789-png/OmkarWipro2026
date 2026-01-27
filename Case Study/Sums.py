import json
import csv
from abc import ABC, abstractmethod


class MarksValidator:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if all(0 <= mark <= 100 for mark in value):
            setattr(obj, self.private_name, value)
        else:
            raise ValueError("Marks should be between 0 and 100")

# ------------------------ Base Classes ------------------------
class Person(ABC):
    def __init__(self, person_id, name, department):
        self.id = person_id
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    marks = MarksValidator()
    def __init__(self, student_id, name, department, semester, marks):
        super().__init__(student_id, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        return f"Name: {self.name}, Role: Student, Dept: {self.department}"

    def calculate_performance(self):
        avg = sum(self.marks)/len(self.marks)
        grade = self._get_grade(avg)
        return avg, grade

    def _get_grade(self, avg):
        if avg >= 85: return 'A'
        if avg >= 70: return 'B'
        if avg >= 50: return 'C'
        return 'D'

    def __gt__(self, other):
        return sum(self.marks)/len(self.marks) > sum(other.marks)/len(other.marks)

class Faculty(Person):
    def __init__(self, faculty_id, name, department, salary):
        super().__init__(faculty_id, name, department)
        self._salary = salary

    def get_details(self):
        return f"Name: {self.name}, Role: Faculty, Dept: {self.department}"

    @property
    def salary(self):
        raise PermissionError("Salary is confidential")

# ------------------------ Course ------------------------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __str__(self):
        return f"{self.name} ({self.code})"

    def __add__(self, other):
        return self.credits + other.credits

# ------------------------ University System ------------------------
class UniversityManagementSystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.courses = []

    # ---------- Add Student ----------
    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            print("Error: Student ID already exists"); return
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    # ---------- Add Faculty ----------
    def add_faculty(self, faculty):
        if any(f.id == faculty.id for f in self.faculty):
            print("Error: Faculty ID already exists"); return
        self.faculty.append(faculty)
        print(f"Faculty {faculty.name} added successfully!")

    # ---------- Add Course ----------
    def add_course(self, course):
        if any(c.code == course.code for c in self.courses):
            print("Error: Course Code already exists"); return
        self.courses.append(course)
        print(f"Course {course.name} added successfully!")

    # ---------- Enroll ----------
    def enroll_student(self, student_id, course_code):
        student = next((s for s in self.students if s.id==student_id), None)
        course = next((c for c in self.courses if c.code==course_code), None)
        if not student or not course:
            print("Error: Student or Course not found"); return
        student.courses.append(course)
        print(f"{student.name} enrolled in {course.name} successfully!")

    # ---------- Performance ----------
    def calculate_student_performance(self, student_id):
        student = next((s for s in self.students if s.id==student_id), None)
        if not student: print("Error: Student not found"); return
        avg, grade = student.calculate_performance()
        print(f"{student.name} Performance → Average: {avg:.2f}, Grade: {grade}")

    # ---------- Compare Students ----------
    def compare_students(self, id1, id2):
        s1 = next((s for s in self.students if s.id==id1), None)
        s2 = next((s for s in self.students if s.id==id2), None)
        if not s1 or not s2: print("Error: Student not found"); return
        print(f"{s1.name} > {s2.name}: {s1 > s2}")

    # ---------- Generate Reports ----------
    def generate_reports(self):
        # Save CSV
        try:
            with open("students_report.csv","w",newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID","Name","Dept","Average","Grade"])
                for s in self.students:
                    avg, grade = s.calculate_performance()
                    writer.writerow([s.id,s.name,s.department,avg,grade])
            print("CSV report saved!")
        except PermissionError:
            print("Error: Close students_report.csv if open!")

        # Save JSON
        try:
            data = [{"id":s.id,"name":s.name,"department":s.department,"semester":s.semester,"marks":s.marks} for s in self.students]
            with open("students.json","w") as f:
                json.dump(data,f,indent=4)
            print("JSON file saved!")
        except PermissionError:
            print("Error: Cannot write students.json!")

    # ---------- Display Students ----------
    def display_students(self):
        print("Student Records:")
        for s in self.students:
            print(f"{s.id} - {s.name}")

# ------------------------ Menu ------------------------
def main():
    ums = UniversityManagementSystem()
    while True:
        print("\n--- Smart University Management ---")
        print("1 → Add Student\n2 → Add Faculty\n3 → Add Course")
        print("4 → Enroll Student\n5 → Performance\n6 → Compare Students")
        print("7 → Generate Reports\n8 → Display Students\n9 → Exit")
        choice = input("Choice: ")

        if choice=="1":
            try:
                sid=input("Student ID: "); name=input("Name: ")
                dept=input("Department: "); sem=int(input("Semester: "))
                marks=list(map(int,input("Marks (5 subjects): ").split()))
                ums.add_student(Student(sid,name,dept,sem,marks))
            except Exception as e: print("Error:",e)

        elif choice=="2":
            try:
                fid=input("Faculty ID: "); name=input("Name: ")
                dept=input("Department: "); sal=float(input("Salary: "))
                ums.add_faculty(Faculty(fid,name,dept,sal))
            except Exception as e: print("Error:",e)

        elif choice=="3":
            try:
                code=input("Course Code: "); name=input("Course Name: ")
                credits=int(input("Credits: ")); fid=input("Faculty ID: ")
                fac=next((f for f in ums.faculty if f.id==fid),None)
                if not fac: print("Faculty not found"); continue
                ums.add_course(Course(code,name,credits,fac))
            except Exception as e: print("Error:",e)

        elif choice=="4":
            ums.enroll_student(input("Student ID: "),input("Course Code: "))

        elif choice=="5":
            ums.calculate_student_performance(input("Student ID: "))

        elif choice=="6":
            ums.compare_students(input("Student 1 ID: "),input("Student 2 ID: "))

        elif choice=="7":
            ums.generate_reports()

        elif choice=="8":
            ums.display_students()

        elif choice=="9":
            print("Exiting..."); break

        else: print("Invalid choice!")

if __name__=="__main__":
    main()
