from ui.console_io import (
console_io as default_console_io
)

class FeedValidation:
    def __init__(self, console_io = default_console_io):
        self._io = console_io
        self._error = False

    def _check_title(self, title):
        """Validates user input for title.

        if user's input is not valid, prints an error message
        and places True in the variable self._error.

        Args:
        title (string): user's input for title
        """
        
        title = title.strip()
        if not title or len(title) > 100:
            self._io.write("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)")
            return False
        return True

    def _check_link(self, link):
        """Validates user input for link.

        if user's input is not valid, prints an error message
        and places True in the variable self._error.

        Args:
        link (string): user's input for link
        """
        
        if len(link.strip()) < 12 or link[:4] != "http" or " " in link.strip():
            self._io.write("linkki oli virheellinen, anna otsikko ja linkki uudelleen")
            return False
        return True

feed_validation = FeedValidation()
