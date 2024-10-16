import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
def create_table():
    with connection:
        cursor.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")
def add_entry(entry_content, entry_date):
    with connection:
        cursor.execute("INSERT INTO entries (content, date) values (?, ?);", (entry_content, entry_date))
def get_entries():
    cursor.execute("SELECT * FROM  entries")
    return cursor

