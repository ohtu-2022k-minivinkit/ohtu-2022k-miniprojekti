from ui.console_io import (
    console_io as default_console_io
)
from ui.commands.add_bookmark import AddBookmark
from ui.commands.list_bookmarks import (
    ListAllBookmarks, ListUnreadBookmarks, ListCheckedBookmarks
)
from ui.bookmark_validation import BookmarkValidation
from services.bookmark_service import (
    bookmark_service as default_bookmark_service
)


class UI:
    def __init__(
            self, bookmark_service=default_bookmark_service,
            input_output=default_console_io):
        """Initialize UI with BookmarkService and IO objects.

        Args:
            bookmark_service (class, optional):
                Service class containing business logic. Defaults to
                default_bookmark_service.
            input_output (class, optional):
                Object providing IO methods (read() and write()). Defaults to
                default_console_io.
        """
        self._io = input_output
        self._bookmark_service = bookmark_service
        self._list_unread_bookmarks = ListUnreadBookmarks(
            self._io, self._bookmark_service)

        self._commands = {
            "1": AddBookmark(
                self._io, self._bookmark_service, BookmarkValidation(self._io)),
            "2": ListAllBookmarks(self._io, self._bookmark_service),
            "3": ListCheckedBookmarks(self._io, self._bookmark_service)
        }

    def start(self):
        """Starts the user interface."""

        self._io.write("** Lukuvinkkikirjasto **\n")
        self._list_unread_bookmarks.execute()
        self._print_info()

        while True:
            self._io.write("")
            command = self._io.read("komento: ")

            if command == "x":
                break
            if not command in self._commands:
                self._io.write("virheellinen komento")
                self._print_info()
                continue

            command_object = self._commands[command]
            command_object.execute()

    def _print_info(self):
        self._io.write("\nKomennot:\nx lopeta")
        for key in self._commands.keys():
            self._io.write(f"{key} {self._commands[key]}")
