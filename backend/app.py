import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    connection = psycopg2.connect(
        host="172.27.156.196",
        database="devopsdb",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )
    return connection


@app.route("/")
def home():
    return "Hello from backend - GitOps v2"

@app.route("/health")
def health():
    return "Healthy"


@app.route("/api/users")
def users():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, role FROM users;")
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    users_list = []

    for row in rows:
        users_list.append({
            "id": row[0],
            "name": row[1],
            "role": row[2]
        })

    return jsonify(users_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
