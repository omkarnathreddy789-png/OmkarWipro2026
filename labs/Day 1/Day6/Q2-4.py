import re

# Without re.IGNORECASE
print(re.search(r'python', "Python").group() if re.search(r'python', "Python") else "No match")

# With re.IGNORECASE
print(re.search(r'python', "Python", re.IGNORECASE).group())

# Without re.MULTILINE
text = "Cat\nDog\nCat"
print(re.findall(r'^Cat', text))

# With re.MULTILINE
print(re.findall(r'^Cat', text, re.MULTILINE))

# Without re.DOTALL
print(re.search(r'Cat.*Cat', text))

# With re.DOTALL
print(re.search(r'Cat.*Cat', text, re.DOTALL).group())
