import unittest
from services.network_service import NetworkService

class TestNetworkRequest(unittest.TestCase):
    def setUp(self):
        self._network_service = NetworkService()

    def test_get_url_title_returns_correct_title(self):
        url = "https://www.helsinki.fi"

        title = self._network_service.get_url_title(url)

        self.assertEqual(title, "University of Helsinki")

    def test_get_url_title_returns_none_when_page_does_not_exist(self):
        url = "https://not_existing_page.fi"

        title = self._network_service.get_url_title(url)

        self.assertIsNone(title)

    def test_get_url_title_returns_none_when_url_is_invalid(self):
        url = "not_a_url"

        title = self._network_service.get_url_title(url)

        self.assertIsNone(title)
