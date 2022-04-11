*** Settings ***
Resource  database_resource.robot
Library  ../../RobotLibrary.py

*** Variables ***
${standard_output}  ['', 'Lukemattomat vinkit:', '', 'Bookmarks komennot:', 'x lopeta', '1 lisää vinkki', '2 näytä kaikki vinkit', '3 näytä luetut vinkit', ''
${standard_output_ending}  ]
${empty_output_line}  , ''

*** Keywords ***
Go To Bookmark Input
    Input Command  1

List Bookmarks
    Input Command  2
    Input Command  x
    Run Commands

Add Bookmark
    [Arguments]  ${headline}  ${url}
    Clear Inputs
    Clear Outputs
    Go To Bookmark Input
    Input Command  ${url}
    Input Command  ${headline}
    Input Command  x
    Run Commands

Run Commands
    Ui Start

Clear Outputs
    Command Line Clear Output

Clear Inputs
    Command Line Clear Input

Output Should Contain Bookmark
    [Arguments]  ${index}  ${headline}  ${url}  ${checked}
    Command Line Output Should Contain  ${index}: ${headline}, ${url}

Output Should Not Contain Bookmark
    [Arguments]  ${index}  ${headline}  ${url}  ${checked}
    Command Line Output Should Not Contain  ${index}: ${headline}, ${url}

Output Should Be Standard Output
    Command Line Output Should Be  ${standard_output}${standard_output_ending}

Output Should Be Standard Output And Empty Output Line
    Command Line Output Should Be  ${standard_output}${empty_output_line}${standard_output_ending}

Input Command 
    [Arguments]  ${text}
    Command Line Input  ${text}

Amount Of Bookmarks In Output Should Be
    [Arguments]  ${amount}
    Command Line Output Count Of Bookmarks  ${amount}
