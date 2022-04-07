from ui.console_io import (
    console_io as default_console_io
)
from services.bookmark_service import (
    bookmark_service as default_bookmark_service
)
#??tuleeko näistä ongelma testauksessa? 
# funktiolla all read -valinta erikseen ja nämä defaultin kautta
from ui.user_commands.add_bookmark import AddBookmark
from ui.user_commands.list_bookmarks import ListBookmarks
from ui.user_commands.exit import Exit

class UI:
    def __init__(self,
            bookmark_service=default_bookmark_service,
            input_output=default_console_io):

        self._io = input_output
        self._bookmark_service = bookmark_service

        self._commands = {
            "x": Exit(),
            "1": AddBookmark(),
            "2": ListBookmarks("all"),
            "3": ListBookmarks("read")
        }

    def start(self):
        """Start the program"""

        self._io.write("")
        self._io.write("Lukemattomat vinkit:")
        ListBookmarks("not read")

        self._io.write("")
        self._io.write("Bookmarks komennot:")
        self._print_all_commands()

        while True:
            self._io.write("")
            command = self._io.read("komento: ")
            
            if not command in self._commands:
                self._io.write("virheellinen komento")
                self._print_all_info()
                continue

            if command == "x":
                break

            command_object = self._commands[command]
            command_object._execute()

    def _print_all_commands(self):
        """Prints all UI -commands to user to see"""

        for command in self._commands.values():
            self._io.write(command._print_info())
