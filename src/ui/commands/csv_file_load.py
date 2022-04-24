class LoadCsvFile:
    def __init__(self, i_o, bookmark_service):
        """Initializes command with IO and BookmarkService object.

        Args:
            i_o (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = i_o
        self._bookmark_service = bookmark_service

    def __str__(self):
        return "lataa csv -tiedosto"

    def execute(self):
        """Executes command."""
