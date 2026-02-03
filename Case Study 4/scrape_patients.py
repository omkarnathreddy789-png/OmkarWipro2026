import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:5000/patients")
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    print({
        "name": cols[0].text,
        "age": cols[1].text,
        "disease": cols[2].text,
        "doctor": cols[3].text
    })
