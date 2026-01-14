import json

data = {
    "Name": "Ohmkar",
    "Age": "25",
    "Location": "Hyderabad",
    "Skills": ['C', 'Python']
}

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)