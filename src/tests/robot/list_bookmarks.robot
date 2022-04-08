*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table

*** Test Cases ***
List Bookmarks With No Bookmarks
    List Bookmarks
    Command Line Output Should Contain  Kirjastossa ei ole vinkkejä

Create One Bookmark Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    List Bookmarks
    Output Should Contain Bookmark  1  Netti  http://www.netti.fi  False

Create Two Bookmarks Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    Create Bookmark In Bookmarks Table  Vinkki  http://www.vinkki.fi
    List Bookmarks
    Output Should Contain Bookmark  1  Netti  http://www.netti.fi  False
    Output Should Contain Bookmark  2  Vinkki  http://www.vinkki.fi  False

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
