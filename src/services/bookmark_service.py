from repositories.bookmark_repository import (
    bookmark_repository as default_bookmark_repository
)


class BookmarkService():
    def __init__(self, bookmark_repository=default_bookmark_repository):
        self._bookmark_repository = bookmark_repository

    def create_bookmark(self, bookmark):
        # Menisikö tämä näin: self._bookmark_repository.create(bookmark)?
        pass

    def get_all_bookmarks(self):
        # return self._bookmark_repository.find_all()
        print('BookmarkService.get_all_bookmarks()')


bookmark_service = BookmarkService()