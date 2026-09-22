import sqlite3

connection = sqlite3.connect("school.db")
# Cursor is the command runner for every SQL statement in this script.
cursor = connection.cursor()

# Build the first table.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER
)
""")

# Build the second table, which stores the related student_id value.
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_id INTEGER
)
""")

# Remove old data so each run starts cleanly.
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM courses")

cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Ava", 10)
)
ava_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Leo", 11)
)
leo_id = cursor.lastrowid

# Use lastrowid values so each course links to the correct student row.
cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Science Club", ava_id)
)
cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Math Team", leo_id)
)

# JOIN combines student names with their matching course names.
cursor.execute("""
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

# Save table changes before closing the database.
connection.commit()
connection.close()