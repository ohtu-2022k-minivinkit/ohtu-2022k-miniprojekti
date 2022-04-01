import unittest
from unittest.mock import Mock, ANY
from entities.bookmark import Bookmark
from ui.ui import UI
from services.bookmark_service import BookmarkService

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, input_command):
        self.inputs += [input_command]
        return self.inputs.pop(0) if self.inputs else ""

class TestUI(unittest.TestCase):
    def setUp(self):
        self.service_mock = Mock()

    def test_info_is_printed_when_started(self):
        io = StubIO(["x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("x lopeta",io.outputs)

    def test_asks_command_after_start(self):
        io = StubIO(["x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("komento: ",io.inputs[0])

    def test_choosing_command_not_in_commands_gives_error_message(self):
        io = StubIO(["0", "x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("virheellinen komento",io.outputs)

    def test_command_x_breaks_executing(self):
        io = StubIO(["x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertNotIn("virheellinen komento",io.outputs)

    def test_command_1_moves_to_add_new_bookmark(self):
        io = StubIO(["1","","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("Lisätään uusi vinkki",io.outputs)
    
    def test_asks_title_when_adding_bookmark(self):
        io = StubIO(["1","","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("otsikko: ",io.inputs)

    def test_asks_link_when_adding_bookmark(self):
        io = StubIO(["1","title","","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("linkki: ",io.inputs)

    def test_not_title_given_gives_error_message(self):
        io = StubIO(["1","","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)",io.outputs)
    
    def test_title_too_long_gives_error_message(self):
        title = "t"*101
        io = StubIO(["1",title,"x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)",io.outputs)
    
    def test_correct_title_checks_correct(self):
        title = "t"*100
        io = StubIO(["1",title,"","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("otsikko: ",io.inputs)

    def test_not_link_given_gives_error_message(self):
        io = StubIO(["1","title","","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("linkki oli virheellinen, anna otsikko ja linkki uudelleen",io.outputs)
    
    def test_correct_link_checks_correct(self):
        io = StubIO(["1","title","http_5-6./","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("linkki: ",io.inputs)

    def test_url_starting_incorrectly_gives_error_message(self):
        io = StubIO(["1","title","ttp_5-6./1","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("linkki: ",io.inputs)

    def test_too_short_url_gives_error_message(self):
        io = StubIO(["1","title","http56789","x"])
        ui = UI(self.service_mock, io)
        ui.start()
        self.assertIn("linkki: ",io.inputs)

    def test_creates_list_of_bookmarks(self):
        io = StubIO()
        ui = UI(self.service_mock, io)
        bookmark = Bookmark("title", "link")
        self.service_mock.get_all_bookmarks.return_value = [bookmark, bookmark]
        ui._list_bookmarks()
        self.assertIn("title link\n",io.outputs)
