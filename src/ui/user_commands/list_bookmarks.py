from ui.user_commands.user_command import UserCommand

class ListBookmarks(UserCommand):
    
    def __init__(self, choice):
        super().__init__()
        """inherits attributes from superclass 
            and prints not read bookmarks to user to see"""
        
        self._choice = choice
        
        if self._choice == "not read":
            self._execute()

    def _print_info(self):
        """prints command info to user to see 
            (chosen in the constructor)"""
        
        if self._choice == "all":
            return "2 näytä kaikki vinkit"
        
        if self._choice == "read":
            return "3 näytä luetut"

    def _execute(self):
        """Prints chosen range of bookmarks stored in the repository."""
        
        bookmark_list = self._bookmark_service.get_bookmarks(self._choice)
        if bookmark_list:  
            for bookmark in bookmark_list:
                self._io.write(f'{bookmark}')
