from ui.ui import UI

#tämä koko viritelmä UI suoritusta varten :D saa poistaa
class Bookmark_service():
    def __init__(self):
        self.service = []
    

def main():
    ui = UI(Bookmark_service())
    ui.start()

if __name__ == '__main__':
    main()
