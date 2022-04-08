from ui.commands.list_bookmarks import ListUnreadBookmarks


class MarkBookmarkChecked:
    def __init__(self, i_o, bookmark_service):
        """Initializes command with IO and BookmarkService objects.

        Args:
            i_o (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = i_o
        self._bookmark_service = bookmark_service
        self._list_unread_bookmarks = ListUnreadBookmarks(
            self._io, self._bookmark_service
        )

    def __str__(self):
        return "merkitse vinkki luetuksi"

    def execute(self):
        """Executes command."""
        self._list_unread_bookmarks.execute()
        bookmark_id = self._io.read(
            "\nMerkitse vinkki luetuksi antamalla vinkin numero: ")

        self._io.write(bookmark_id)
        #if not self._validator.check_title(title):
        #    self.execute()
        #    return

        #self._bookmark_service.set_bookmark_checked(bookmark_id)
