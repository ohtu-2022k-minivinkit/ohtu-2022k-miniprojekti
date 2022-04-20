import pyshorteners

class AddBookWithISBN:
    def __init__(self, i_o, bookmark_service, network_service):
        """Initializes command with IO, BookmarkService and NetworkService.

        Args:
            i_o (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
            network_service (class, optional):
                Service class containing network logic.
        """
        self._io = i_o
        self._bookmark_service = bookmark_service
        self._network_service = network_service

    def __str__(self):
        return "lisää kirja ISBN-tunnuksella"

    def execute(self):
        """Executes command."""
        isbn = self._io.read("\nAnna ISBN-tunnus: ")

        if isbn == "x":
            return

        book = self._network_service.get_book_by_isbn(isbn)

        if book is None:
            self._io.write("Kirjaa ei löytynyt.")
            return

        url_shortener = pyshorteners.Shortener()

        title = book["title"]

        self._io.write(f"otsikko: {title}")
        edit = self._io.read("Muokkaa otsikkoa? (k/e): ")

        if edit == "k":
            title = self._io.read("otsikko: ")

        link = url_shortener.tinyurl.short(book["link"])

        self._bookmark_service.create_bookmark(title, link)
