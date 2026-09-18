import sqlite3

connection = sqlite3.connect("school.db")
# The cursor runs SQL queries and returns their results to Python.
cursor = connection.cursor()

# Run a SELECT query to read columns from the students table.
cursor.execute("SELECT id, name, year_group FROM students")
# fetchall() returns a list of all rows from the most recent query.
rows = cursor.fetchall()

# Each row is a tuple like (id, name, year_group).
for row in rows:
    print(row)

# Close the connection when all reading is complete.
connection.close()