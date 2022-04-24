class AddBookmark:
    def __init__(self, i_o, bookmark_service, network_service, validator):
        """Initializes command with IO, BookmarkService, NetworkService and validator object.

        Args:
            i_o (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
            network_service (class, optional):
                Service class containing network logic.
            validator (BookmarkValidation):
                Object with methods to validate user input.
        """
        self._io = i_o
        self._bookmark_service = bookmark_service
        self._network_service = network_service
        self._validator = validator

    def __str__(self):
        return "lisää vinkki"

    def execute(self):
        """Executes command."""
        self._io.write("\nLisätään uusi vinkki, jos haluat palata valikkoon syötä x")

        link = self._io.read("linkki: ")

        if link != "x":
            if not self._validator.check_link(link):
                self.execute()
                return

            title = self._network_service.get_url_title(link)

            if not title:
                title = self._io.read("otsikko: ")
            else:
                self._io.write(f"otsikko: {title}")
                edit = self._io.read("Muokkaa otsikkoa? (k/e): ")

                if edit == "k":
                    title = self._io.read("otsikko: ")

            if not self._validator.check_title(title):
                self.execute()
                return

            shortened_link = self._network_service.shorten_url(link)

            if shortened_link:
                link = shortened_link

            self._bookmark_service.create_bookmark(title, link)
