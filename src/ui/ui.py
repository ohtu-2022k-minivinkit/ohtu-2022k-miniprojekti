class ConsoleIO:
    def write(self, text):
        print(text)

    def read(self, text):
        text = input(text)
        return text
        
        
COMMANDS = {
    "x": "x lopeta",
    "1": "1 lisää vinkki"
}

class UI:
    def __init__(self, service, io=ConsoleIO()):
        self._io = io
        self._bookmarks_service = service

    def start(self):
        self._io.write("")
        self._io.write("Bookmarks komennot:")
        self._print_info()

        while True:
            self._io.write("")
            command = self._io.read("komento: ")
            if not command in COMMANDS:
                self._io.write("virheellinen komento")
                self._print_info()
                continue

            if command == "x":
                break
            elif command == "1":
                self._add_bookmark()

    def _print_info(self):
        [self._io.write(command) for command in COMMANDS.values()]

    def _add_bookmark(self):
        self._io.write("Lisätään uusi vinkki")
        title = self._io.read("title: ")
        link = self._io.read("link:")
        #tähän logiikan metodiin kutsu, esim. self._service._add_bookmark(title, link)?
        #ja tarvitaan vielä myös virheviesti
        