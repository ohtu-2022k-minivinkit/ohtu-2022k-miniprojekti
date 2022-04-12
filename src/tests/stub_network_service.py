# pylint: skip-file
class StubNetworkService():
    def __init__(self, title_returning_urls=None):
        self._title_returning_urls = title_returning_urls or {}

    def get_url_title(self, url):
        if not self._title_returning_urls.get(url, False):
            return None
        else:
            return self._title_returning_urls.get(url)
