import pyshorteners as sh

class Expand:
  def expand_url(self, url):
    s = sh.Shortener()
    expanded = s.tinyurl.expand(url)
    return expanded
