import sqlite3
from config import DATABASE_FILE_PATH

CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)

def get_database_connection():
    return CONNECTION
