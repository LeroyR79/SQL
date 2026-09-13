# Lesson 4 - Filter, Sort, and Summarize

## Time

**75 minutes**

## Learning goals

By the end of this lesson, you should be able to:

- use `WHERE` to filter rows
- use `ORDER BY` to sort results
- use `COUNT()` to summarize data

## Why this matters

Filtering and summarizing helps you answer questions with data instead of just printing everything in the table.

## Key theory

- `WHERE` narrows results to matching rows.
- `ORDER BY` changes the order of returned results.
- Aggregate functions such as `COUNT()` summarize data.
- Parameterized queries help keep input handling safe and predictable.

## Glossary

- **WHERE**: filters rows
- **ORDER BY**: sorts rows
- **COUNT()**: counts matching rows
- **aggregate**: a summary calculation over many rows
- **parameterized query**: a query that safely inserts values using placeholders

## Explicit code

Create a file named `lesson4_filter.py`:

```python
"""Lesson 4: Filter, sort, and count rows with SQL."""

import sqlite3

connection = sqlite3.connect("school.db")
# Cursor sends SQL to SQLite and reads results back into Python.
cursor = connection.cursor()

# Python value used in a parameterized query below.
year_group = 10
cursor.execute(
    "SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name",
    (year_group,)
)

rows = cursor.fetchall()
for row in rows:
    print(row)

# COUNT(*) returns one row with one value, so fetchone()[0] gets the number.
cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print("Total students:", total_students)

connection.close()
```

## Your activity

1. Type the script yourself in VS Code (do not paste the full block at once).
2. Run the query for year group 10.
3. Change the value to 11, then try one year group value that returns fewer rows.
4. Compare sorted and unsorted output.
5. Predict the result of `COUNT(*)` before running the code, then check if your prediction was correct.

## Stretch challenge

- Ask students to write a query that only shows one column.
- Ask students to sort by `year_group` first and `name` second.
- Ask students to explain in one sentence why the `?` placeholder is safer than building SQL with string concatenation.
- Write a query that only shows one column.
- Sort by `year_group` first and `name` second.

## Exit check

- What does `WHERE` do?
- Why is `?` used in the query?
