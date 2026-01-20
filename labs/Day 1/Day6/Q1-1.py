import re

def check_employee_id(text):
    pattern = r'^EMP\d{3}'
    if re.match(pattern, text):
        print("Valid employee ID at the start of the string.")
    else:
        print("Invalid employee ID.")

check_employee_id("EMP123 is assigned to the project")
check_employee_id("EMP12 is invalid")
check_employee_id("ABCEMP123")
