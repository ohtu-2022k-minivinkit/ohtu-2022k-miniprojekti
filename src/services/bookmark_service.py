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

    def get_bookmarks(self, choice):
        """Returns chosen range of bookmarks stored in the repository.

        Returns chosen range of bookmarks stored in the repository as a list of Bookmark objects.

        Args:
            range (string): selected range of bookmarks
                            values: all, not readed or readed

        Returns:
            list: List of Bookmark objects.
        """
        if choice == "all":
            return self._bookmark_repository.get_all()
        if choice == "not readed":
            return self._bookmark_repository.get_choice(0)
        if choice == "readed":
            return self._bookmark_repository.get_choice(1)

bookmark_service = BookmarkService()
