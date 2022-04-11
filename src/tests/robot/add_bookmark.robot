*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  1 second

*** Test Cases ***
Add Bookmark With Valid Url And Empty Title
    Input Command  1
    Input Command  http://www.netti.testi
    Input Command  ${EMPTY}
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)
    Bookmarks Table Should Be Empty

Add Bookmark With Empty Url And Valid Name
    Input Command  1
    Input Command  ${EMPTY}
    Input Command  Netti
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  linkki oli virheellinen, anna otsikko ja linkki uudelleen
    Bookmarks Table Should Be Empty

Add One Valid Bookmark
    Input Command  1
    Input Command  http://www.netti.testi
    Input Command  Netti
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Netti  http://www.netti.testi

Add Two Valid Bookmarks With Different Data
    Input Command  1
    Input Command  http://www.netti.testi
    Input Command  Netti
    Input Command  1
    Input Command  http://www.testi.netti
    Input Command  Testi
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Netti  http://www.netti.testi
    Bookmarks Table Should Contain Only One  Testi  http://www.testi.netti

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
