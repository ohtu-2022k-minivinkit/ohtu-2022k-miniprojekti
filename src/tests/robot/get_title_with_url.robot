*** Settings ***
Library  ../../RobotLibrary.py  network
Resource  resource.robot
Test Setup  Empty Bookmarks Table And Clear IO
Suite Teardown  Empty Bookmarks Table
Test Timeout  5 second

*** Test Cases ***
Add Valid Bookmark With Working Url
    Input Command  1
    Input Command  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti
    Input Command  e
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  GitHub - ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti

Add Bookmark With Nonexistent Url
    Input Command  1
    Input Command  https://not_existing_page.testi
    Input Command  Title
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Title  https://not_existing_page.testi

Add Valid Bookmark with Working Url And Edit Title
    Input Command  1
    Input Command  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti
    Input Command  k
    Input Command  Minivinkit
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  Minivinkit  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti

Add Two Valid Bookmarks With Working Urls
    Input Command  1
    Input Command  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti
    Input Command  e
    Input Command  1
    Input Command  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti
    Input Command  k
    Input Command  Minivinkit
    Input Command  x
    Run Commands
    Bookmarks Table Should Contain Only One  GitHub - ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti
    Bookmarks Table Should Contain Only One  Minivinkit  https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti

*** Keywords ***
Empty Bookmarks Table And Clear IO
    Empty Bookmarks Table
    Clear Inputs
    Clear Outputs
