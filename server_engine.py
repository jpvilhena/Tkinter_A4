import os
import pymysql
from typing import Any, List, Dict, Optional


class Database:
    def __init__(self) -> None:
        """
        Initializes a connection to the MySQL database using environment variables.
        """
        self.connection = pymysql.connect(
            host=os.environ['HOST'],
            port=int(os.environ['PORT']),
            user=os.environ['USER'],
            password=os.environ['PASSWORD'],
            database="defaultdb",
            ssl={"ca": "ca.pem"},
            cursorclass=pymysql.cursors.DictCursor
        )

    def query(self, sql: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """
        Executes a SELECT query and returns the results.

        Args:
            sql (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.

        Returns:
            List[Dict]: A list of rows as dictionaries.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or ())
                return cursor.fetchall()
        except Exception as e:
            print("Query error:", e)
            return []

    def execute(self, sql: str, params: Optional[tuple] = None) -> bool:
        """
        Executes an INSERT, UPDATE, or DELETE query.

        Args:
            sql (str): The SQL command.
            params (tuple, optional): Parameters for the query.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or ())
            self.connection.commit()
            return True
        except Exception as e:
            print("Execution error:", e)
            return False

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self.connection.close()