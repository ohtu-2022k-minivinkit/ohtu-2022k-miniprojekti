*** Settings ***
Resource  database_resource.robot

*** Keywords ***
Run Commands
    Ui Start

Clear Outputs
    Command Line Clear Output

Clear Inputs
    Command Line Clear Input

Clear Output Record
    Command Line Clear Output With Stubio Input

Output Should Contain Bookmark
    [Arguments]  ${index}  ${headline}  ${url}  ${checked}
    Command Line Output Should Contain  ${index} ${headline} ${url} ${checked}

Output Should Not Contain Bookmark
    [Arguments]  ${index}  ${headline}  ${url}  ${checked}
    Command Line Output Should Not Contain  ${index} ${headline} ${url} ${checked}

File Should Contain Headline And Url
    [Arguments]  ${DIRPATH}  ${FILENAME}  ${headline}  ${url}
    File Should Contain  ${DIRPATH}${FILENAME}  ${headline};${url}

File Should Not Contain Headline And Url
    [Arguments]  ${DIRPATH}  ${FILENAME}  ${headline}  ${url}
    File Should Not Contain  ${DIRPATH}${FILENAME}  ${headline};${url}

Input Command 
    [Arguments]  ${text}
    Command Line Input  ${text}

Amount Of Bookmarks In Output Should Be
    [Arguments]  ${amount}
    Command Line Output Count Of Bookmarks  ${amount}
