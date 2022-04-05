from database_connection import get_database_connection

def drop_tables(connection):
    """Drop all tables in the database"""
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS bookmarks;
    ''')

    connection.commit()


def create_tables(connection):
    """Create bookmark table in db"""
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE bookmarks (
            id INTEGER PRIMARY KEY,
            headline TEXT,
            url text
        );
    ''')

    connection.commit()


def initialize_database():
    """Initialize the database"""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
