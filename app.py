import sqlite3
import subprocess
import os

app = sqlite3.connect("users.db")
cursor = app.cursor()


def find_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def ping_host(host):
    result = subprocess.run(
        "ping -c 1 " + host,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def main():
    username = input("Enter username: ")
    print(find_user(username))

    host = input("Enter host to ping: ")
    print(ping_host(host))

    filename = input("Enter filename: ")
    print(read_file(filename))


if __name__ == "__main__":
    main()
