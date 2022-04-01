from ui.ui import UI
from services.bookmark_service import bookmark_service

def main():
    # pylint: disable=invalid-name
    ui = UI(bookmark_service)
    ui.start()

if __name__ == '__main__':
    main()
