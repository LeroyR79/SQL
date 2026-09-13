# Lesson 1 - Setup and First Database Connection

## Time

**60 minutes**

## Learning goals

By the end of this lesson, you should be able to:

- explain what a database is
- explain what SQLite is
- open a project in VS Code
- run a Python file from the terminal
- connect to a SQLite database with Python

## Why this matters

You need a clear mental model of how Python, SQLite, files, and VS Code fit together before you can write useful database programs.

## Before you start

You should have:

- VS Code installed
- Python 3 installed
- permission to create files in a project folder
- access to the VS Code terminal

## Key theory

- A **database** stores information in an organized way.
- **SQLite** is a lightweight database engine that stores data in a single file.
- **Python** can talk to SQLite using the built-in `sqlite3` module.
- A **connection** lets Python open and work with a database file.
- Running a Python script from the terminal executes the instructions in the file from top to bottom.
- If the database file does not exist yet, SQLite creates it when Python connects to it.

## Glossary

- **database**: an organized collection of data
- **table**: a grid of rows and columns
- **row**: one record in a table
- **column**: one type of information in a table
- **SQLite**: a file-based SQL database engine
- **connection**: the active link between Python and the database
- **script**: a saved Python file
- **terminal**: the text-based area where commands are typed and run

## Explicit code

Inside your project folder, create a file named `lesson1_connect.py`:

```python
"""Lesson 1: Connect to a SQLite database file."""

import sqlite3

# Open a connection to school.db (SQLite creates the file if needed).
connection = sqlite3.connect("school.db")
print("Database connected!")
# Close the connection so the file is safely released.
connection.close()
print("Database closed!")
```

Run it in the VS Code terminal:

```bash
python lesson1_connect.py
```

Expected output:

```text
Database connected!
Database closed!
```

## Your activity

1. Open VS Code.
2. Create a folder for the project and open that folder in VS Code.
3. Open the VS Code terminal.
4. Create `lesson1_connect.py`.
5. Type the code exactly as shown.
6. Run the file from the terminal.
7. Confirm that the terminal prints both messages.
8. Confirm that a `school.db` file appears in the folder.
9. Ask a partner to explain what part of the script creates the database file.

## Stretch challenge

- Change the database file name to `library.db`.
- Add one more `print()` line explaining what the script is doing before the connection opens.
- Delete the database file, run the script again, and explain what happened.

## Exit check

- What is the difference between Python and SQLite?
- What file was created when the script ran?
- What does the connection do?
