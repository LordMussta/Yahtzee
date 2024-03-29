import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS highScores (date TEXT, user TEXT, score INTEGER);")


def insert_data(date, user, score):
    with connection:
        connection.execute(
            "INSERT INTO highScores VALUES(?, ?, ?);", (date, user, score))


def select_all_data():
    return connection.execute("SELECT * FROM highScores ORDER BY score DESC LIMIT 10;")


def delete_table():
    with connection:
        connection.execute("DROP TABLE IF EXISTS highScores;")


def close_connection():
    connection.close()
