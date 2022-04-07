import requests

def get_url_title(url):
    """Returns the title of the webpage at the given url.

    Args:
        url (string): URL of the webpage.

    Returns:
        string: Title of the webpage.
    """
    html = requests.get(url).text

    title_start = html.find('<title>') + 7
    title_end = html.find('</title>')

    return html[title_start:title_end]
