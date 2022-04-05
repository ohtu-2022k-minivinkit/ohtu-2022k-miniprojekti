*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table

*** Test Cases ***
List Bookmarks With No Bookmarks
    List Bookmarks
    Output Should Not Contain Bookmark  Netti  http://www.netti.fi
    Output Should Not Contain Bookmark  Vinkki  http://www.vinkki.fi
    Output Should Be Standard Output And Empty Output Line

Create One Bookmark Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    List Bookmarks
    Output Should Contain Bookmark  Netti  http://www.netti.fi
    Output Should Not Contain Bookmark  Vinkki  http://www.vinkki.fi

Create Two Bookmarks Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    Create Bookmark In Bookmarks Table  Vinkki  http://www.vinkki.fi
    List Bookmarks
    Output Should Contain Bookmark  Netti  http://www.netti.fi
    Output Should Contain Bookmark  Vinkki  http://www.vinkki.fi

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
