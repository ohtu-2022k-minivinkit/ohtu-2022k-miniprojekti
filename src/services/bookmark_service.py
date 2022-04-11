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
            bookmark_range (string):
                Selected range of bookmarks. Accepts values BOOKMARK_RANGE__ALL,
                BOOKMARK_RANGE__CHECKED and BOOKMARK_RANGE__UNCHECKED.

        Returns:
            list: List of Bookmark objects.
        """
        if bookmark_range == BOOKMARK_RANGE__ALL:
            return self._bookmark_repository.get_all()
        if bookmark_range == BOOKMARK_RANGE__UNCHECKED:
            return self._bookmark_repository.get_by_checked(0)
        if bookmark_range == BOOKMARK_RANGE__CHECKED:
            return self._bookmark_repository.get_by_checked(1)
        raise ValueError(f"Unknown range ({range})!")

    def get_bookmarks_by_keyword(self, keyword) -> list:
        """Returns all bookmarks where headline contains keyword.

        Args:
            keyword (string):
                Keyword to be looked for from bookmark headlines.

        Returns:
            list: List of Bookmark objects.
        """
        return self._bookmark_repository.get_bookmarks(keyword)

    def set_bookmark_as_checked(self, bookmark_id):
        """Sets bookmark with given id as checked."""
        self._bookmark_repository.set_bookmark_as_checked(bookmark_id)


bookmark_service = BookmarkService()
