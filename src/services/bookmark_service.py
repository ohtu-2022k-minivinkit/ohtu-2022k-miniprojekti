import os
from datetime import datetime
from repositories.bookmark_repository import (
    bookmark_repository as default_bookmark_repository
)
from entities.bookmark import Bookmark


BOOKMARK_RANGE__ALL = 0
BOOKMARK_RANGE__CHECKED = 1
BOOKMARK_RANGE__UNCHECKED = 2


class BookmarkService():
    def __init__(self, bookmark_repository=default_bookmark_repository):
        """Creates new BookmarkService object.

        Args:
            bookmark_repository (BookmarkRepository, optional):
                Repository where the bookmarks are stored. Defaults to
                default_bookmark_repository.
        """
        self._bookmark_repository = bookmark_repository

    def create_bookmark(self, title, link):
        """Creates a new bookmark and stores it into the repository.

        Args:
            title (string): Title of the bookmark.
            link (string): Bookmarked link.
        """
        self._bookmark_repository.create(Bookmark(title, link))

    def get_bookmarks_by_range(self, bookmark_range) -> list:
        """Returns a list of bookmarks by predefined ranges.

        Args:
            bookmark_range (integer):
                Selected range of bookmarks. Accepts values BOOKMARK_RANGE__ALL,
                BOOKMARK_RANGE__CHECKED and BOOKMARK_RANGE__UNCHECKED.

        Returns:
            list: List of Bookmark objects.
        """
        if bookmark_range == BOOKMARK_RANGE__ALL:
            return self._bookmark_repository.get_all()
        if bookmark_range == BOOKMARK_RANGE__UNCHECKED:
            return self._bookmark_repository.get_by_checked(False)
        if bookmark_range == BOOKMARK_RANGE__CHECKED:
            return self._bookmark_repository.get_by_checked(True)
        raise ValueError(f"Unknown range ({range})!")

    def get_bookmarks_by_keyword(self, keyword) -> list:
        """Returns all bookmarks where headline contains keyword.

        Args:
            keyword (string):
                Keyword to be looked for from bookmark headlines.

        Returns:
            list: List of Bookmark objects.
        """
        return self._bookmark_repository.get_by_keyword(keyword)

    def set_bookmark_as_checked(self, bookmark_id):
        """Sets bookmark with given id as checked."""
        self._bookmark_repository.set_as_checked(bookmark_id)

    def create_file(self, file_path):
        """Calls bookmark repository to write bookmarks into the file provided by user.

        Args:
            file_path (string): path to the file provided by user.
        """
        self._bookmark_repository.create_csv_file(file_path)

    def load_file(self, file_path):
        """Calls bookmark repository to read bookmarks from the file provided by user
        and add them to the repository.

        Args:
            file_path (string): path to the file provided by user.

        Returns:
            boolean: True if successful, False otherwise.
        """
        self._bookmark_repository.load_csv_file(file_path)

    @classmethod
    def create_default_filename(cls):
        """Creates default filename"""
        return f"vinkit_{datetime.now().strftime('%d.%m.%Y')}.csv"

    @classmethod
    def correct_filename(cls, filename):
        """Checks correctness of the filename provided by the user.

        Checks file extension and underscores, and corrects them if necessary.

        Args:
            filename (string):  filename given by user as input

        Returns:    corrected filename as a string
        """
        filename = filename if " " not in filename else filename.replace(" ", "_")
        filename = filename if filename[-4:] == ".csv" else filename + ".csv"
        return filename

    @classmethod
    def create_default_filepath(cls, filename):
        """Creates an absolute file path to the file in the application data directory.

        Args:
            filename (string):  filename provided by user

        Returns:    absolute file path to the file as a string
        """

        BookmarkService.create_default_csv_directory_if_missing()
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "..", "..", "csv_files", filename)
        return str(file_path).replace("/src/services/../..", "")

    @classmethod
    def create_default_csv_directory_if_missing(cls):
        """Creates the default csv-directory if missing."""

        dirname = os.path.dirname(__file__)
        dir_path = os.path.join(dirname, "..", "..", "csv_files")
        if not BookmarkService.exists(dir_path):
            os.mkdir(dir_path)

    @classmethod
    def exists(cls, path):
        """Checks if the file or the directory already exists.

        Args:
            path (string): an absolute path to the file or directory

        Returns:    boolean value depending on the existence of the file or directory
        """
        return os.path.exists(path)

    @classmethod
    def correct_dir_path(cls, new_dir_path):
        """Checks trailing slashes from begin and the end of the path

        Args:
            new_dir_path (string): an absolute path to the directory

        Returns:    an absolute path to the directory with trailing lashes
        """
        new_dir_path = new_dir_path + "/" if new_dir_path[-1] != "/" else new_dir_path
        new_dir_path = "/" + new_dir_path if new_dir_path[0] != "/" else new_dir_path
        return new_dir_path

bookmark_service = BookmarkService()
