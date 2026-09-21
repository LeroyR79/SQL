# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: Commit 1 - Start lesson 3
- Commit 2 hash + message: Commit 2 - Changed lesson 3 code
- Optional Commit 3 hash + message: Commit 3 - Finished lesson 3

## Run evidence
- Command run: 
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
    grade TEXT NOT NULL
    )
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Adrian", 10, 10, "N"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Oscar", 10, 50, "C"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Marlon", 10, 100, "A"))
cursor.execute("INSERT INTO students (name, year_group, test_mark, grade) VALUES (?, ?, ?, ?)", ("Terence", 10, 80, "B"))

connection.commit()
connection.close()
To create a new table in order to make changes.

## Prediction before run
- Query version:
- My prediction (rows/columns or sample output): Adds a new column and row for the required changes.
- What actually happened: The changed came through as expected.

## SQL/Python changes I made
- Change 1: Added another row for Terence.
- Change 2: Added a column for Grades.
- Why these changes were mine (not just starter code): These changes were made to change the code and add more people to the table.

## Error and fix
- Error I hit: When adding a column for the grade, errors kept occurring because the system wasn't able to update an already existing table.
- How I fixed it: I deleted the table and allowed the system to make a new one with the new values.

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
SELECT read all the values within a table
2. What type of value does `fetchall()` return?
fetchall() returns all data within a table
3. How did your output change when you selected fewer columns?
The output became smaller.

## Quality checklist
- [x] Script runs without unhandled errors
- [x] I included at least 2 lesson commits
- [x] I included query output evidence
- [x] I showed a prediction and compared it to actual output
- [x] I made at least 2 personal changes to the starter work
- [x] I answered all questions in my own words
