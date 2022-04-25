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
        """Returns all bookmarks as a list of Bookmark objects."""
        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url, checked, id FROM bookmarks")
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1], row[2], row[3]))

        return bookmarks

    def get_by_checked(self, checked) -> list:
        """Returns read or unread bookmarks as a list of Bookmark objects.

        Args:
            status (integer): Is bookmark checked or not (0 or 1).
        """
        cursor = self._connection.cursor()
        cursor.execute("""SELECT headline, url, checked, id
                        FROM bookmarks
                        WHERE checked=?
                        """, [checked])
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1], row[2], row[3]))

        return bookmarks

    def get_by_keyword(self, keyword: str) -> list:
        """Returns list of bookmarks where headline contains keyword."""
        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url, checked, id FROM bookmarks " \
            "WHERE headline LIKE ?", ['%' + keyword + '%'])
        data = cursor.fetchall()
        bookmarks = []
        for row in data:
            bookmarks.append(Bookmark(row[0], row[1], row[2], row[3]))

        return bookmarks

    def set_as_checked(self, bookmark_id: int):
        """Sets bookmark with given database id as checked."""
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE bookmarks SET checked=TRUE WHERE id=?", [bookmark_id])
        self._connection.commit()

    def delete_all(self):
        """Delete all bookmarks"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM bookmarks")
        self._connection.commit()

    def create_csv_file(self, file_path):
        """Creates csv file containing headline and url columns."""

        cursor = self._connection.cursor()
        cursor.execute("SELECT headline, url FROM bookmarks")
        data = cursor.fetchall()

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("otsikko;linkki\n")
            for row in data:
                file.write(";".join(row)+"\n")


    def load_csv_file(self, file_path):
        """Reads csv file containing headline;url rows and creates bookmarks out of them.

        Returns:
            boolean: True if successful, False otherwise.
        """

        with open(file_path, encoding="utf-8") as file:
            first_row = next(file)

            if first_row != "otsikko;linkki\n":
                return False

            for row in file:
                row = row.strip()
                row_parts = row.split(";")
                self.create(Bookmark(row_parts[0],row_parts[1]))
        return True

    @classmethod
    def read_file(cls, file_path):
        """For testing, reads content of the file."""
        with open(file_path, encoding="utf-8") as file:
            return file.read()

    @classmethod
    def create_file(cls, file_path, data):
        """For testing, creates test file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @classmethod
    def delete_all_file_content(cls, file_path):
        """For testing, deletes content of the file."""
        with open (file_path, "w", encoding="utf-8"):
            pass

bookmark_repository = BookmarkRepository(get_database_connection())
