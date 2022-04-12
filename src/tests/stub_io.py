STUBIO__CLEAR_OUTPUTS = "__clear_outputs"


class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt):
        self.outputs.append(prompt)
        current_input = self.inputs.pop(0) if self.inputs else ""
        if current_input == STUBIO__CLEAR_OUTPUTS:
            self.clear_output()
            return self.inputs.pop(0) if self.inputs else ""
        return current_input

    def write_table(self, bookmarks):
        for i, bookmark in enumerate(bookmarks):
            self.outputs.append(
                f"{str(i+1)}: {bookmark.headline}, {bookmark.url}")

    def clear_output(self):
        self.outputs = []
