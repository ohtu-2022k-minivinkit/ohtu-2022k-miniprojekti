import unittest
from unittest.mock import Mock
from entities.bookmark import Bookmark
from services.bookmark_service import (
        BOOKMARK_RANGE__CHECKED, BookmarkService
)
from tests.stub_network_service import StubNetworkService
from tests.stub_io import StubIO, STUBIO__CLEAR_OUTPUTS
from ui.ui import UI


class TestUI(unittest.TestCase):
    def setUp(self):
        self.bookmark_service_mock = Mock(wraps=BookmarkService())
        self.network_service_mock = Mock(wraps=StubNetworkService(
            {"https://stub_url.fi": "otsikko"},
            {"12345": {"title": "kirja", "link": "https://stub_url.fi"}}
            )
        )

    def test_info_is_printed_when_started(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\nKomennot:\nx lopeta", in_out.outputs)

    def test_asks_command_after_start(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("komento: ", in_out.outputs)

    def test_choosing_command_not_in_commands_gives_error_message(self):
        in_out = StubIO(["0", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("virheellinen komento", in_out.outputs)

    def test_command_x_breaks_executing(self):
        in_out = StubIO(["x"])
        user_interface = UI(self.bookmark_service_mock,self.network_service_mock, in_out)
        user_interface.start()
        self.assertNotIn("virheellinen komento", in_out.outputs)

    def test_add_bookmark__command_1_moves_to_add_new_bookmark(self):
        in_out = StubIO(["1", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\nLisätään uusi vinkki, jos haluat palata valikkoon syötä x", in_out.outputs)

    def test_add_bookmark__asks_title_when_adding_bookmark(self):
        in_out = StubIO(["1", "http://not_working_link", "otsikko", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: ", in_out.outputs)

    def test_add_bookmark__asks_link_when_adding_bookmark(self):
        in_out = StubIO(["1", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_add_bookmark__no_title_given_gives_error_message(self):
        in_out = StubIO(["1", "https://stub_url.fi", "k", "", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)", in_out.outputs)

    def test_add_bookmark__too_long_title_gives_error_message(self):
        title = "t"*101
        in_out = StubIO(["1", "https://stub_url.fi", "k", title, "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)", in_out.outputs)

    def test_add_bookmark__correct_title_checks_correct(self):
        title = "t"*100
        in_out = StubIO(["1", "https://stub_url.fi", "k", title, "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: ", in_out.outputs)

    def test_add_bookmark__no_link_given_gives_error_message(self):
        in_out = StubIO(["1", "", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki oli virheellinen, anna otsikko ja linkki uudelleen", in_out.outputs)

    def test_add_bookmark__correct_link_checks_correct(self):
        in_out = StubIO(["1", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_add_bookmark__url_starting_incorrectly_gives_error_message(self):
        in_out = StubIO(["1", "ttps://stub_url.fi", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_too_short_url_gives_error_message(self):
        in_out = StubIO(["1", "http56789", "https://stub_url.fi", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("linkki: ", in_out.outputs)

    def test_list_all_bookmarks__command_2_shows_list_of_bookmarks(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "3", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("1 title1 link1 ei luettu", in_out.outputs)
        self.assertIn("2 title2 link2 ei luettu", in_out.outputs)

    def test_set_bookmark_checked__lists_unchecked_bookmarks(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "5", "x", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("1 title1 link1 ei luettu", in_out.outputs)
        self.assertIn("2 title2 link2 ei luettu", in_out.outputs)

    def test_set_bookmark_checked__asks_for_bookmark_number(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "5", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn(
            "\nMerkitse vinkki luetuksi antamalla vinkin numero (tai 'x' keskeyttääksesi): ",
            in_out.outputs)

    def test_list_bookmarks_by_keyword_command_5_asks_for_keyword(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "6", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Anna hakusana: ", in_out.outputs)

    def test_list_bookmarks_by_keyword_gives_correct_error_message_when_zero_matches(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "6", "hakusana", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Hakusanalla 'hakusana' ei löytynyt yhtään vinkkiä", in_out.outputs)

    def test_list_bookmarks_by_keyword_returns_correct_output_when_keyword_matches(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "6", "title", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.bookmark_service_mock.get_bookmarks_by_keyword.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Vinkit, jotka sisälsivät hakusanan 'title':", in_out.outputs)

    def test_set_bookmark_checked__too_small_number_gives_error_message(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "5", "0", "x", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\nVIRHE: Vinkkiä 0 ei ole!\n", in_out.outputs)

    def test_set_bookmark_checked__too_big_number_gives_error_message(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "5", "3", "x", "x"])
        bookmark1 = Bookmark("title1", "link1")
        bookmark2 = Bookmark("title2", "link2")
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\nVIRHE: Vinkkiä 3 ei ole!\n", in_out.outputs)

    def test_set_bookmark_checked__calls_bookmark_service_function_with_correct_id(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "5", "1", "x", "x"])
        bookmark1 = Bookmark("title1", "link1", False, database_id=5)
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.bookmark_service_mock.set_bookmark_as_checked.assert_called_once_with(5)

    def test_command_get_checked_bookmarks__calls_bookmark_service_with_correct_args(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "4", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.bookmark_service_mock.get_bookmarks_by_range.assert_called_with(
            BOOKMARK_RANGE__CHECKED
            )

    def test_command_get_checked_bookmarks__lists_checked_bookmarks(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "4", "x"])
        bookmark1 = Bookmark("title1", "link1", True, database_id=2)
        bookmark2 = Bookmark("title2", "link2", True, database_id=3)
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = [bookmark1, bookmark2]
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("1 title1 link1 luettu", in_out.outputs)
        self.assertIn("2 title2 link2 luettu", in_out.outputs)

    def test_gives_message_when_asked_checked_bookmarks__if_not_bookmarks_in_repository(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "4", "x"])
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = []
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Kirjastossa ei ole luettuja vinkkejä", in_out.outputs)

    def test_gives_message_when_asked_bookmarks__without_bookmarks_in_repository(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "3", "x"])
        self.bookmark_service_mock.get_bookmarks_by_range.return_value = []
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Kirjastossa ei ole vinkkejä", in_out.outputs)

    def test_add_book_with_isbn_commands_2_begins_adding_a_book(self):
        in_out = StubIO(["2", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\nLisätään uusi kirja, jos haluat palata valikkoon syötä x", in_out.outputs)
        self.assertIn("Anna ISBN-tunnus: ", in_out.outputs)

    def test_add_book_with_isbn_gets_title_with_working_isbn(self):
        in_out = StubIO(["2", "12345", "e", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: kirja", in_out.outputs)

    def test_add_book_with_isbn_title_can_be_edited(self):
        in_out = StubIO(["2", "12345", "k", "muokattu", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("otsikko: ", in_out.outputs)

    def test_add_book_with_isbn_fails_correctly_if_given_incorrect_isbn(self):
        in_out = StubIO(["2", "isbn", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("Kirjaa ei löytynyt.", in_out.outputs)

    def test_command_to_create_file_asks_filename(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "7", "x", "x"])
        def create_file(file_path):
            pass
        self.bookmark_service_mock.create_file.side_effect = create_file

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("tiedostonimi: ", in_out.outputs)

    def test_create_csv_file_calls_to_create_file_path(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "7", "", "", "x"])

        def create_file(file_path):
            pass
        self.bookmark_service_mock.create_file.side_effect = create_file

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()

        self.bookmark_service_mock.create_default_filepath.assert_called()

    def test_answer_not_overwrite_csv_file_asks_name_of_file_again(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "7", "file.csv", "", "e", "x", "x"])
        self.bookmark_service_mock.correct_filename.return_value = True
        self.bookmark_service_mock.create_default_filepath.return_value = "filepath/file.csv"
        self.bookmark_service_mock.exists.return_value = True

        def create_file(file_path):
            pass
        self.bookmark_service_mock.create_file.side_effect = create_file

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("kirjoita tiedostolle uusi nimi: ", in_out.outputs)

    def test_create_csv_file_wrong_path(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "7", "", "not-found", "x"])
        
        def create_file(file_path):
            pass
        self.bookmark_service_mock.create_file.side_effect = create_file

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\npolkua ei löytynyt, tiedosto sijoitetaan sovelluksen kansioon", in_out.outputs)

    def test_create_csv_file_calls_bookmark_service_to_create_file(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "7", "", "", "x"])

        def create_file(file_path):
            pass
        self.bookmark_service_mock.create_file.side_effect = create_file
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()

        self.bookmark_service_mock.create_file.assert_called()

    def test_command_to_load_file_asks_for_directory(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("csv-tiedoston hakemiston polku: ", in_out.outputs)

    def test_command_to_load_file_asks_for_filename(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("csv-tiedoston nimi: ", in_out.outputs)

    def test_command_to_load_file_directory_not_found(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "testi", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        self.bookmark_service_mock.exists.return_value = False
        user_interface.start()
        self.assertIn("\npolkua ei löytynyt", in_out.outputs)

    def test_command_to_load_file_directory_not_found(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "testi", "x", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\npolkua ei löytynyt", in_out.outputs)

    def test_command_to_load_file_file_not_found(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "", "not-found", "x"])
        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)
        user_interface.start()
        self.assertIn("\ntiedostoa ei löytynyt", in_out.outputs)

    def test_command_to_load_file_file_loaded(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "", "found", "x"])

        def load_file(file_path):
            return True
        self.bookmark_service_mock.load_file.side_effect = load_file
        self.bookmark_service_mock.exists.return_value = True

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)

        user_interface.start()
        self.assertIn("\nkirjanmerkit ladattiin tiedostosta \n", in_out.outputs)

    def test_command_to_load_file_file_not_loaded(self):
        in_out = StubIO([STUBIO__CLEAR_OUTPUTS, "8", "", "found", "x"])

        def load_file(file_path):
            return False
        self.bookmark_service_mock.load_file.side_effect = load_file
        self.bookmark_service_mock.exists.return_value = True

        user_interface = UI(self.bookmark_service_mock, self.network_service_mock, in_out)

        user_interface.start()
        self.assertIn("\ntiedosto on virheellinen", in_out.outputs)
