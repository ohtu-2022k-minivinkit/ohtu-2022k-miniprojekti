import unittest
from repositories.bookmark_repository import bookmark_repository
from services.bookmark_service import bookmark_service
from entities.bookmark import Bookmark

class TestBookmarkRepository(unittest.TestCase):
    def setUp(self):
        bookmark_repository.delete_all()
        self.bookmark_1 = Bookmark("Testausta", "www.testausta.fi")
        self.bookmark_2 = Bookmark("Lisää testausta", "www.lisaatestausta.fi")

    def test_create(self):
        bookmark_repository.create(self.bookmark_1)
        bookmark_repository.create(self.bookmark_2)

        bookmarks = bookmark_repository.get_all()

        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0].headline, "Testausta")
        self.assertEqual(bookmarks[1].url, "www.lisaatestausta.fi")

    def test_get_all(self):
        bookmark_repository.create(self.bookmark_1)
        bookmark_repository.create(self.bookmark_2)

        bookmarks = bookmark_repository.get_all()

        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0].headline, "Testausta")
        self.assertEqual(bookmarks[0].url, "www.testausta.fi")
        self.assertEqual(bookmarks[1].headline, "Lisää testausta")
        self.assertEqual(bookmarks[1].url, "www.lisaatestausta.fi")

    def test_get_bookmarks(self):
        bookmark_repository.create(self.bookmark_1)
        bookmark_repository.create(self.bookmark_2)

        bookmarks = bookmark_repository.get_by_keyword("Tes")
        self.assertEqual(len(bookmarks), 2)

    def test_get_bookmarks_ignore_case(self):
        bookmark_repository.create(self.bookmark_1)
        bookmark_repository.create(self.bookmark_2)

        bookmarks = bookmark_repository.get_by_keyword("ES")
        self.assertEqual(len(bookmarks), 2)

    def test_get_bookmarks_checked_with_param_0_as_not_checked__gets_not_checked_bookmarks(self):
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", True))

        bookmarks = bookmark_repository.get_by_checked(0)
        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0].checked, 0)

    def test_get_bookmarks_checked_with_param_1_as_checked__gets_checked_bookmarks(self):
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", True))

        bookmarks = bookmark_repository.get_by_checked(1)
        self.assertEqual(len(bookmarks), 1)
        self.assertEqual(bookmarks[0].checked, 1)

    def test_set_as_checked(self):
        bookmark_repository.create(Bookmark("1, headline", "url", False))
        bookmark_repository.create(Bookmark("2, headline", "url", False))

        bookmark_repository.set_as_checked(bookmark_id=2)

        bookmarks = bookmark_repository.get_by_checked(1)
        self.assertEqual(len(bookmarks), 1)
        self.assertEqual(bookmarks[0].database_id, 2)

    def test_create_csv_file__writes_all_headlines_and_links_in_file(self):
        bookmark_repository.create(Bookmark("headline1", "url1", False))
        bookmark_repository.create(Bookmark("headline2", "url2", False))
        bookmark_repository.create(Bookmark("headline3", "url3", True))
        file_path = bookmark_service.create_default_filepath("test-file.csv").replace(
            "csv_files","data"
            )
        bookmark_repository.create_csv_file(file_path)

        self.assertTrue(bookmark_service.exists(file_path))
        content = bookmark_repository.read_file(file_path)
        self.assertIn("headline1", content)
        self.assertIn("url3", content)
        bookmark_repository.delete_all_file_content(file_path)

    def test_load_csv_file_loads_all_bookmarks_in_file(self):
        file_path = bookmark_service.create_default_filepath("test-file.csv").replace(
            "csv_files","data"
            )
        data = ("otsikko;linkki""\n"
            "headline1;url1""\n"
            "headline2;url2""\n")
        bookmark_repository.delete_all_file_content(file_path)
        bookmark_repository.create_file(file_path, data)
        self.assertTrue(bookmark_service.exists(file_path))
        bookmark_repository.load_csv_file(file_path)

        bookmarks = bookmark_repository.get_all()
        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0].headline, "headline1")
        self.assertEqual(bookmarks[1].url, "url2")
        bookmark_repository.delete_all_file_content(file_path)
    
    def test_load_csv_file_returns_true_when_successful(self):
        file_path = bookmark_service.create_default_filepath("test-file.csv").replace(
            "csv_files","data"
            )
        data = ("otsikko;linkki""\n")
        bookmark_repository.delete_all_file_content(file_path)
        bookmark_repository.create_file(file_path, data)
        self.assertTrue(bookmark_service.exists(file_path))
        self.assertTrue(bookmark_repository.load_csv_file(file_path))
        bookmark_repository.delete_all_file_content(file_path)

    def test_load_csv_file_returns_false_when_unsuccessful(self):
        file_path = bookmark_service.create_default_filepath("test-file.csv").replace(
            "csv_files","data"
            )
        data = ("unvalid")
        bookmark_repository.delete_all_file_content(file_path)
        bookmark_repository.create_file(file_path, data)
        self.assertTrue(bookmark_service.exists(file_path))
        self.assertFalse(bookmark_repository.load_csv_file(file_path))
        bookmark_repository.delete_all_file_content(file_path)

