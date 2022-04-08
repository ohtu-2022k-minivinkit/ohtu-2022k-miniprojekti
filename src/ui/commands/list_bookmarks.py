class ListAllBookmarks():
    def __init__(self, io, bookmark_service):
        """Initializes command with IO and BookmarkService objects.

        Args:
            io (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = io
        self._bookmark_service = bookmark_service

    def __str__(self):
        return "näytä kaikki vinkit"

    def execute(self):
        """Executes command."""
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("all")
        if bookmark_list:
            self._io.write("Kaikki vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Kirjastossa ei ole vinkkejä")


class ListUnreadBookmarks():
    def __init__(self, io, bookmark_service):
        """Initializes command with IO and BookmarkService objects.

        Args:
            io (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = io
        self._bookmark_service = bookmark_service

    def __str__(self):
        return "näytä lukemattomat vinkit"

    def execute(self):
        """Executes command."""
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("not checked")
        if bookmark_list:
            self._io.write("Lukemattomat vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Olet lukenut kaikki vinkit")


class ListCheckedBookmarks():
    def __init__(self, io, bookmark_service):
        """Initializes command with IO and BookmarkService objects.

        Args:
            io (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = io
        self._bookmark_service = bookmark_service

    def __str__(self):
        return "näytä luetut vinkit"

    def execute(self):
        """Executes command."""
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("checked")
        if bookmark_list:
            self._io.write("Luetut vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Kirjastossa ei ole luettuja vinkkejä")
