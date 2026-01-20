import re

text = "Pass@123"

pattern = r'(?=.*[A-Z])(?=.*\d)'

if re.search(pattern, text):
    print("Lookahead condition satisfied")
else:
    print("Condition not satisfied")
