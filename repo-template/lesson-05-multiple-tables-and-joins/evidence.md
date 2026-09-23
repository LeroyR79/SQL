# Lesson 05 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: Commit 1 - Inputted the lesson 5 code
- Commit 2 hash + message: Commit 2 - Finished lesson 5
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python lesson5_join.py
- Terminal output pasted below:

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER,
    test_mark INTEGER,
    grade TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_id INTEGER
)
""")

cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM courses")

cursor.execute(
    "INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)",
    ("Adrian", 10, 50, "C")
)
Adrian_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)",
    ("Marlon", 10, 80, "B")
)
Marlon_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Coding Club", Marlon_id)
)
cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Language Club", Adrian_id)
)

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()

## Prediction before run
- JOIN query version:
- My prediction (student-course pairs): The JOIN command will join the two tables into one.
- What actually happened:

## SQL/Python changes I made
- Change 1: Added test_mark and grade 
- Change 2: Added new students and changed the course names
- Why these changes were mine (not just starter code): 

## Error and fix
- Error I hit: Forgot to add comma when adding new field into the table.
- How I fixed it: ,

## Understanding check (answer in your own words)
1. Why do we use more than one table?
In order to combine tables into one and merge information.
2. What is the purpose of `JOIN`?
Combines data from multiple tables.
3. Which columns connect your two tables?
student_id column.

## Quality checklist
- [x] Script runs without unhandled errors
- [x] I included at least 2 lesson commits
- [x] I included joined output evidence
- [x] I showed a prediction and compared it to actual output
- [x] I made at least 2 personal changes to the starter work
- [x] I answered all questions in my own words
