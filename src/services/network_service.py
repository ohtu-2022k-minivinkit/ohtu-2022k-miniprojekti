import requests

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


network_service = NetworkService()
