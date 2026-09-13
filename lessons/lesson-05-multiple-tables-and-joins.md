# Lesson 5 - Work with Multiple Tables

## Time

**75 minutes**

## Learning goals

By the end of this lesson, you should be able to:

- explain why databases often use more than one table
- create a second table
- connect related tables with IDs
- use a simple `JOIN`

## Why this matters

Using more than one table introduces the relational thinking that makes databases powerful and different from simple spreadsheets.

## Key theory

- Real databases often split data into related tables.
- A **foreign key** links one table to another.
- A `JOIN` combines matching information from more than one table.
- Using multiple tables reduces repeated data.

## Glossary

- **foreign key**: a column that points to a row in another table
- **relationship**: how two tables connect
- **JOIN**: SQL operation that combines data from multiple tables
- **duplicate data**: repeated information stored in many places

## Explicit code

Create a file named `lesson5_join.py`:

```python
"""Lesson 5: Create related tables and combine them with a JOIN."""

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
```

## Your activity

1. Type the script yourself in VS Code (do not paste the full block at once).
2. Create both tables in one script.
3. Add one or two course records using your own course names.
4. Before running the `JOIN`, predict which student-course pairs you expect to see.
5. Run the `JOIN` query and compare the actual output with your prediction.
6. Explain which columns are used to connect the tables.

## Stretch challenge

- Add a second course for a different student.
- Ask students to predict the joined output before running the script.
- Ask students to modify one link (`student_id`) and explain how that changed the joined output.
- Add a second course for a different row in `students`.
- Predict the joined output before running the script.

## Exit check

- Why do we use more than one table?
- What is the purpose of `JOIN`?
