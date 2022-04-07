from ui.console_io import (
console_io as default_console_io
)
from ui.feed_validation import (
feed_validation as default_feed_validation
)
from services.bookmark_service import (
bookmark_service as default_bookmark_service
)

class UserCommand:
    """superclass use with new command for user"""

    def __init__(self,
        console_io = default_console_io,
        feed_validation = default_feed_validation,
        bookmark_service = default_bookmark_service
        ):
        self._io = console_io
        self._feed_validation = feed_validation
        self._bookmark_service = bookmark_service

    def _print_info():
        pass
    
    def _execute(self):
        pass
