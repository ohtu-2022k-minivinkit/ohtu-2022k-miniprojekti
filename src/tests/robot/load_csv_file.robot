*** Settings ***
Library  OperatingSystem
Library  ../../RobotLibrary.py
Resource  resource.robot
Test Setup  Empty Bookmarks And Remove CSV File And Clear IO
#Timeout to ensure application closure.
#If the ui does not recieve the x-command at the right place tests won´t finnish properly and it can lead to unpredictable behaviour.
Test Timeout  1 second

***Variables***
${FILENAME}  robot-load_file.csv
${DIRPATH}  ${CURDIR}/../../../data/
${FILE_HEADER}  otsikko;linkki\n
${FILEROW1}  Kirja;https://tinyurl.com/aaaaa1\n
${FILEROW2}  Vihko;https://tinyurl.com/bbbbbb2\n

*** Test Cases ***
Atempt To Load Nonexistent Csv File
    Input Command  8
    Input Command  ${DIRPATH}
    Input Command  ${FILENAME}
    Input Command  x
    Run Commands
    Bookmarks Table Should Be Empty
    Command Line Output Should Contain  \ntiedostoa ei löytynyt

Create Empty Csv File And Load It
    Create Test Csv File  ${DIRPATH}${FILENAME}  ${FILE_HEADER}
    Input Command  8
    Input Command  ${DIRPATH}
    Input Command  ${FILENAME}
    Input Command  x
    Run Commands
    Bookmarks Table Should Be Empty

Create Csv File With Two Bookmarks And Load It
    Create Test Csv File  ${DIRPATH}${FILENAME}  ${FILE_HEADER}${FILEROW1}${FILEROW2}
    Input Command  8
    Input Command  ${DIRPATH}
    Input Command  ${FILENAME}
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain  Kirja  https://tinyurl.com/aaaaa1
    Bookmarks Table Should Contain  Vihko  https://tinyurl.com/bbbbbb2
    Bookmarks Table Should Contain X Items  2

*** Keywords ***
Empty Bookmarks And Remove CSV File And Clear IO
    Empty Bookmarks Table
    Remove File  ${DIRPATH}${FILENAME}
    Clear Inputs
    Clear Outputs
