*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table
Suite Teardown  Empty Bookmarks Table

*** Test Cases ***
Add Bookmark With Empty Title And Valid Url
    Add Bookmark  ${EMPTY}  http://www.netti.fi
    Bookmarks Table Should Be Empty

Add Bookmark With Valid Name And Empty Url
    Add Bookmark  Netti  ${EMPTY}
    Bookmarks Table Should Be Empty

Add One Valid Bookmark
    Add Bookmark  Netti  http://www.netti.fi
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Bookmarks Table Should Contain X Items  1

Add Two Valid Bookmarks With Different Data
    Add Bookmark  Netti  http://www.netti.fi
    Add Bookmark  Vinkki  http://www.vinkki.fi
    Bookmarks Table Should Contain  Vinkki  http://www.vinkki.fi
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Bookmarks Table Should Contain X Items  2
