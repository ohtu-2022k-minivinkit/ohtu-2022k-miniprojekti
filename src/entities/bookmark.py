class Bookmark:
    def __init__(self, headline, url, checked=False):
        """Initializes Bookmark with headline, url and checked.

        Args:
            headline (string):
                Headline of the bookmark.
            url (string):
                URL to bookmarked material.
            checked (bool, optional):
                True if bookmark has been read. Defaults to False.
        """
        self.headline = headline
        self.url = url
        self.checked = checked

    def __str__(self):
        """Returns string representation of the object.

        Returns:
            string: String representation of the object.
        """
        return f"{self.headline}: {self.url}, {'True' if self.checked else 'False'}"
