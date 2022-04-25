# pylint: skip-file
from robot.api.deco import keyword
from ui.ui import UI
from tests.stub_io import StubIO, STUBIO__CLEAR_OUTPUTS
from tests.stub_network_service import StubNetworkService
from services.bookmark_service import BookmarkService
from services.network_service import NetworkService


class RobotLibrary:
    ROBOT_AUTO_KEYWORDS = False
    def __init__(self, network_setting=None, input_string=None):
        self._io = StubIO()
        self._bookmark_service = BookmarkService()

        self._title_returning_urls = {}
        
        if input_string:
            self._input_string_validator(input_string)

        if network_setting == "network":
            self._ui = UI(self._bookmark_service, NetworkService(), self._io)
        else:
            self._ui = UI(self._bookmark_service, StubNetworkService(self._title_returning_urls), self._io)

    def _input_string_validator(self, value):
        values = value.split(" ")
        if values[0] == "url_title_pairs":
            self._title_returning_urls_splitter(values[1:])
        else:
            raise ValueError(
                f"\"{values[0]}\" is not known input type"
            )

    def _title_returning_urls_splitter(self, values):
        if len(values)%2 != 0:
            raise ValueError(
                f"\"{values}\" is not suitable for key-value pairing"
            )
        for i in range(1,len(values),2):
            self._title_returning_urls[values[i-1]] = values[i]

    @keyword
    def ui_start(self):
        self._ui.start()

    @keyword
    def command_line_input(self, value):
        self._io.inputs += [value]

    @keyword
    def command_line_clear_output(self):
        self._io.outputs.clear()

    @keyword
    def command_line_clear_input(self):
        self._io.inputs.clear()

    @keyword
    def command_line_clear_output_with_stubio_input(self):
        self._io.inputs += [STUBIO__CLEAR_OUTPUTS]

    @keyword
    def command_line_output_should_contain(self, value):
        outputs = self._io.outputs
        if value not in outputs:
            raise AssertionError(
                f"\"{value}\" is not in {str(outputs)}"
            )

    @keyword
    def command_line_output_should_not_contain(self, value):
        outputs = self._io.outputs
        if value in outputs:
            raise AssertionError(
                f"\"{value}\" is in {str(outputs)}"
            )

    @keyword
    def command_line_output_should_be(self, value):
        outputs = self._io.outputs
        if value != str(outputs):
            raise AssertionError(
                f"\"{value}\" is not {str(outputs)}"
            )

    @keyword
    def command_line_output_count_of_bookmarks(self, value):
        outputs = self._io.outputs
        bookmarks_count = 0
        for output_line in outputs:
            bookmarks_count += output_line.count("http")
        if int(value) != bookmarks_count:
            raise AssertionError(
                f"\"{value}\" is not {bookmarks_count}"
            )

    @keyword
    def file_should_contain(self, file_path, value):
        with open(file_path) as file:
            content = file.read()
        if value not in content:
            raise AssertionError(
                f"\"{value}\" is not in {content}"
            )

    @keyword
    def file_should_not_contain(self, file_path, value):
        with open(file_path) as file:
            content = file.read()
        if value in content:
            raise AssertionError(
                f"\"{value}\" is in {content}"
            )

    @keyword
    def create_test_csv_file(self, file_path, data):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
