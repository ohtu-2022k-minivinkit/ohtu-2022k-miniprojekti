from rich.console import Console
from rich.table import Table

class ConsoleIO:
    """class, moves input and output between class UI and os.
    Use write similar as print and read similar as input.

    Attributes:
        output: output to user
        __text: users answer to input command
    """

    def __init__(self):
        self.__text = None
        self.output = None

    def write(self, output):
        """Write output to user"""
        self.output = output
        print(self.output)

    def write_table(self, bookmarks):
        """Write table to user"""
        table = Table(title="Bookmarks")
        table.add_column("#", style="green")
        table.add_column("title", style="cyan")
        table.add_column("link", style="magenta")

        for i, bookmark in enumerate(bookmarks):
            table.add_row(str(i+1), bookmark.headline, bookmark.url)

        console = Console()
        console.print(table)

    def read(self, input_command):
        """Read input from user"""
        self.__text = input(input_command)
        return self.__text


console_io = ConsoleIO()
