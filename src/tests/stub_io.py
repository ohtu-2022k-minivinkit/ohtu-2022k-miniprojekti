# pylint: skip-file
from io import StringIO
from collections import deque
from rich.console import Console
from ui.console_io import ConsoleIO


STUBIO__CLEAR_OUTPUTS = "__clear_outputs"


class StubIO(ConsoleIO):
    """Stub class to be used instead of ConsoleIO in tests.

    See ConsoleIO for more information.

    Attributes:
        inputs: Strings faking to be input from user.
        outputs: Output strings from the program under test.
    """

    def __init__(self, inputs=None):
        """Initializes StubIO with fake input.

        Initializes object with list of fake input strings and Rich library
        console object self._console with StringIO. Latter makes rich console
        output readable as plain strings.
        """
        self.inputs = inputs or deque()
        if not isinstance(self.inputs, deque):
            self.inputs = deque(self.inputs)
        self.outputs = deque()
        self._console = Console(file=StringIO())

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
        current_input = self.inputs.popleft() if self.inputs else ""
        if current_input == STUBIO__CLEAR_OUTPUTS:
            self.outputs = deque()
            self._console.file.truncate(0)
            self._console.file.seek(0)
            return self.inputs.popleft() if self.inputs else ""
        return current_input

    def write_table(self, bookmarks: list):
        """Appends table rows to self.outputs as strings.

        See ConsoleIO.write_table().
        """
        super().write_table(bookmarks)
        line_list = self._console.file.getvalue().splitlines()
        for line_str in line_list:
            self.outputs.append(" ".join(line_str.split()))
