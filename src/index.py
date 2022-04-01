from ui.ui import UI
from services.bookmark_service import bookmark_service

def main():
    # pylint: disable=invalid-name, kiitos, nyt lienee parempi
    user_interface = UI(bookmark_service)
    user_interface.start()

if __name__ == '__main__':
    main()
