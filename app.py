from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)


def get_db():
    return sqlite3.connect("users.db")


@app.route("/user")
def find_user():
    username = request.args.get("username", "")

    db = get_db()
    cursor = db.cursor()

    # Intentionally vulnerable: user input is directly added to SQL.
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    results = cursor.fetchall()
    db.close()

    return str(results)


@app.route("/ping")
def ping_host():
    host = request.args.get("host", "")

    # Intentionally vulnerable: user input is passed to a shell command.
    result = subprocess.run(
        "ping -c 1 " + host,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout


if __name__ == "__main__":
    app.run(debug=True)
