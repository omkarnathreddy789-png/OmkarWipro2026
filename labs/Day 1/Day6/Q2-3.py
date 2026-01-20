import re

# re.IGNORECASE
text1 = "Hello World"
print(re.search(r'hello', text1, re.IGNORECASE).group())

# re.MULTILINE
text2 = "One\nTwo\nThree"
print(re.findall(r'^T\w+', text2, re.MULTILINE))

# re.DOTALL
text3 = "Start\nEnd"
print(re.search(r'Start.*End', text3, re.DOTALL).group())
