class BookmarkValidation:
    def __init__(self, console_io):
        """Initializes object with IO object.

        Args:
            console_io (class, optional):
                Object providing IO methods (read() and write()). Defaults
                to default_console_io.
        """
        self._io = console_io

    def check_title(self, input):
        """Validates user input for title.

        Args:
            input (string): User input.
        """
        input = input.strip()
        if not input or len(input) > 100:
            self._io.write("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")
            return False
        return True

    def check_link(self, input):
        """Validates user input for link.

        Args:
            input (string): User input.
        """
        if len(input.strip()) < 12 or input[:4] != "http" or " " in input.strip():
            self._io.write("linkki oli virheellinen, anna otsikko ja linkki uudelleen")
            return False
        return True
