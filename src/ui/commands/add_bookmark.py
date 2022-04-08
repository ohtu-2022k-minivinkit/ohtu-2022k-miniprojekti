from ui.bookmark_validation import BookmarkValidation


class AddBookmark:
    def __init__(self, io, bookmark_service, validator):
        """Initializes command with IO, BookmarkService and validator object.

        Args:
            io (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
            validator (BookmarkValidation):
                Object with methods to validate user input.
        """
        self._io = io
        self._bookmark_service = bookmark_service
        self._validator = validator

    def __str__(self):
        return "lisää vinkki"

    def execute(self):
        """Executes command."""
        self._io.write("\nLisätään uusi vinkki")

        title = self._io.read("otsikko: ")
        if not self._validator.check_title(title):
            self.execute()

        link = self._io.read("linkki: ")
        if not self._validator.check_link(link):
            self.execute()

        self._bookmark_service.create_bookmark(title, link)
