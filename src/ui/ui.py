from ui.console_io import (
    console_io as default_console_io
)
from entities.bookmark import Bookmark

COMMANDS = {
    "x": "x lopeta",
    "1": "1 lisää vinkki",
    "2": "2 tulosta vinkit"
    }

class UI:
    def __init__(self, service, input_output=default_console_io):
        self._io = input_output
        self._bookmark_service = service
        self._error = False

    def start(self):
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
                self.list_bookmarks()

    def _print_info(self):
        for command in COMMANDS.values():
            self._io.write(command)

    def _add_bookmark(self):
        self._io.write("Lisätään uusi vinkki")

        title = self._io.read("otsikko: ")
        self.check_title(title)
        if self._error:
            return

        link = self._io.read("linkki: ")
        self.check_link(link)
        if self._error:
            return

        self._bookmark_service.create_bookmark(Bookmark(title, link))

    def check_title(self, title):
        title = title.strip()
        # ehkä lisää ehtoja? nyt katsoo ettei title tyhjä tai yli 100 merkkiä
        if not title or len(title) > 100:
            self._error = True
            self._io.write("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")

        # ? ehkä parempia ehtoja? nyt katsoo että alussa http ja väh 10 merkkiä pitkä
    def check_link(self, link):
        if len(link.strip()) < 10 or link[:4] != "http":
            self._error = True
            self._io.write("linkki oli virheellinen, anna otsikko ja linkki uudelleen")

    def list_bookmarks(self):
        bookmark_list = self._bookmark_service.get_all_bookmarks()
        if bookmark_list:
            for bookmark in bookmark_list:
                self._io.write(f'{bookmark}\n')
 