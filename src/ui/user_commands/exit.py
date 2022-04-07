from ui.user_commands.user_command import UserCommand

class Exit(UserCommand):
    """prints info"""

    def __init__(self):
        super().__init__()

    def _print_info(self):
        return "x lopeta"
    
    def _execute(self):
        pass
