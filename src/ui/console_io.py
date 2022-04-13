from rich.console import Console
from rich.table import Table


class ConsoleIO:
    def __init__(self):
        self._console = Console()

    @classmethod
    def write(cls, output):
        """Prints output to stdout."""
        print(output)

    @classmethod
    def read(cls, input_command):
        """Read input from stdin."""
        return input(input_command)

    def write_table(self, bookmarks: list):
        """Prints list of Bookmarks to stdout as a Rich.Table.

        Args:
            bookmarks (list): List of Bookmark objects.
        """
        table = Table(box=None)
        table.add_column("#", style="green")
        table.add_column("otsikko", style="cyan")
        table.add_column("linkki", style="magenta")
        table.add_column("luettu", style="green")

        for i, bookmark in enumerate(bookmarks):
            luettu = "luettu" if bookmark.checked == 1 else "ei luettu"
            table.add_row(str(i+1), str(bookmark.headline), str(bookmark.url), luettu)

        self._console.print(table)


console_io = ConsoleIO()
