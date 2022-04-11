# pylint: skip-file
class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, input_command):
        self.inputs += [input_command]
        return self.inputs.pop(0) if self.inputs else ""

    def write_table(self, bookmarks):
        for i, bookmark in enumerate(bookmarks):
            self.outputs.append(
                f"{str(i+1)}: {bookmark.headline}, {bookmark.url}")
    