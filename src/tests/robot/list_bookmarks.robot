*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  1 second

*** Test Cases ***
List Bookmarks With No Bookmarks
    Input Command  2
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Kirjastossa ei ole vinkkejä

Create One Bookmark Into Database And List Bookmarks
    Create Bookmark Into Database  Netti  http://www.netti.testi
    Input Command  2
    Input Command  x
    Run Commands
    Output Should Contain Bookmark  1  Netti  http://www.netti.testi  False

Create Two Bookmarks Into Database And List Bookmarks
    Create Bookmark Into Database  Netti  http://www.netti.testi
    Create Bookmark Into Database  Vinkki  http://www.vinkki.testi
    Input Command  2
    Input Command  x
    Run Commands
    Output Should Contain Bookmark  1  Netti  http://www.netti.testi  False
    Output Should Contain Bookmark  2  Vinkki  http://www.vinkki.testi  False

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
