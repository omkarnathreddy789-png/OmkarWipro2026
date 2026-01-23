import requests
import json

# Public REST API (JSONPlaceholder)
API_URL = "https://jsonplaceholder.typicode.com/users"

# Custom headers
headers = {
    "User-Agent": "Python-Requests-Demo",
    "Accept": "application/json"
}

try:
    # 1. Send GET request with custom headers
    response = requests.get(API_URL, headers=headers, timeout=5)

    # 5. Handle HTTP errors
    response.raise_for_status()   # Raises exception for 4xx / 5xx errors

    # 3. Parse JSON response
    users = response.json()

    # Extract specific fields
    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

    # 4. Serialize and save to JSON file
    with open("users_data.json", "w", encoding="utf-8") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data successfully fetched and saved to users_data.json")

except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API")

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.RequestException as err:
    print("Unexpected error:", err)
