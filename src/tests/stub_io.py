STUBIO__CLEAR_OUTPUTS = "__clear_outputs"
from typing_extensions import Self
import unittest
from unittest.mock import Mock
from entities.bookmark import Bookmark
from services.bookmark_service import BookmarkService
from ui.ui import UI
from rich.console import Console
from rich.table import Table
from io import StringIO
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class StubIO:
    """Stub class to be used instead of ConsoleIO in tests.

    See ConsoleIO for more information.

    Attributes:
        inputs: Strings faking to be input from user.
        outputs: Output strings from the program under test.
    """

    def __init__(self, inputs=None):
        """Initializes StubIO with fake input."""
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        """Captures output from program under test to self.outputs.

        See ConsoleIO.write().

        Args:
            value (string): Output from program under test.
        """
        self.outputs.append(value)

    def read(self, prompt) -> str:
        """Returns fake input from self.inputs.

        Returns fake input from self.inputs and adds prompt string to
        self.outputs. See ConsoleIO.read().

        Output list (self.outputs) can be cleared by adding command
        '__clear_outputs' to input list in initialization. Command
        should be added using constant STUBIO__CLEAR_OUTPUTS.

        Args:
            prompt (string): Prompt string from program under test.

        Returns:
            str: String faking input from user.
        """
        self.outputs.append(prompt)
        current_input = self.inputs.pop(0) if self.inputs else ""
        if current_input == STUBIO__CLEAR_OUTPUTS:
            self.outputs = []
            return self.inputs.pop(0) if self.inputs else ""
        return current_input

    '''
    def write_table(self, bookmarks: list):
        """Appends table rows to self.outputs as strings.

        See ConsoleIO.write_table().
        """
        for i, bookmark in enumerate(bookmarks):
            self.outputs.append(
                f"{str(i+1)}: {bookmark.headline}, {bookmark.url}")

    '''
    def write_table(self, bookmarks):
        id = 0
        """Write table to user"""
        self.bookmarks = bookmarks
        table = Table(title="Bookmarks")
        table.add_column("id", style="green")
        table.add_column("title", style="cyan")
        table.add_column("link", style="magenta")

        #for bookmark in self.bookmarks:
        #    id += 1
        #    table.add_row(str(id), bookmark.headline, bookmark.url)
        #    with Capturing(self.outputs) as self.outputs:
        #        print(str(id), bookmark.headline, bookmark.url)

        for i, bookmark in enumerate(bookmarks):
            if bookmark.checked == 1:
                luettu = "luettu"
            else:
                luettu = "ei luettu"
            table.add_row(str(i+1), str(bookmark.headline), str(bookmark.url), str(luettu))
            #with Capturing(self.outputs) as self.outputs:
            #    print(str(i+1), str(bookmark.headline), str(bookmark.url), str(luettu))

        console = Console()
        with Capturing(self.outputs) as self.outputs:
            console.print(table)
