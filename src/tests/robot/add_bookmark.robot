*** Settings ***
Library  ../../RobotLibrary.py
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  1 second

*** Test Cases ***
Add Bookmark With Valid Non Title Returning Url And Empty Title
    Input Command  1
    Input Command  http://www.notreturning.com
    Input Command  ${EMPTY}
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  otsikko puuttui tai oli liian pitkä (yli 100 merkkiä)
    Bookmarks Table Should Be Empty

Add Bookmark With Empty Url And Valid Name
    Input Command  1
    Input Command  ${EMPTY}
    Input Command  Not Returning
    Input Command  x
    Input Command  x
    Run Commands
    Command Line Output Should Contain  linkki oli virheellinen, anna otsikko ja linkki uudelleen
    Bookmarks Table Should Be Empty

Add One Valid Non Title Returning Bookmark
    Input Command  1
    Input Command  http://www.notreturning.com
    Input Command  Not Returning
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Not Returning  http://www.notreturning.com

Add Two Valid Non Title Returning Bookmarks With Different Data
    Input Command  1
    Input Command  http://www.notreturning.com
    Input Command  Not Returning
    Input Command  1
    Input Command  http://www.notreturning2.com
    Input Command  Not Returning2
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Not Returning  http://www.notreturning.com
    Bookmarks Table Should Contain Only One  Not Returning2  http://www.notreturning2.com

Add One Valid Title Returning Bookmark And Do Not Edit Name
    Input Command  1
    Input Command  http://www.returning.com
    Input Command  e
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Returning  http://www.returning.com

Add One Valid Title Returning Bookmark And Edit Name
    Input Command  1
    Input Command  http://www.returning.com
    Input Command  k
    Input Command  Edited
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Edited  http://www.returning.com

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
