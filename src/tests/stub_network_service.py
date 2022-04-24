# pylint: skip-file
class StubNetworkService():
    def __init__(self, title_returning_urls=None, book_returning_isbns=None):
        self._title_returning_urls = title_returning_urls or {}
        self.book_returning_isbns = book_returning_isbns or {}

    def get_url_title(self, url):
        if not self._title_returning_urls.get(url, False):
            return None
        else:
            return self._title_returning_urls.get(url)

    def shorten_url(self, url):
        return "https://tinyurl.com/" + str(hash(url))

    def get_book_by_isbn(self, isbn):
        if not self.book_returning_isbns.get(isbn, False):
            return None
        else:
            return self.book_returning_isbns.get(isbn)
