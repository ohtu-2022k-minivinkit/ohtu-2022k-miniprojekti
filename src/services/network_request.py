import requests

def get_url_title(url):
    """Returns the title of the webpage at the given url.

    Args:
        url (string): URL of the webpage.

    Returns:
        string: Title of the webpage.
    """
    try:
        html = requests.get(url).text
    except requests.exceptions.RequestException:
        return ""

    title_start = html.find('<title>') + 7
    title_end = html.find('</title>')

    if title_start == -1 or title_end == -1:
        return ""

    return html[title_start:title_end]
