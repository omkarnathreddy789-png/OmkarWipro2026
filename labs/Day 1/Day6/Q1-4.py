import re

text = "Employee ID: EMP123"

pattern = r'(EMP)(\d{3})'
match = re.search(pattern, text)

if match:
    print("Full match:", match.group(0))
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
