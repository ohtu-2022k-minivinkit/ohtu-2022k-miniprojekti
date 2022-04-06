from database_connection import get_database_connection


def drop_tables(connection):
    """Drop all tables in the database"""
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS bookmarks;
    """)

    connection.commit()


def create_tables(connection):
    """Create bookmark table in db"""
    cursor = connection.cursor()

    # Checked column is intended to be used like a boolean. Since SQLite does
    # not have a separate boolean datatype, integer is used instead. Column
    # defaults to FALSE (= 0) and when bookmark has been checked the value
    # is supposed to be TRUE (= 1).
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY,
            headline TEXT,
            url TEXT,
            checked INTEGER DEFAULT FALSE
        );
    """)

    connection.commit()


def initialize_database():
    """Initialize the database"""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
