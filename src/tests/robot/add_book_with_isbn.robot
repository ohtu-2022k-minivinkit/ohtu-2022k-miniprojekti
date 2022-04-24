*** Settings ***
Library  ../../RobotLibrary.py  network
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
#Timeout to ensure application closure.
#If the ui does not recieve the x-command at the right place tests won´t finnish properly and it can lead to unpredictable behaviour.
Test Timeout  10 second

*** Test Cases ***
Add Book With Working ISBN
    Input Command  2
    Input Command  9780262011532
    Input Command  e
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Structure and Interpretation of Computer Programs
    Url Connected To Headline Should Contain Tiny  Structure and Interpretation of Computer Programs

Add Book With Incorrect ISBN
    Input Command  2
    Input Command  12345
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Kirjaa ei löytynyt.

Add Book With Working ISBN And Edit Title
    Input Command  2
    Input Command  9780262011532
    Input Command  k
    Input Command  Muokattu
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Muokattu
    Url Connected To Headline Should Contain Tiny  Muokattu

Add Two Books With Valid ISBNs
    Input Command  2
    Input Command  9780262011532
    Input Command  e
    Input Command  2
    Input Command  9780262011532
    Input Command  k
    Input Command  Muokattu
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Structure and Interpretation of Computer Programs
    Bookmarks Table Should Contain Only One  Muokattu
    Url Connected To Headline Should Contain Tiny  Structure and Interpretation of Computer Programs
    Url Connected To Headline Should Contain Tiny  Muokattu

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
