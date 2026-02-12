

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["Company_DB"]      # use exact database name
collection = db["employees"]

print("Connected to MongoDB")


new_employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 45000
}

collection.insert_one(new_employee)
print("Employee inserted")


print("\nEmployees in IT Department:")
for emp in collection.find({"department": "IT"}):
    print(emp)


employee_name = "Rahul"

collection.update_one(
    {"name": employee_name},
    {"$set": {"salary": 50000}}
)

print("\nSalary updated for", employee_name)

# Close connection
client.close()
