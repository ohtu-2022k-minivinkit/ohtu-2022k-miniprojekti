import requests
import pyshorteners

# pylint: disable=no-self-use
class NetworkService():
    def __init__(self):
        """Creates new NetworkService object.
        """

    def get_url_title(self, url):
        """Returns the title of the webpage at the given url.
            If the url is invalid or no title is found, returns None.

        Args:
            url (string): URL of the webpage.

        Returns:
            string: Title of the webpage.
        """
        try:
            html = requests.get(url).text
        except requests.exceptions.RequestException:
            return None

        title_start = html.find('<title>') + 7
        title_end = html.find('</title>')

        if title_start == -1 or title_end == -1:
            return None

        return html[title_start:title_end]

    def shorten_url(self, url):
        """Returns the shortened url of the given url.
        If shortening is unsuccessful, returns None.

        Args:
            url (string): URL of the webpage.

        Returns:
            string: Shortened url of the webpage.
        """
        try:
            shortened_url = pyshorteners.Shortener().tinyurl.short(url)
        except requests.exceptions.RequestException:
            return None

        return shortened_url

    def get_book_by_isbn(self, isbn):
        """Returns the book with the given isbn.
            If the isbn is invalid or no book is found, returns None.
           Uses the Open Library API.

        Args:
            isbn (string): ISBN of the book.

        Returns:
            dictionary: Book with the given isbn.
        """
        url = f"https://openlibrary.org/isbn/{isbn}.json"

        try:
            book = requests.get(url).json()
        except requests.exceptions.RequestException:
            return None

        if "error" in book:
            return None

        book["link"] = url[:-5]

        return book

network_service = NetworkService()
