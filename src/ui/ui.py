from entities.bookmark import Bookmark
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
    def __init__(self,
            bookmark_service=default_bookmark_service,
            input_output=default_console_io
            ):
        self._io = input_output
        self._bookmark_service = bookmark_service
        self._error = False

    def start(self):
        """Start the program"""

        self._io.write("")
        self._io.write("Lukemattomat vinkit:")
        self._list_bookmarks_with_range("not read")

        self._io.write("")
        self._io.write("Bookmarks komennot:")
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
                self._list_bookmarks_with_range("all")

            if command == "3":
                self._list_bookmarks_with_range("read")

    def _print_info(self):
        """Prints all UI -commands to user to see"""

        for command in COMMANDS.values():
            self._io.write(command)

    def _add_bookmark(self):
        """Asks for title and link inputs from user.

        If user's input is valid,
        calls Bookmark_service class to create bookmark and add
        it into the repository.

        If input is not valid, executing will return to the
        while -loop in the method start.
        """
        self._io.write("Lisätään uusi vinkki")

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
        """Validates user input for title.

        if user's input is not valid, prints an error message
        and places True in the variable self._error.

        Args:
            title (string): user's input for title
        """
        title = title.strip()
        if not title or len(title) > 100:
            self._error = True
            self._io.write("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")

    def _check_link(self, link):
        """Validates user input for link.

        if user's input is not valid, prints an error message
        and places True in the variable self._error.

        Args:
            link (string): user's input for link
        """
        if len(link.strip()) < 12 or link[:4] != "http" or " " in link.strip():
            self._error = True
            self._io.write("linkki oli virheellinen, anna otsikko ja linkki uudelleen")

    def _list_bookmarks_with_range(self, choice):
        """Prints chosen range of bookmarks stored in the repository."""

        bookmark_list = self._bookmark_service.get_bookmarks(choice)
        if bookmark_list:
            for bookmark in bookmark_list:
                self._io.write(f'{bookmark}')
