Website Defacement Detection System

A cybersecurity project that monitors website integrity by comparing the current website content against a trusted baseline using SHA-256 hashing. The system detects unauthorized modifications, logs events in a database, provides a monitoring dashboard, captures screenshots, and supports email alerts.

Features
Website content monitoring
SHA-256 hash-based integrity verification
Website defacement detection
SQLite database logging
Flask web dashboard
Timestamped activity records
Screenshot capture using Selenium
Email alert notifications
Support for monitoring public websites or local demo websites
Technologies Used
Python
Flask
SQLite
Requests
BeautifulSoup
Hashlib
Selenium
SMTP Email Alerts
How to Run
1. Run the Sample Website (Optional)

Open a terminal in the project folder and run:

python -m http.server 8000

Sample website URL: http://127.0.0.1:8000/demo_website.html

2. Create the Baseline
python create_baseline.py
3. Run Website Integrity Check
python detector.py
4. Launch Dashboard
python app.py
Open: http://127.0.0.1:5000/
5. Capture Website Screenshot
python screenshot.py

Configuration
To monitor a different website, update the URL in:  config.py
Example:
URL = "https://www.python.org"

Email Alerts
To enable email notifications, configure the following fields in:
detector.py

Sender Email

Gmail App Password

Receiver Email
