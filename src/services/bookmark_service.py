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

    def get_bookmarks_with_range(self, choice):
        """Returns chosen range of bookmarks stored in the repository.

        Returns chosen range of bookmarks stored in the repository as a list of Bookmark objects.

        Args:
            choice (string): selected range of bookmarks
                            values: all, not read or read

        Returns:
            list: List of Bookmark objects.
        """
        if choice == "all":
            return self._bookmark_repository.get_all()
        if choice == "not read":
            return self._bookmark_repository.get_choice(0)
        if choice == "read":
            return self._bookmark_repository.get_choice(1)

    def get_bookmarks(self, keyword):
        """Returns all bookmarks where headline contains keyword
        Returns:
            list: List of Bookmark objects
        """
        return self._bookmark_repository.get_bookmarks(keyword)

bookmark_service = BookmarkService()
