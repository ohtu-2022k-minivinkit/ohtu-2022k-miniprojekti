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

    def read(self, input_command):
        """Read input from user"""
        self.__text = input(input_command)
        return self.__text


console_io = ConsoleIO()
