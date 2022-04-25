# Manual

## Installation 

Method 1

- Clone the project to your computer by first navigating to a desired directory and then giving a command: `git clone git@github.com:ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti.git`

- There should now be a new directory called ’ohtu-2022k-miniprojekti’ – navigate there

- Install dependencies with a command: `poetry install --no-dev` (install Poetry first if you haven't done so already: https://python-poetry.org/docs/)

Method 2

- Download the newest release from [releases](https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti/releases).
  - Source files are under assets.

- Unzip the file to a location of your choosing and navigate to the folder.

- Install dependencies with a command: poetry install (install Poetry first if you haven't done so already: https://python-poetry.org/docs/)

## How to use the program

- Launch the program with command: `poetry run python3 src/index.py`

- You can quit the program at any time by pressing control + c

- The program gives you options to choose from: 
  - x lopeta
  - 1 lisää vinkki
  - 2 lisää kirja ISBN-tunnuksella
  - 3 näytä kaikki vinkit
  - 4 näytä luetut vinkit
  - 5 merkitse vinkki luetuksi
  - 7 hae otsikolla
  - 7 muodosta csv -tiedosto
  - 8 lataa csv -tiedosto


- Press 1 + enter if you want to add a new bookmark.
  - If you want to return to menu press x + enter.
  - To add bookmark add url + enter. 
  - If url returns a title and you want to keep it press e + enter or press k + enter if you want to edit it.
  - If url did not return a title or you chose to edit it add your title + enter.

- Press 2 + enter if you want to add a new book using the book's ISBN code
  - To add book input the ISBN + enter
  - If the book is found and you want to keep it press e + enter or press k + enter if you want to edit it.
  - If the ISBN is not found the program tells you that the book wasn't found and exits the book addition

- Press 3 + enter if you want to see all bookmarks you've saved.

- Press 4 + enter if you want to see bookmarks that have been read already.

- Press 5 + enter if you want to mark a bookmark as read.
  - If you want to return to menu press x + enter.
  - To mark a bookmark as read add its number + press enter.

- Press 6 + enter if you want to search bookmarks by title.
  - To search add your search word + press enter.

- Press 7 to form a csv file with your bookmarks.
  - Give the csv file a name or use the default name by pressing enter.
  - Give the absolute path for saving the csv file or use the default path by pressing enter.
  - The csv file will be located in csv_files folder at given location.

- Press 8 to load a csv file with bookmarks into the program.
  - Give the path to the csv file or use the default path of current folder by pressing enter.
  - Input the name of the csv file and press enter.
  - The data from the csv file will be loaded into the program.
 
- Press x + enter if you want to quit running the program.
