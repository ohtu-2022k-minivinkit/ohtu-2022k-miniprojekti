import unittest
from unittest.mock import Mock
from entities.bookmark import Bookmark
from services.bookmark_service import BookmarkService
from ui.ui import UI
from tests.stub_io import StubIO, STUBIO__CLEAR_OUTPUTS


class TestUI(unittest.TestCase):
    def setUp(self):
        self.service_mock = Mock(wraps=BookmarkService())

    def test_info_is_printed_when_started(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("\nKomennot:\nx lopeta", in_out.outputs)

    def test_asks_command_after_start(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("komento: ", in_out.outputs)

    def test_choosing_command_not_in_commands_gives_error_message(self):
        in_out = StubIO(["0", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("virheellinen komento", in_out.outputs)

    def test_command_x_breaks_executing(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertNotIn("virheellinen komento", in_out.outputs)

    def test_add_bookmark__command_1_moves_to_add_new_bookmark(self):
        in_out = StubIO(["1", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("\nLisätään uusi vinkki, jos haluat palata valikkoon syötä x", in_out.outputs)

    def test_add_bookmark__asks_title_when_adding_bookmark(self):
        in_out = StubIO(["1", "http://not_working_link", "otsikko", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: ", in_out.outputs)

    def test_add_bookmark__asks_link_when_adding_bookmark(self):
        in_out = StubIO(["1", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_add_bookmark__no_title_given_gives_error_message(self):
        in_out = StubIO(["1", "https://helsinki.fi", "k", "", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)", in_out.outputs)

    def test_add_bookmark__too_long_title_gives_error_message(self):
        title = "t"*101
        in_out = StubIO(["1", "https://helsinki.fi", "k", title, "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)", in_out.outputs)

    def test_add_bookmark__correct_title_checks_correct(self):
        title = "t"*100
        in_out = StubIO(["1", "https://helsinki.fi", "k", title, "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: ", in_out.outputs)

    def test_add_bookmark__no_link_given_gives_error_message(self):
        in_out = StubIO(["1", "", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki oli virheellinen, anna otsikko ja linkki uudelleen", in_out.outputs)

    def test_add_bookmark__correct_link_checks_correct(self):
        in_out = StubIO(["1", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_add_bookmark__url_starting_incorrectly_gives_error_message(self):
        in_out = StubIO(["1", "ttps://helsinki.fi", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_too_short_url_gives_error_message(self):
        in_out = StubIO(["1", "http56789", "https://helsinki.fi", "e", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_list_all_bookmarks__command_2_shows_list_of_bookmarks(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "2", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("1: title1, link1", in_out.outputs)
        self.assertIn("2: title2, link2", in_out.outputs)

    def test_set_bookmark_checked__lists_unchecked_bookmarks(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "4", "x", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn("1: title1, link1", in_out.outputs)
        self.assertIn("2: title2, link2", in_out.outputs)

    def test_set_bookmark_checked__asks_for_bookmark_number(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "4", "x", "x"])
        user_interface = UI(self.service_mock, in_out)
        user_interface.start()
        self.assertIn(
            "\nMerkitse vinkki luetuksi antamalla vinkin numero (tai 'x' keskeyttääksesi): ",
            in_out.outputs)
