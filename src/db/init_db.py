from pathlib import Path
import sqlite3


class DatabaseInitializer:
    """
    Creates the SQLite database using schema.sql
    """

    def __init__(
        self,
        db_path="db/nifty100.db",
        schema_path="db/schema.sql"
    ):
        self.db_path = Path(db_path)
        self.schema_path = Path(schema_path)

    def initialize_database(self):
        """
        Create database and tables.
        """

        connection = sqlite3.connect(self.db_path)

        with open(self.schema_path, "r") as file:
            schema = file.read()

        connection.executescript(schema)

        connection.commit()
        connection.close()

        print("Database initialized successfully!")