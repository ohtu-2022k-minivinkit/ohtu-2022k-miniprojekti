*** Settings ***
Library  ../../RobotLibrary.py
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  1 second

*** Test Cases ***
Main Menu Contains Command To Mark The Bookmark As Read
    Input Command  x
    Run Commands
    Command Line Output Should Contain  4 merkitse vinkki luetuksi

Checking Bookmark Using Serial Number Moves Bookmark To Checked Bookmarks
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  True
    Input Command  4
    Clear Output With Stubio Input
    Input Command  2
    Input command  3
    Input Command  x
    Run Commands
    Amount Of Bookmarks In Output Should Be  2
    Output Should Contain Bookmark  1  Netti  http://www.netti.testi  True

Error Message And List Of Unchecked Bookmarks If InValid Serial Number Is Given
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  True
    Input Command  4
    Clear Output With Stubio Input
    Input Command  55
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  \nVIRHE: Vinkkiä 55 ei ole!\n
    Amount Of Bookmarks In Output Should Be  2

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
