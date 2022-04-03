import unittest
from unittest.mock import Mock
from services.bookmark_service import BookmarkService
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
