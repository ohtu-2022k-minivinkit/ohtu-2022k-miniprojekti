class ConsoleIO:
    '''class, moves input and output between class UI and os.

    Attributes:
        output: output to user
        input_command: input command to ask input from user
        __text: users answer to input command
    '''

    def __init__(self):
        self.__text = None
        self.output = None

    def write(self, output):
        self.output = output
        print(self.output)

    def read(self, input_command):
        self.__text = input(input_command)
        return self.__text


console_io = ConsoleIO()
