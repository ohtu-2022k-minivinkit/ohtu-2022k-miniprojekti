# pylint: skip-file
import pyshorteners

class Expand:
  def expand_url(self, url):
    url_shortener = pyshorteners.Shortener()
    expanded = url_shortener.tinyurl.expand(url)
    return expanded
