import os
import pymysql


connection = pymysql.connect(
    host=os.environ['HOST'],
    port=int(os.environ['PORT']),
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database="defaultdb",
    ssl={
        "ca": "ca.pem"
    }
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        result = cursor.fetchone()
        print("MySQL version:", result)
finally:
    connection.close()