import requests

BASE_URL = "https://api.restful-api.dev/objects"

# ---------- POST ----------
post_body = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

post_response = requests.post(BASE_URL, json=post_body)
print("POST:", post_response.status_code)
post_data = post_response.json()
print(post_data)

# Capture correct ID
object_id = post_data["id"]

# ---------- PUT ----------
put_url = f"{BASE_URL}/{object_id}"
put_body = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}

put_response = requests.put(put_url, json=put_body)
print("PUT:", put_response.status_code)
print(put_response.json())

# ---------- PATCH ----------
patch_body = {
    "name": "Apple MacBook Pro 16 (Updated Name)"
}

patch_response = requests.patch(put_url, json=patch_body)
print("PATCH:", patch_response.status_code)
print(patch_response.json())

# ---------- DELETE ----------
delete_response = requests.delete(put_url)
print("DELETE:", delete_response.status_code)
print(delete_response.json())
