*** Settings ***
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  1 second

*** Test Cases ***
Add Valid Bookmark With Working Url
    Input Command  1
    Input Command  https://helsinki.fi
    Input Command  e
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  University of Helsinki  https://helsinki.fi

Add Bookmark With Nonexistent Url
    Input Command  1
    Input Command  https://not_existing_page.fi
    Input Command  Title
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Title  https://not_existing_page.fi

Add Valid Bookmark with Working Url And Edit Title
    Input Command  1
    Input Command  https://helsinki.fi
    Input Command  k
    Input Command  Helsingin yliopisto
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Helsingin yliopisto  https://helsinki.fi

Add Two Valid Bookmarks With Working Urls
    Input Command  1
    Input Command  https://helsinki.fi
    Input Command  e
    Input Command  1
    Input Command  https://helsinki.fi
    Input Command  k
    Input Command  Helsingin yliopisto
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  University of Helsinki  https://helsinki.fi
    Bookmarks Table Should Contain Only One  Helsingin yliopisto  https://helsinki.fi

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
