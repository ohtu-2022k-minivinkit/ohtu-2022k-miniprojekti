from repositories.bookmark_repository import (
    bookmark_repository as default_bookmark_repository
)
from entities.bookmark import Bookmark


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

    def get_bookmarks_with_range(self, choice) -> list:
        """Returns the list of the chosen range of bookmarks stored in the repository.

        Args:
            choice (string):
                Selected range of bookmarks. Accepts values 'all', 'checked'
                and 'not checked'.

        Returns:
            list: List of Bookmark objects.
        """
        if choice == "not checked":
            return self._bookmark_repository.get_bookmarks_checked_status(0)
        if choice == "checked":
            return self._bookmark_repository.get_bookmarks_checked_status(1)
        return self._bookmark_repository.get_all()

    def get_bookmarks(self, keyword) -> list:
        """Returns all bookmarks where headline contains keyword.

        Args:
            keyword (string):
                Keyword to be looked for from bookmark headlines.

        Returns:
            list: List of Bookmark objects.
        """
        return self._bookmark_repository.get_bookmarks(keyword)

    def set_bookmark_checked(self, bookmark_id):
        """Sets bookmark with given id as checked.

        Args:
            bookmark_id (integer): Database id of the
        """
        # pylint: disable=unnecessary-pass
        pass


bookmark_service = BookmarkService()
