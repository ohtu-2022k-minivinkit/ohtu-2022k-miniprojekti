from ui.commands.list_bookmarks import ListUnreadBookmarks


class MarkBookmarkChecked:
    def __init__(self, console_io, bookmark_service, user_interface):
        """Initializes command with IO, BookmarkService and UI objects.

        Args:
            in_out (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._console_io = console_io
        self._bookmark_service = bookmark_service
        self._list_unread_bookmarks = ListUnreadBookmarks(
            self._console_io, self._bookmark_service
        )
        self._user_interface = user_interface

    def __str__(self):
        return "merkitse vinkki luetuksi"

    def execute(self):
        """Executes command."""
        self._list_unread_bookmarks.execute()
        ui_number = self._console_io.read(
            "\nMerkitse vinkki luetuksi antamalla vinkin numero (tai 'x' "\
            "keskeyttääksesi): ")

        if ui_number == "x":
            return

        if not self._validate_ui_number(ui_number):
            self.execute()
            return

        bookmark = self._list_unread_bookmarks.bookmark_list[int(ui_number)-1]
        self._bookmark_service.set_bookmark_as_checked(bookmark.database_id)
        self._console_io.write(
            f"Merkittiin vinkki {ui_number} ({bookmark.headline}) luetuksi")

    def _validate_ui_number(self, ui_number):
        try:
            ui_number = int(ui_number)
        except ValueError:
            self._user_interface.print_error(
                f"Virheellinen syöte ({ui_number})!")
            return False

        if ui_number < 1 or ui_number > len(
                self._list_unread_bookmarks.bookmark_list):
            self._user_interface.print_error(
                f"Vinkkiä {ui_number} ei ole!")
            return False

        return True
