from sqlite3 import Error
from entities.bookmark import Bookmark
from database_connection import get_database_connection

class BookmarkRepository:
    def __init__(self, connection):
        self._connection = connection
        self.__create_table()

    def __create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY, headline TEXT, url TEXT)"""
        try:
            cursor = self._connection.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)

    def create(self, bookmark: Bookmark):
        try:
            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO bookmarks (headline, url) VALUES (?,?)", 
                [bookmark.headline, bookmark.url])
            self._connection.commit()
        except Error as e:
            print(e)


bookmark_repository = BookmarkRepository(get_database_connection())