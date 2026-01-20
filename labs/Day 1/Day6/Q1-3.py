import re

text = "User1 age 25"

# .  → any character
print(re.search(r'U.er1', text).group())

# \d+ → one or more digits
print(re.search(r'\d+', text).group())

# \w+ → word characters
print(re.search(r'\w+', text).group())

# \s → whitespace
print(re.search(r'\s', text).group())

# * → zero or more occurrences
print(re.search(r'a*ge', text).group())

# ? → zero or one occurrence
print(re.search(r'Use?r1', text).group())
