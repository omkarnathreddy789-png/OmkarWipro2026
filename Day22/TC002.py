from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Company_DB"]
collection = db["employees"]

print("Connected to MongoDB")

# New employee document
new_employee = {
    "name": "Kiran",
    "dep": "IT",
    "course": "Java",
    "salary": 32000
}

collection.insert_one(new_employee)

print("Another employee inserted successfully")

# Show all employees
for emp in collection.find():
    print(emp)

client.close()
