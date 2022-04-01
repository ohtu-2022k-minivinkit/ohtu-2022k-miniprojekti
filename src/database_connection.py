import sqlite3

connection = sqlite3.connect("database.sqlite")

#Palauttaa sanakirjana
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
