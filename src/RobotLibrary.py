# pylint: skip-file
from ui.ui import UI
from tests.stub_io import StubIO
from services.bookmark_service import BookmarkService


class RobotLibrary:
    def __init__(self):
        self._io = StubIO()
        self._bookmark_service = BookmarkService()
        self._ui = UI(self._bookmark_service, self._io)

    def ui_start(self):
        self._ui.start()

    def command_line_input(self, value):
        self._io.inputs += [value]

    def command_line_clear_output(self):
        self._io.outputs.clear()

    def command_line_clear_input(self):
        self._io.inputs.clear()

    def command_line_output_should_contain(self, value):
        outputs = self._io.outputs
        if value not in outputs:
            raise AssertionError(
                f"\"{value}\" is not in {str(outputs)}"
            )

    def command_line_output_should_not_contain(self, value):
        outputs = self._io.outputs
        if value in outputs:
            raise AssertionError(
                f"\"{value}\" is in {str(outputs)}"
            )

    def command_line_output_should_be(self, value):
        outputs = self._io.outputs
        if value != str(outputs):
            raise AssertionError(
                f"\"{value}\" is not {str(outputs)}"
            )
