import unittest
from unittest.mock import Mock
from services.bookmark_service import (
    BOOKMARK_RANGE__ALL, BOOKMARK_RANGE__CHECKED, BOOKMARK_RANGE__UNCHECKED,
    BookmarkService
)
from entities.bookmark import Bookmark


class TestBookmarkService(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.bookmark_service = BookmarkService(self.repository_mock)

    def test_create_method_of_repository_is_called(self):
        self.bookmark_service.create_bookmark("otsikko", "http://linkki.fi")
        self.repository_mock.create.assert_called_once()

    def test_create_method_of_repository_is_called_with_correct_parameters(self):
        self.bookmark_service.create_bookmark("otsikko", "http://linkki.fi")
        self.assertTrue(isinstance(self.repository_mock.create.call_args.args[0], Bookmark))

    def test_when_list_of_bookmarks_contains_two_bookmark_delivered_list_length_is_two(self):
        bookmark = Bookmark("headline","link")
        self.repository_mock.get_all.return_value = [bookmark, bookmark]
        bookmarks = self.bookmark_service.get_bookmarks_by_range(BOOKMARK_RANGE__ALL)
        self.assertEqual(len(bookmarks),2)

    def test_method_get_all_bookmarks_delivers_bookmarks(self):
        bookmark = Bookmark("headline","link")
        self.repository_mock.get_all.return_value = [bookmark, bookmark]
        bookmarks = self.bookmark_service.get_bookmarks_by_range(BOOKMARK_RANGE__ALL)
        self.assertEqual(bookmarks[1].headline,"headline")

    def test_get_bookmarks_called_with_correct_params(self):
        self.bookmark_service.create_bookmark("headline", "link")
        self.bookmark_service.get_bookmarks_by_keyword("ead")

        self.repository_mock.get_by_keyword.assert_called_with("ead")

    def test_when_asked_not_checked_bookmarks_calls_for_not_checked_from_repository(self):
        self.bookmark_service.get_bookmarks_by_range(BOOKMARK_RANGE__UNCHECKED)
        self.repository_mock.get_by_checked.assert_called_with(0)

    def test_when_asked_checked_bookmarks_calls_for_checked_from_repository(self):
        self.bookmark_service.get_bookmarks_by_range(BOOKMARK_RANGE__CHECKED)
        self.repository_mock.get_by_checked.assert_called_with(1)

    def test_when_asked_all_bookmarks_calls_for_all_from_repository(self):
        self.bookmark_service.get_bookmarks_by_range(BOOKMARK_RANGE__ALL)
        self.repository_mock.get_all.assert_called_with()

    def test_calls_bookmark_repository_to_check_bookmark(self):
        self.bookmark_service.set_bookmark_as_checked(2)
        self.repository_mock.set_as_checked.assert_called_with(2)
