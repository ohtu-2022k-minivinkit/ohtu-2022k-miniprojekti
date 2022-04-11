*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem

*** Variables ***
${database_name}  test-database.sqlite

*** Keywords ***
Connect To Test Database
    Connect To Database Using Custom Params  sqlite3  database="./data/${database_name}", isolation_level=None

Empty Bookmarks Table
    Connect To Test Database
    Execute SQL String  DELETE FROM bookmarks;
    Disconnect From Database

Create Bookmarks Table If Missing
    Connect To Test Database
    Execute SQL String  CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY, headline TEXT, url TEXT, checked INTEGER DEFAULT FALSE);
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

Create Bookmark Into Database
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Execute Sql String  INSERT INTO bookmarks (headline, url) VALUES ("${headline}", "${url}");
    Disconnect From Database