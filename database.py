import mysql.connector

from config import ConfigManager


class DatabaseConnector:
    """Manage MySQL database connections."""

    def __init__(self):
        config = ConfigManager.create_default()

        self.host = config.get("PROJECT_1")
        self.user = config.get("root")
        self.password = config.get("Cyntheiya123#")
        self.database = config.get("sprint1_db")

        self.connection = None

    def connect(self):
        """Connect to MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            print("Database connected successfully.")
            return self.connection

        except mysql.connector.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close(self) -> None:
        """Close database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query: str, values=None):
        """Execute SQL query."""
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()

            cursor = self.connection.cursor()

            cursor.execute(query, values)

            self.connection.commit()

            return cursor

        except mysql.connector.Error as e:
            if self.connection:
                self.connection.rollback()

            print(f"SQL execution error: {e}")
            raise