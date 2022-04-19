*** Settings ***
Library  OperatingSystem
Library  ../../RobotLibrary.py
Resource  resource.robot
Test Setup  Empty Bookmarks Table Create Csv File And Clear IO

***Variables***
${FILENAME}     robot-test_file.csv
${DIRPATH}      ${CURDIR}/../../../data/

*** Test Cases ***
Not existing Csv File Is Created Containing All Headlines And Links From Bookmark Repository
    Create Bookmark Into Database With Status  Netti11  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki12  http://www.vinkki.testi  True
    Create Bookmark Into Database With Status  Netti13  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki14  http://www.vinkki.testi  True
    Remove File  ${DIRPATH}${FILENAME}
    Input Command  6
    Input Command  ${FILENAME}
    Input Command  ${DIRPATH}
    Input Command  x
    Run Commands
    File Should Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Netti11  http://www.netti.testi
    File Should Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Vinkki14  http://www.vinkki.testi

Existing Csv File Is Not Overwrited
    Create Bookmark Into Database With Status  Netti11  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki12  http://www.vinkki.testi  True
    Create Bookmark Into Database With Status  Netti13  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki14  http://www.vinkki.testi  True
    Touch  ${DIRPATH}${FILENAME}
    Input Command  6
    Input Command  ${FILENAME}
    Input Command  ${DIRPATH}
    Input Command  e
    Input Command  x
    Input Command  x
    Run Commands
    File Should Not Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Netti11  http://www.netti.testi
    File Should Not Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Vinkki14  http://www.vinkki.testi

Existing Csv File Is Overwrited if asked
    Create Bookmark Into Database With Status  Netti11  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki12  http://www.vinkki.testi  True
    Create Bookmark Into Database With Status  Netti13  http://www.netti.testi  False
    Create Bookmark Into Database With Status  Vinkki14  http://www.vinkki.testi  True
    Touch  ${DIRPATH}${FILENAME}
    Input Command  6
    Input Command  ${FILENAME}
    Input Command  ${DIRPATH}
    Input Command  k
    Input Command  x
    Run Commands
    File Should Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Netti11  http://www.netti.testi
    File Should Contain Headline And Url  ${DIRPATH}  ${FILENAME}  Vinkki14  http://www.vinkki.testi


*** Keywords ***
Empty Bookmarks Table Create Csv File And Clear IO
    Empty Bookmarks Table
    Remove File  ${DIRPATH}${FILENAME}
    #Touch  ${DIRPATH}${FILENAME}
    Clear Inputs
    Clear Outputs
