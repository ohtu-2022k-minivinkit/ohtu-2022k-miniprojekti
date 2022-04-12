from services.bookmark_service import (
    BOOKMARK_RANGE__ALL, BOOKMARK_RANGE__CHECKED, BOOKMARK_RANGE__UNCHECKED
)


class ListAllBookmarks:
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

    def __str__(self):
        return "näytä kaikki vinkit"

    def execute(self):
        """Executes command.

        Returns:
            Returns True if bookmarks were found, False otherwise.
        """
        bookmark_list = self._bookmark_service.get_bookmarks_by_range(
            BOOKMARK_RANGE__ALL)
        if bookmark_list:
            self._io.write("Kaikki vinkit:")
            self._io.write_table(bookmark_list)
            return True
        self._io.write("Kirjastossa ei ole vinkkejä")
        return False


class ListUnreadBookmarks:
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
        self.bookmark_list = None

    def __str__(self):
        return "näytä lukemattomat vinkit"

    def execute(self):
        """Executes command.

        Returns:
            Returns True if bookmarks were found, False otherwise.
        """
        self.bookmark_list = self._bookmark_service.get_bookmarks_by_range(
            BOOKMARK_RANGE__UNCHECKED)
        if self.bookmark_list:
            self._io.write("Lukemattomat vinkit:")
            self._io.write_table(self.bookmark_list)
            return True
        self._io.write("Olet lukenut kaikki vinkit")
        return False


class ListCheckedBookmarks:
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

    def __str__(self):
        return "näytä luetut vinkit"

    def execute(self):
        """Executes command.

        Returns:
            Returns True if bookmarks were found, False otherwise.
        """
        bookmark_list = self._bookmark_service.get_bookmarks_by_range(
            BOOKMARK_RANGE__CHECKED
        )
        if bookmark_list:
            self._io.write("Luetut vinkit:")
            self._io.write_table(bookmark_list)
            return True
        self._io.write("Kirjastossa ei ole luettuja vinkkejä")
        return False


class ListBookmarksByKeyword:
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

    def __str__(self):
        return "hae otsikolla"

    def execute(self):
        """Executes command."""
        keyword = self._io.read("Anna hakusana: ")
        bookmarks = self._bookmark_service.get_bookmarks_by_keyword(keyword)
        if bookmarks:
            self._io.write(f"Vinkit, jotka sisälsivät hakusanan '{keyword}':")
            self._io.write_table(bookmarks)
        else:
            self._io.write(f"Hakusanalla '{keyword}' ei löytynyt yhtään vinkkiä")
