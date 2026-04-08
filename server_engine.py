import os
import pymysql


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=os.environ['HOST'],
            port=int(os.environ['PORT']),
            user=os.environ['USER'],
            password=os.environ['PASSWORD'],
            database="defaultdb",
            ssl={"ca": "ca.pem"},
            cursorclass=pymysql.cursors.DictCursor  # returns dicts instead of tuples
        )

    def query(self, sql, params=None):
        """SELECT queries"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or ())
                return cursor.fetchall()
        except Exception as e:
            print("Query error:", e)
            return []

    def execute(self, sql, params=None):
        """INSERT, UPDATE, DELETE"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or ())
            self.connection.commit()
            return True
        except Exception as e:
            print("Execution error:", e)
            return False

    def close(self):
        self.connection.close()