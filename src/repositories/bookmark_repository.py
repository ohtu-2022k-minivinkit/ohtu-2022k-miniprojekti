from sqlite3 import Error
from entities.bookmark import Bookmark
from database_connection import get_database_connection
import initialize_database


class BookmarkRepository:
    def __init__(self, connection):
        self._connection = connection
        initialize_database.initialize_database()

    def create(self, bookmark: Bookmark):
        """Create a new bookmark"""
        try:
            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO bookmarks (headline, url) VALUES (?,?)",
                [bookmark.headline, bookmark.url])
            self._connection.commit()
        except Error as err:
            print(err)

    def get_all(self) -> list:
        """Get all bookmarks"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url FROM bookmarks")
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1]))

        return bookmarks

    def delete_all(self):
        """Delete all bookmarks"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM bookmarks")
        self._connection.commit()


bookmark_repository = BookmarkRepository(get_database_connection())
