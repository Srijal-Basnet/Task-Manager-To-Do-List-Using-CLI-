import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    category TEXT,
    completed BOOLEAN NOT NULL DEFAULT 0  
)
"""
)
# Insert a test task
cursor.execute("INSERT INTO tasks (task, category) VALUES (?, ?)", ("Test task", "Testing"))
conn.commit()

# Fetch and print tasks to verify
cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("DELETE FROM tasks WHERE task = ?", ("Test task",))
conn.commit()
