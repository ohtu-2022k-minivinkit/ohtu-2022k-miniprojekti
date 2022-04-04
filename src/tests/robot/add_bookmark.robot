*** Settings ***
Resource  resource.robot
Test Setup  Run Application And Empty Bookmarks Table And Go To Bookmark Input
Suite Teardown  Empty Bookmarks Table And Bookmarks Table Should Be Empty

*** Test Cases ***
Add Bookmark With Empty Title And Valid Url
    Add Bookmark  ${EMPTY}  http://www.netti.fi
    Run Application
    Bookmarks Table Should Be Empty

Add Bookmark With Valid Name And Empty Url
    Add Bookmark  Netti  ${EMPTY}
    Run Application
    Bookmarks Table Should Be Empty

Add One Valid Bookmark
    Add Bookmark  Netti  http://www.netti.fi
    Run Application
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Bookmarks Table Should Contain X Items  1

Add Two Valid Bookmarks With Different Data
    Add Bookmark  Netti  http://www.netti.fi
    Go To Bookmark Input
    Add Bookmark  Vinkki  http://www.vinkki.fi
    Run Application
    Bookmarks Table Should Contain  Vinkki  http://www.vinkki.fi
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Bookmarks Table Should Contain X Items  2

Add Valid Bookmark And Close Application And Start Application
    Add Bookmark  Netti  http://www.netti.fi
    Run Application
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Run Application
    Bookmarks Table Should Contain  Netti  http://www.netti.fi
    Bookmarks Table Should Contain X Items  1

*** Keywords ***
Run Application And Empty Bookmarks Table And Go To Bookmark Input
    Run Application
    Empty Bookmarks Table
    Bookmarks Table Should Be Empty
    Go To Bookmark Input

Empty Bookmarks Table And Bookmarks Table Should Be Empty
    Empty Bookmarks Table
    Bookmarks Table Should Be Empty

