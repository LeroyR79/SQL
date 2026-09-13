# Lesson 6 - Build a Mini Project in Python

## Time

**60 minutes**

## Learning goals

By the end of this lesson, you should be able to:

- combine previous skills in one script
- create a simple menu-driven Python program
- store and display records from a SQLite database

## Why this matters

The mini project gives you a chance to combine isolated skills into one complete workflow you can explain and extend.

## Key theory

- Small projects help you connect isolated skills into one workflow.
- Breaking work into steps makes database programs easier to understand.
- Reusing simple SQL commands is enough to build a useful beginner app.

## Glossary

- **CRUD**: create, read, update, delete
- **menu**: a set of choices shown to the user
- **workflow**: the order of steps in a process

## Explicit code

Create a file named `lesson6_project.py`:

```python
"""Lesson 6: Build a small books database script."""

import sqlite3

connection = sqlite3.connect("school.db")
# Cursor executes SQL commands and reads query results.
cursor = connection.cursor()

# Create the books table once, then reuse it on later runs.
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

# Reset demo data so lesson output stays consistent.
cursor.execute("DELETE FROM books")

# Add sample book records.
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Holes", "Louis Sachar"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Wonder", "R. J. Palacio"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Hobbit", "J. R. R. Tolkien"))
# Query all books in alphabetical order by title.
cursor.execute("SELECT title, author FROM books ORDER BY title")

# fetchall() gives a list of (title, author) tuples to loop through.
for title, author in cursor.fetchall():
    print(f"{title} by {author}")

# Commit saves inserted rows to the database file.
connection.commit()
connection.close()
```

## Your activity

1. Build the script exactly as shown.
2. Add two more books.
3. Run the script and confirm all books print in order.
4. Explain which parts are Python and which parts are SQL.

## Stretch challenge

- Turn the script into a simple menu with options such as:
  - add a book
  - show all books
  - exit

## Exit check

- Which skills from earlier lessons were reused here?
- What would you add next to improve the app?
