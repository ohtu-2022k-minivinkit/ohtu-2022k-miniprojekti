# Robot Framework Acceptance Criteria Files
## Sprint 1 User stories
- [User can add a new bookmark, containing a title and a link](../src/tests/robot/add_bookmark.robot)
- [User can see a list of added bookmarks](../src/tests/robot/list_bookmarks.robot)
## Sprint 2 User stories
- [While adding a bookmark the title is fetched automatically from the link url](../src/tests/robot/get_title_with_url.robot)
- [Unread bookmarks are listed, when the application opens. User can also list read boomarks](../src/tests/robot/list_bookmarks.robot#L31)
- [User can search from bookmarks by entering a keyword. If bookmark's title contains keyword, bookmark is displayed to the user](../src/tests/robot/list_bookmarks.robot#L72)
## Sprint 3 User stories
- [Bookmarks are listed in table form, first column is the title and second is the url](../src/tests/robot/list_bookmarks.robot#L16)
- [User can add a book with the book's ISBN code](../src/tests/robot/add_book_with_isbn.robot)
- [User can output bookmarks to a csv-file](../src/tests/robot/create_csv_file.robot)
- [User can load bookmarks from a csv-file](../src/tests/robot/load_csv_file.robot)
