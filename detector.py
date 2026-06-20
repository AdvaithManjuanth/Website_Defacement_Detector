from config import URL
import requests
from bs4 import BeautifulSoup
import hashlib
import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


SENDER_EMAIL = "ADD SENDER EMAIL ID"
APP_PASSWORD = "ADD SENDER Gmail app password"

RECEIVER_EMAIL = "ADD RECIVER EMAIL ID"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

current_content = soup.get_text()

current_hash = hashlib.sha256(current_content.encode()).hexdigest()

with open("baseline.txt", "r") as file:
    saved_hash = file.read()

if current_hash == saved_hash:
    status = "Website Safe"
else:
    status = "WARNING! Website Changed"

    msg = MIMEText("Possible Website Defacement Detected")

    msg["Subject"] = "Website Defacement Alert"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(SENDER_EMAIL, APP_PASSWORD)

    server.send_message(msg)

    server.quit()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
    timestamp TEXT
)
""")

cursor.execute(
    "INSERT INTO logs(status, timestamp) VALUES (?, ?)",
    (status, current_time)
)

conn.commit()
conn.close()

print(status)
# import requests
# from bs4 import BeautifulSoup
# import hashlib
# import sqlite3
# from datetime import datetime

# url = "https://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# current_content = soup.get_text()

# current_hash = hashlib.sha256(current_content.encode()).hexdigest()

# with open("baseline.txt", "r") as file:
#     saved_hash = file.read()

# if current_hash == saved_hash:
#     status = "Website Safe"
# else:
#     status = "WARNING! Website Changed"

# current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# conn = sqlite3.connect("database.db")

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS logs (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     status TEXT,
#     timestamp TEXT
# )
# """)

# cursor.execute(
#     "INSERT INTO logs(status, timestamp) VALUES (?, ?)",
#     (status, current_time)
# )

# conn.commit()
# conn.close()

# print(status)
# print("Log Saved")