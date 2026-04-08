from server_engine import Database

db = Database()

# Test Connection
version = db.query("SELECT VERSION();")
print(version)

db.close()