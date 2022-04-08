from sqlite3 import Error
from entities.bookmark import Bookmark
from database_connection import get_database_connection
import initialize_database


class BookmarkRepository:
    def __init__(self, connection):
        self._connection = connection
        initialize_database.create_tables(connection)

    def create(self, bookmark: Bookmark):
        """Create a new bookmark"""
        try:
            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO bookmarks (headline, url, checked) VALUES (?,?,?)",
                [bookmark.headline, bookmark.url, bookmark.checked])
            self._connection.commit()
        except Error as err:
            print(err)

    def get_all(self) -> list:
        """Get all bookmarks"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url, checked FROM bookmarks")
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1], row[2]))

        return bookmarks


    def get_bookmarks_checked_status(self, status) -> list:
        """Gets already read or not read bookmarks as chosen.

            Args:
                status (integer): selected status of bookmarks to get from repository
                                    0 = not checked
                                    1 = checked
            """
        cursor = self._connection.cursor()
        cursor.execute("""SELECT headline, url, checked
                        FROM bookmarks
                        WHERE checked=?
                        """, [status])
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            print(row)
            bookmarks.append(Bookmark(row[0], row[1], row[2]))

        return bookmarks

    def get_bookmarks(self, keyword: str) -> list:
        """Get all bookmarks where headline contains keyword"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url, checked FROM bookmarks " \
            "WHERE headline LIKE ?", ['%' + keyword + '%'])
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1], row[2]))

        return bookmarks

    def delete_all(self):
        """Delete all bookmarks"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM bookmarks")
        self._connection.commit()


bookmark_repository = BookmarkRepository(get_database_connection())
