from ui.console_io import (
    console_io as default_console_io
)
from ui.commands.add_bookmark import AddBookmark
from ui.commands.list_bookmarks import (
    ListAllBookmarks, ListBookmarksByKeyword, ListUnreadBookmarks, ListCheckedBookmarks
)
from ui.commands.mark_bookmark_checked import MarkBookmarkChecked
from ui.commands.csv_file_transactions import CreateCsvFile
from ui.bookmark_validation import BookmarkValidation
from services.bookmark_service import (
    bookmark_service as default_bookmark_service
)
from services.network_service import (
    network_service as default_network_service
)


class UI:
    def __init__(
            self, bookmark_service=default_bookmark_service,
            network_service=default_network_service,
            input_output=default_console_io):
        """Initialize UI with BookmarkService, NetworkService and IO objects.

        Args:
            bookmark_service (class, optional):
                Service class containing business logic. Defaults to
                default_bookmark_service.
            network_service (class, optional):
                Service class containing network logic. Defaults to
                default_network_service.
            input_output (class, optional):
                Object providing IO methods (read() and write()). Defaults to
                default_console_io.
        """
        self._console_io = input_output
        self._bookmark_service = bookmark_service
        self._network_service = network_service
        self._list_unread_bookmarks = ListUnreadBookmarks(
            self._console_io, self._bookmark_service)

        self._commands = {
            "1": AddBookmark(
                self._console_io, self._bookmark_service, self._network_service,
                BookmarkValidation(self._console_io)),
            "2": ListAllBookmarks(self._console_io, self._bookmark_service),
            "3": ListCheckedBookmarks(self._console_io, self._bookmark_service),
            "4": MarkBookmarkChecked(self._console_io, self._bookmark_service, self),
            "5": ListBookmarksByKeyword(self._console_io, self._bookmark_service),
            "6": CreateCsvFile(self._console_io, self._bookmark_service)
        }

    def start(self):
        """Starts the user interface."""

        self._console_io.write("** Lukuvinkkikirjasto **\n")
        self._list_unread_bookmarks.execute()
        self.print_info()

        while True:
            self._console_io.write("")
            command = self._console_io.read("komento: ")

            if command == "x":
                break
            if not command in self._commands:
                self._console_io.write("virheellinen komento")
                self.print_info()
                continue

            command_object = self._commands[command]
            command_object.execute()

    def print_info(self):
        """Prints command menu to console."""
        self._console_io.write("\nKomennot:\nx lopeta")
        # pylint: disable=consider-using-dict-items
        for key in self._commands:
            self._console_io.write(f"{key} {self._commands[key]}")

    def print_error(self, error_msg):
        """Prints error message to console."""
        self._console_io.write(f"\nVIRHE: {error_msg}\n")
