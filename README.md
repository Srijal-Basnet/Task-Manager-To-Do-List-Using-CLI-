# Task Manager CLI App 

A command-line task manager built with Python using Typer, Rich, and SQLite3.

## Features

- Add new tasks
- Update task name/category
- Mark tasks complete
- Delete tasks
- Show all tasks in a table

## Tech Stack

- Python
- Typer (CLI framework)
- Rich (Console UI)
- SQLite3 (Local DB)

## Setup

```bash
pip install typer rich
```
## Usage

```bash
# Add a task
python TodoCLI.py add "Workout" "Fitness"

# Show all tasks
python TodoCLI.py show

# Mark a task as complete (use the ID shown in the table)
python TodoCLI.py complete 1

# Update a task's name or category
python TodoCLI.py update 1 --task "Morning Yoga" --category "Health"

# Delete a task
python TodoCLI.py delete 1
```
