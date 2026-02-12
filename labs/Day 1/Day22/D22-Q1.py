import mysql.connector

host = "localhost"
user = "root"
password = "root@2026"
database = "feb2026"

# ----- Connect -----
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
print("connected to the database successfully")

# Fetch employees with Salary > 50000
print("\nEmployees with salary > 50000")
select_query = "SELECT * FROM employee WHERE `Salary` > %s"
cursor.execute(select_query, (50000,))
for row in cursor.fetchall():
    print(row)

# Insert new employee  (FIXED: include Employee no)
insert_query = """
INSERT INTO employee (`Employee no`, `Employee Name`, `Salary`)
VALUES (%s, %s, %s)
"""

new_employee = (3, "Kumar", 60000)   # give new ID manually
cursor.execute(insert_query, new_employee)
conn.commit()
print("\nNew employee inserted successfully")

# Update salary by 10%
employee_id = 1
update_query = """
UPDATE employee
SET `Salary` = `Salary` * 1.10
WHERE `Employee no` = %s
"""
cursor.execute(update_query, (employee_id,))
conn.commit()
print("Salary updated by 10%")

# Show updated table
print("\nUpdated Employee Table:")
cursor.execute("SELECT * FROM employee")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
print("\nDatabase connection closed")
