import re


def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

    if re.match(pattern, password):
        print("Strong password")
    else:
        print("Weak password")



validate_password("Pass@123")
validate_password("password")
