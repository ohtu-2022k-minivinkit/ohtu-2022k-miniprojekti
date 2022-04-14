*** Settings ***
Library  ../../RobotLibrary.py
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO

*** Test Cases ***
Main Menu Contains Command To Mark The Bookmark As Read
    Input Command  x
    Run Commands
    Command Line Output Should Contain  4 merkitse vinkki luetuksi

Setting Bookmark As Checked Using Correct Index Number Sets Bookmark As Checked
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  True
    Input Command  4
    Clear Output Record
    Input Command  1
    Input command  3
    Input Command  x
    Run Commands
    Amount Of Bookmarks In Output Should Be  2
    Output Should Contain Bookmark  1  Netti  http://www.netti.testi  luettu

Gives Error If Invalid Index Number Is Used
    Create Bookmark Into Database With Status  Netti  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki  http://www.vinkki.testi  False
    Input Command  4
    Clear Output Record
    Input Command  3
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  \nVIRHE: Vinkkiä 3 ei ole!\n

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
