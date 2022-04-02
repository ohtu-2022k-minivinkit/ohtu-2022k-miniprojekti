from repositories.bookmark_repository import (
    bookmark_repository as default_bookmark_repository
)


class BookmarkService():
    def __init__(self, bookmark_repository=default_bookmark_repository):
        self._bookmark_repository = bookmark_repository

    def create_bookmark(self, title, link):
        # Menisikö tämä näin: self._bookmark_repository.create(Bookmark(title, link))?
        pass

    def get_all_bookmarks(self):
        # return self._bookmark_repository.find_all()
        pass


bookmark_service = BookmarkService()
