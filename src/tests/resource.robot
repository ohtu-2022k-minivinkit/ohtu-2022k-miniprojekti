*** Settings ***
Library  ../BookmarksLibrary.py
Library  DatabaseLibrary
Library  OperatingSystem

*** Variables ***
${database_name}  database.sqlite
${standard_output}  ['', 'Bookmarks komennot:', 'x lopeta', '1 lisää vinkki', '2 tulosta vinkit', ''
${standard_output_ending}  ]
${empty_output_line}  , ''

*** Keywords ***
Connect To Test Database
    Connect To Database Using Custom Params  sqlite3  database="./data/${database_name}", isolation_level=None

Empty Bookmarks Table
    Connect To Test Database
    Execute SQL String  DELETE FROM bookmarks;
    Disconnect From Database

Create Bookmarks Table If Missing
    Connect To Test Database
    Execute SQL String  CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY, headline TEXT, url TEXT);
    Disconnect From Database

Bookmarks Table Should Be Empty
    Connect To Test Database
    Row Count Is 0  SELECT * FROM bookmarks;
    Disconnect From Database

Bookmarks Table Should Contain X Items
    [Arguments]  ${rows}
    Connect To Test Database
    Row Count Is Equal To X  SELECT * FROM bookmarks;  ${rows}
    Disconnect From Database

Bookmarks Table Should Contain
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Row Count Is Greater Than X  SELECT * FROM bookmarks WHERE headline = "${headline}" AND url = "${url}";  0
    Disconnect From Database

Bookmarks Table Should Not Contain
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Row Count Is Equal To X  SELECT * FROM bookmarks WHERE headline = "${headline}" AND url = "${url}";  0
    Disconnect From Database

Bookmarks Table Should Contain Only One
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Row Count Is Equal To X  SELECT * FROM bookmarks WHERE headline = "${headline}" AND url = "${url}";  1
    Disconnect From Database

Create Bookmark In Bookmarks Table
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Execute Sql String  INSERT INTO bookmarks (headline, url) VALUES ("${headline}", "${url}");
    Disconnect From Database

Go To Bookmark Input
    Input Command  1

List Bookmarks
    Input Command  2

Add Bookmark
    [Arguments]  ${headline}  ${url}
    Input Command  ${headline}
    Input Command  ${url}

Run Application
    Add Close Application Command
    Ui Start

Add Close Application Command
    Input Command  x

Clear Outputs
    Command Line Clear Output

Clear Inputs
    Command Line Clear Input

Output Should Contain Bookmark
    [Arguments]  ${headline}  ${url}
    Command Line Output Should Contain  ${headline} ${url}

Output Should Not Contain Bookmark
    [Arguments]  ${headline}  ${url}
    Command Line Output Should Not Contain  ${headline} ${url}

Output Should Be Standard Output
    Command Line Output Should Be  ${standard_output}${standard_output_ending}

Output Should Be Standard Output And Empty Output Line
    Command Line Output Should Be  ${standard_output}${empty_output_line}${standard_output_ending}

Input Command
    [Arguments]  ${text}
    Command Line Input  ${text}








