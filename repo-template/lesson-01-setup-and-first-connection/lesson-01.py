import sqlite3
# Open a connection to school.db (SQLite creates the file if needed).
connection = sqlite3.connect("library.db")
print("Database connected!")
# Close the connection so the file is safely released.
connection.close()
print("Database closed!")

