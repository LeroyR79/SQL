# Lesson 3 - Query Data with SELECT

## Time

**75 minutes**

## Learning goals

By the end of this lesson, you should be able to:

- use `SELECT` to read data
- use `fetchall()` to get query results in Python
- loop through rows and print results clearly

## Why this matters

You will likely care most about seeing stored information again, so reading data is where SQL starts to feel practical and rewarding.

## Key theory

- `SELECT` reads data from a table.
- `*` means "all columns."
- Python can store query results in lists of rows.
- Clean output helps you understand what the data means.

## Glossary

- **SELECT**: SQL command used to read data
- **query**: a request for data
- **result**: the data returned by a query
- **cursor**: object used to run SQL commands
- **fetchall**: gets all returned rows from a query

## Explicit code

Create a file named `lesson3_select.py`:

```python
"""Lesson 3: Query students with SELECT and print the results."""

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
```

## Your activity

1. Type the script yourself in VS Code (do not paste the full block at once).
2. Run the script and read the output.
3. Change the query to `SELECT name FROM students`.
4. Add one more student in the database with your own name choice and run again.
5. Before each run, predict how many rows/columns you expect, then compare with actual output.
1. Run the script and read the output.
2. Change the query to `SELECT name FROM students`.
3. Add one more row in the database and run the script again.
4. Count how many rows are returned.

## Stretch challenge

- Format the output as:

```python
for student_id, name, year_group in rows:
    print(f"{name} is in year {year_group}.")
```
- Explain why the formatted output is easier to read than printing raw tuples.

## Exit check

- What is the job of `SELECT`?
- What type of value does `fetchall()` return?
