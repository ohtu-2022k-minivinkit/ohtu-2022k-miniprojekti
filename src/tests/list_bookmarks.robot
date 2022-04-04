*** Settings ***
Resource  resource.robot
Test Setup  Run Application And Empty Bookmarks Table And Clear Inputs And Clear Outputs

*** Test Cases ***
Create One Bookmark Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    List Bookmarks
    Run Application
    Output Should Contain Bookmark  Netti  http://www.netti.fi
    Output Should Not Contain Bookmark  Vinkki  http://www.vinkki.fi

Create Two Bookmarks Into Database And List Bookmarks
    Create Bookmark In Bookmarks Table  Netti  http://www.netti.fi
    Create Bookmark In Bookmarks Table  Vinkki  http://www.vinkki.fi
    List Bookmarks
    Run Application
    Output Should Contain Bookmark  Netti  http://www.netti.fi
    Output Should Contain Bookmark  Vinkki  http://www.vinkki.fi

List Bookmarks
    List Bookmarks
    Run Application
    Output Should Not Contain Bookmark  Netti  http://www.netti.fi
    Output Should Not Contain Bookmark  Vinkki  http://www.vinkki.fi
    Output Should Be Standard Output

*** Keywords ***
Run Application And Empty Bookmarks Table And Clear Inputs And Clear Outputs
    Run Application
    Empty Bookmarks Table
    Bookmarks Table Should Be Empty
    Clear Inputs
    Clear Outputs
    
