class BookmarkValidation:
    def __init__(self, console_io):
        """Initializes object with IO object.

        Args:
            console_io (class, optional):
                Object providing IO methods (read() and write()). Defaults
                to default_console_io.
        """
        self._io = console_io

    def check_title(self, user_input):
        """Validates user input for title.

        Args:
            input (string): User input.
        """
        user_input = user_input.strip()
        if not user_input or len(user_input) > 100:
            self._io.write(
                "otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")
            return False
        return True

    def check_link(self, user_input):
        """Validates user input for link.

        Args:
            input (string): User input.
        """
        if len(user_input.strip()) < 12 or user_input[:4] != "http"\
                or " " in user_input.strip():
            self._io.write(
                "linkki oli virheellinen, anna otsikko ja linkki uudelleen")
            return False
        return True
