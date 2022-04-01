from ui.ui import UI

#tämä koko viritelmä UI suoritusta varten :D saa poistaa
class BookmarkService():
    def __init__(self):
        self.service = []

def main():
    # pylint: disable=invalid-name
    ui = UI(BookmarkService())
    ui.start()

if __name__ == '__main__':
    main()
