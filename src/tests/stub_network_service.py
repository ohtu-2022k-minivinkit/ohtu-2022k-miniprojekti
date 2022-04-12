# pylint: skip-file
class StubNetworkService():
    def __init__(self, returning_urls=None):
        self._returning_urls = returning_urls or {}

    def get_url_title(self, url):
        if not self._returning_urls.get(url, False):
            return None
        else:
            return self._returning_urls.get(url)
