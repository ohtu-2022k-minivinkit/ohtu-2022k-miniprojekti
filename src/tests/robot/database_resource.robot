*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem
Library  Expand.py

*** Variables ***
${database_name}  test-database.sqlite

*** Keywords ***
Connect To Test Database
    Connect To Database Using Custom Params  sqlite3  database="./data/${database_name}", isolation_level=None

Empty Bookmarks Table
    Connect To Test Database
    Execute SQL String  DELETE FROM bookmarks;
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
    [Arguments]  ${headline}
    Connect To Test Database
    Row Count Is Equal To X  SELECT * FROM bookmarks WHERE headline = "${headline}";  1
    Disconnect From Database

Url Connected To Headline Should Contain Tiny
    [Arguments]  ${headline}
    Connect To Test Database
    @{queryResults}  Query  SELECT url FROM bookmarks WHERE headline = "${headline}"
    Should Contain    @{queryResults[0]}    tiny
    Disconnect From Database

Expanded Tinyurl Should Match Original Url
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    @{queryResults}  Query  SELECT url FROM bookmarks WHERE headline = "${headline}"
    ${Expand}=    Expand url    @{queryResults[0]}
    Should Be Equal    ${Expand}    ${url}
    Disconnect From Database

Create Bookmark Into Database
    [Arguments]  ${headline}  ${url}
    Connect To Test Database
    Execute Sql String  INSERT INTO bookmarks (headline, url) VALUES ("${headline}", "${url}");
    Disconnect From Database

Create Bookmark Into Database With Status
    [Arguments]  ${headline}  ${url}  ${status}
    Connect To Test Database
    Execute Sql String  INSERT INTO bookmarks (headline, url, checked) VALUES ("${headline}", "${url}", ${status});
    Disconnect From Database
