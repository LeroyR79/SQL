import sqlite3
# Connect Python to the SQLite database file.
connection = sqlite3.connect("school.db")
# A cursor is the object that sends SQL commands to the database.
cursor = connection.cursor()

# Execute SQL to create the students table if it does not exist yet.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER,
    test_mark INTEGER,
    grade TEXT NOT NULL
    )
""")

# Clear old rows so this lesson script gives predictable output each run.
cursor.execute("DELETE FROM students")

# Insert rows using placeholders (?) to safely pass Python values.
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Adrian", 10, 10, "N"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Oscar", 10, 50, "C"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Marlon", 10, 100, "A"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Terence", 10, 80, "B"))

# Commit saves all changes made by INSERT/DELETE/CREATE statements.
connection.commit()
# Always close the connection when finished.
connection.close()