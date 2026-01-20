import re

text = "You can reach me at test123@gmail.com for details."

pattern = r'\S+@\S+\.\S+'

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found")
