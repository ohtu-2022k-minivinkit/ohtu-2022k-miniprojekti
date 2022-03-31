*** Settings ***
Resource  resource.robot
Test Setup  Empty Database And Start Application And Go To Bookmark Input

*** Test Cases ***
Add Bookmark With Empty Name And Valid Url
    Add Bookmark  ${EMPTY}  www.netti.fi
    Bookmarks Should Be Empty

Add Bookmark With Valid Name And Empty Url
    Add Bookmark  Netti  ${EMPTY}
    Bookmarks Should Be Empty

Add Bookmark With Valid Name And Valid Url
    Add Bookmark  Netti  www.netti.fi
    Bookmarks Should Contain  Netti  www.netti.fi

Add Two Valid Bookmarks With Same Data
    Add Bookmark  Netti  www.netti.fi
    Bookmarks Should Contain  Netti  www.netti.fi
    Go To Bookmark Input
    Add Bookmark  Netti  www.netti.fi
    Bookmarks Should Contain Only One  Netti  www.netti.fi

Add Two Valid Bookmarks With Different Data
    Add Bookmark  Netti  www.netti.fi
    Bookmarks Should Contain  Netti  www.netti.fi
    Go To Bookmark Input
    Add Bookmark  Vinkki  www.vinkki.fi
    Bookmarks Should Contain  Vinkki  www.vinkki.fi
    Bookmarks Should Contain  Netti  www.netti.fi

Add Valid Bookmark And Close Application And Start Application
    Add Bookmark  Netti  www.netti.fi
    Bookmarks Should Contain  Netti  www.netti.fi
    Close Application
    Start Application
    Bookmarks Should Contain  Netti  www.netti.fi

*** Keywords ***
Empty Database And Start Application And Go To Bookmark Input
    Empty Database
    Start Application
    Go To Bookmark Input

Go To Bookmark Input
    Should Be In Input Mode
    Input Command  1
    Should Be In Bookmark Input

Should Be In Bookmark Input
    Output Should Contain  Lisätään uusi vinkki
    Should Be In Input Mode

Should Be In Input Mode
    Output Should Contain  komento:

Add Bookmark
    [Arguments]  ${headline}  ${url}
    Should Be In Bookmark Input
    Input Command  ${headline}
    Input Command  ${url}

Bookmarks Should Contain
    [Arguments]  ${headline}  ${url}
    Bookmarks Table Should Contain  ${headline}  ${url}

Bookmarks Should Contain Only One
    [Arguments]  ${headline}  ${url}
    Bookmarks Table Should Contain Only One  ${headline}  ${url}
    
Bookmarks Should Be Empty
    Bookmarks Table Should Be Empty

