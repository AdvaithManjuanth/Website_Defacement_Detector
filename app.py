from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, status, timestamp FROM logs ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    html = "<h1>Website Defacement Detector Dashboard</h1>"

    for row in rows:
        html += f"<p>ID: {row[0]} | {row[1]} | {row[2]}</p>"

    return html

if __name__ == "__main__":
    app.run(debug=True)
 # from flask import Flask
# import sqlite3

# app = Flask(__name__)

# @app.route('/')
# def home():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT id, status FROM logs ORDER BY id DESC")

#     rows = cursor.fetchall()

#     conn.close()

#     html = """
#     <html>
#     <body>
#         <h1>Website Defacement Detector Dashboard</h1>
#     """

#     for row in rows:
#         html += f"<h3>ID: {row[0]} | Status: {row[1]}</h3>"

#     html += """
#     </body>
#     </html>
#     """

#     return html

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask
# import sqlite3

# app = Flask(__name__)

# @app.route('/')
# def home():
#     import os
#     print(os.path.abspath("database.db"))
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM logs ORDER BY id DESC")

#     rows = cursor.fetchall()

#     conn.close()

#     output = "<h1>Website Defacement Detector Dashboard</h1>"

#     for row in rows:
#         output += f"<p>ID: {row[0]} | Status: {row[1]}</p>"

#     return output

# if __name__ == '__main__':
#     app.run(debug=True)