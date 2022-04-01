from ui.ui import UI
from services.bookmark_service import bookmark_service

def main():
    user_interface = UI(bookmark_service)
    user_interface.start()

if __name__ == '__main__':
    main()
