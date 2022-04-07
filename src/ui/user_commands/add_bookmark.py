from ui.user_commands.user_command import UserCommand

class AddBookmark(UserCommand):
    
    def __init__(self):
        super().__init__()

    def _print_info(self):
        "prints command info to user to see."
        
        return "1 lisää vinkki"

    def _execute(self):
        """class Asks for title and link inputs from user.

        If user's input is valid,
        calls Bookmark_service class to create bookmark and add
        it into the repository.

        If input is not valid, executing will return to the
        while -loop in the method start.
        """
        
        self._io.write("Lisätään uusi vinkki")

        title = self._io.read("otsikko: ")
        if not self._feed_validation._check_title(title):
            self._execute()

        link = self._io.read("linkki: ")
        if not self._feed_validation._check_link(link):
            self._execute()

        self._bookmark_service.create_bookmark(title, link)
