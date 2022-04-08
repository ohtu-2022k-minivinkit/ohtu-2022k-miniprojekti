from ui.console_io import (
    console_io as default_console_io
)
from services.bookmark_service import (
    bookmark_service as default_bookmark_service
)


COMMANDS = {
    "x": "x lopeta",
    "1": "1 lisää vinkki",
    "2": "2 näytä kaikki vinkit",
    "3": "3 näytä luetut vinkit"
    }


class UI:
    def __init__(
            self, bookmark_service=default_bookmark_service,
            input_output=default_console_io):
        """Initializes UI with service class and ConsoleIO object.

        Args:
            bookmark_service (BookmarkService, optional):
                Service class containing the busines logic used through the UI.
                Defaults to default_bookmark_service.
            input_output (class, optional):
                Object providing IO methods (read() and write()). Defaults to
                default_console_io.
        """
        self._io = input_output
        self._bookmark_service = bookmark_service
        self._error = False

    def start(self):
        """Starts the user interface."""
        self._io.write("** Lukuvinkkikirjasto **\n")
        self._list_unread_bookmarks()
        self._print_info()

        while True:
            self._error = False
            self._io.write("")
            command = self._io.read("komento: ")
            if not command in COMMANDS:
                self._io.write("virheellinen komento")
                self._print_info()
                continue
            if command == "x":
                break
            if command == "1":
                self._add_bookmark()
            if command == "2":
                self._list_all_bookmarks()
            if command == "3":
                self._list_checked_bookmarks()

    def _print_info(self):
        self._io.write("\nKomennot:")
        for command in COMMANDS.values():
            self._io.write(command)

    def _add_bookmark(self):
        self._io.write("\nLisätään uusi vinkki")

        title = self._io.read("otsikko: ")
        self._check_title(title)
        if self._error:
            return

        link = self._io.read("linkki: ")
        self._check_link(link)
        if self._error:
            return

        self._bookmark_service.create_bookmark(title, link)

    def _check_title(self, title):
        title = title.strip()
        if not title or len(title) > 100:
            self._error = True
            self._io.write("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")

    def _check_link(self, link):
        if len(link.strip()) < 12 or link[:4] != "http" or " " in link.strip():
            self._error = True
            self._io.write("linkki oli virheellinen, anna otsikko ja linkki uudelleen")

    def _list_all_bookmarks(self):
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("all")
        if bookmark_list:
            self._io.write("Kaikki vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Kirjastossa ei ole vinkkejä")

    def _list_unread_bookmarks(self):
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("not checked")
        if bookmark_list:
            self._io.write("Lukemattomat vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Olet lukenut kaikki vinkit")

    def _list_checked_bookmarks(self):
        bookmark_list = self._bookmark_service.get_bookmarks_with_range("checked")
        if bookmark_list:
            self._io.write("Luetut vinkit:")
            self._io.write_table(bookmark_list)
        else:
            self._io.write("Kirjastossa ei ole luettuja vinkkejä")
