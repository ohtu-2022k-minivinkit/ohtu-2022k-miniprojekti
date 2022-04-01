class Bookmark:
    def __init__(self, headline, url):
        self.headline = headline
        self.url = url

    def __str__(self):
        return f"{self.headline} {self.url}"
