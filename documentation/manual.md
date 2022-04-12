# Manual

## Installation 

Method 1

- Clone the project to your computer by first navigating to a desired directory and then giving a command: git clone git@github.com:ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti.git

- There should now be a new directory called ’ohtu-2022k-miniprojekti’ – navigate there

- Install dependencies with a command: poetry install (install Poetry first if you haven't done so already: https://python-poetry.org/docs/)

Method 2

- Download the newest release from [Releases](https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti/releases)

- Todo

## How to use the program

- Launch the program with command: poetry run python3 src/index.py

- You can quit the program at any time by pressing control + c

- The program gives you options to choose from: 
  - x lopeta
  - 1 lisää vinkki
  - 2 näytä kaikki vinkit
  - 3 näytä luetut vinkit
  - 4 merkitse vinkki luetuksi
  - 5 hae otsikolla

- Press 1 + enter if you want to add a new bookmark.
  - If you want to return to menu press x + enter.
  - To add bookmark add url + press enter. 
  - If url returns a title and you want to keep it press e + enter or press k + enter if you want to edit it.
  - If url did not return a title or you chose to edit it add your title + press enter.

- Press 2 + enter if you want to see all bookmarks you've saved.

- Press 3 + enter if you want to see bookmarks that have been read already.

- Press 4 + enter if you want to mark a bookmark as read.
  - If you want to return to menu press x + enter.
  - To mark a bookmark as read add its number + press enter.

- Press 5 + enter if you want to search bookmarks by title.
  - To search add your search word + press enter.
 
- Press x + enter if you want to quit running the program.
