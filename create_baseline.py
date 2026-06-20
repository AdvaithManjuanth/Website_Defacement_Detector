from config import URL
import requests
from bs4 import BeautifulSoup
import hashlib

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.get_text()

website_hash = hashlib.sha256(content.encode()).hexdigest()

with open("baseline.txt", "w") as file:
    file.write(website_hash)

print("Baseline Created")