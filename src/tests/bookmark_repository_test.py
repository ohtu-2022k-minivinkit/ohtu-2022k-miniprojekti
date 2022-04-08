import unittest
from repositories.bookmark_repository import bookmark_repository
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

        bookmarks = bookmark_repository.get_bookmarks("Tes")
        self.assertEqual(len(bookmarks), 2)

    def test_get_bookmarks_ignore_case(self):
        bookmark_repository.create(self.bookmark_1)
        bookmark_repository.create(self.bookmark_2)

        bookmarks = bookmark_repository.get_bookmarks("ES")
        self.assertEqual(len(bookmarks), 2)

    def test_get_bookmarks_checked_with_param_0_as_not_checked_gets_not_checked_bookmarks(self):
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", True))
        bookmarks = bookmark_repository.get_bookmarks_checked_status(0)

        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0].checked, 0)

    def test_get_bookmarks_checked_with_param_1_as_checked_gets_checked_bookmarks(self):
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", False))
        bookmark_repository.create(Bookmark("headline", "url", True))
        bookmarks = bookmark_repository.get_bookmarks_checked_status(1)

        self.assertEqual(len(bookmarks), 1)
        self.assertEqual(bookmarks[0].checked, 1)
