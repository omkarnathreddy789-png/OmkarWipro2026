import requests

BASE_URL = "http://127.0.0.1:5000"

# ---- Check server first ----
try:
    requests.get(BASE_URL, timeout=3)
except requests.exceptions.ConnectionError:
    print("❌ Flask server is NOT running. Start app.py first.")
    exit()

# Home
r = requests.get(BASE_URL)
print(r.text)

# Get all users
r1 = requests.get(f"{BASE_URL}/users")
print(r1.status_code, r1.json())

# Get single user
r2 = requests.get(f"{BASE_URL}/users/1")
print(r2.status_code, r2.json())

# Create user
r3 = requests.post(f"{BASE_URL}/users", json={"name": "Lee"})
print(r3.status_code, r3.json())

# 🔑 Capture correct ID
user_id = r3.json()["id"]

# PUT
r4 = requests.put(f"{BASE_URL}/users/{user_id}", json={"name": "sid"})
print(r4.status_code, r4.json())

# PATCH
r5 = requests.patch(f"{BASE_URL}/users/{user_id}", json={"name": "Lee"})
print(r5.status_code, r5.json())

# DELETE
r6 = requests.delete(f"{BASE_URL}/users/{user_id}")
print(r6.status_code, r6.json())

