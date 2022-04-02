from repositories.bookmark_repository import (
    bookmark_repository as default_bookmark_repository
)


class BookmarkService():
    def __init__(self, bookmark_repository=default_bookmark_repository):
        self._bookmark_repository = bookmark_repository

    def create_bookmark(self, bookmark):
        self._bookmark_repository.create(bookmark)

    def get_all_bookmarks(self):
        return self._bookmark_repository.get_all()


bookmark_service = BookmarkService()
