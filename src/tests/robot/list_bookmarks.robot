*** Settings ***
Library  ../../RobotLibrary.py
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

Lists Not Checked Bookmarks Initially
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  True
    Input Command  x
    Run Commands
    Output Should Contain Bookmark  1  Netti  http://www.netti.testi  False
    Output Should Not Contain Bookmark  2  Netti  http://www.netti.testi  True
    Amount Of Bookmarks In Output Should Be  1

No List Of Not Checked Bookmarks
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  True
    Input Command  x
    Run Commands
    Amount Of Bookmarks In Output Should Be  0

Message If Not List Of Not Checked Bookmarks
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  True
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Olet lukenut kaikki vinkit
    Amount Of Bookmarks In Output Should Be  0

Lists Checked Bookmarks Using Separate Command
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  True
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  True
    Input Command  3
    Input Command  3
    Input Command  x
    Run Commands
    Output Should Contain Bookmark  2  Netti  http://www.netti.testi  True
    Amount Of Bookmarks In Output Should Be  5

Message If Not List Of Checked Bookmarks
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Input Command  3
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Kirjastossa ei ole luettuja vinkkejä
    Amount Of Bookmarks In Output Should Be  1

Show Correct Bookmarks When Proper Keyword Is Given To Search Function
    Create Bookmark Into Database  netti  http://www.netti.testi
    Create Bookmark Into Database  Vinkki  http://www.vinkki.testi
    Create Bookmark Into Database  NETti  http://www.netti.testi
    Input Command  5
    Input Command  net
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Vinkit, jotka sisälsivät hakusanan 'net':
    Output Should Contain Bookmark  1  netti  http://www.netti.testi  False
    Output Should Contain Bookmark  3  NETti  http://www.netti.testi  False
    Amount Of Bookmarks In Output Should Be  5

Show No Bookmarks And Display Correct Error Message When Keyword Doesnt Match Any Bookmarks
    Create Bookmark Into Database  netti  http://www.netti.testi
    Create Bookmark Into Database  Vinkki  http://www.vinkki.testi
    Create Bookmark Into Database  NETti  http://www.netti.testi
    Input Command  5
    Input Command  abc
    Input Command  x
    Run Commands
    Command Line Output Should Contain  Hakusanalla 'abc' ei löytynyt yhtään vinkkiä
    Amount Of Bookmarks In Output Should Be  3

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
