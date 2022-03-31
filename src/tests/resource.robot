*** Settings ***
Library  ../BookmarksLibrary.py

*** Keywords ***
Start Application
    Ui Start
    Output Should Contain  Bookmarks komennot:

Close Application
    Ui Close

Empty Database
    Database Empty
    Database Should Be Empty

Output Should Contain
    [Arguments]  ${text}
    Command Line Output Should Contain  ${text}

Input Command
    [Arguments]  ${text}
    Output Should Contain  komento:
    Command Line Input  ${text}








