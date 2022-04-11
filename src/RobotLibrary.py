# pylint: skip-file
from ui.ui import UI
from tests.stub_io import StubIO
from tests.stub_network_service import StubNetworkService
from services.bookmark_service import BookmarkService
from services.network_service import NetworkService


class RobotLibrary:
    def __init__(self, network_setting="stub"):
        self._io = StubIO()
        self._bookmark_service = BookmarkService()

        if network_setting == "network":
            self._ui = UI(self._bookmark_service, NetworkService(), self._io)
        else:
            returning_urls = {}
            returning_urls["http://www.returning.com"] = "Returning"

            self._ui = UI(self._bookmark_service, StubNetworkService(returning_urls), self._io)

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

    def command_line_output_count_of_bookmarks(self, value):
        outputs = self._io.outputs
        bookmarks_count = 0
        for output_line in outputs:
            bookmarks_count += output_line.count("http")
        if int(value) != bookmarks_count:
            raise AssertionError(
                f"\"{value}\" is not {bookmarks_count}"
            )
