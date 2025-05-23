import typer
import sqlite3
from rich.console import Console
from rich.table import Table

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

console = Console()

app = typer.Typer()

@app.command(short_help='Add an item')
def add(task: str,category: str = "General"):
    cursor.execute("INSERT INTO tasks (task,category) VALUES (?,?)",(task,category))
    conn.commit()
    console.print(f"[green]Task added:[/] {task} in category [bold]{category}[/bold]")

@app.command(short_help='Delete an item')
def delete(position: int):
    cursor.execute("DELETE FROM tasks WHERE id = ?",(position,))
    conn.commit()
    console.print(f"[red]Deleted task ID:[/] {position}")

@app.command(short_help='Update an item')
def update(position: int, task: str = None, category: str = None):
    if task:
        cursor.execute("UPDATE tasks SET task = ? where id = ?",(task,position))
        
    if category:
        cursor.execute("UPDATE tasks SET category = ? where id = ?",(category,position))
    conn.commit()
    console.print(f"[blue]Updated task ID:[/] {position}")

@app.command(short_help='Complete a task')
def complete(position: int):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?",(position,))
    conn.commit()
    console.print(f"[green]Marked task ID {position} as completed![/green]")

@app.command(short_help='Show the Table')
def show():
    table = Table(title="Task Manager CLI App")
    table.add_column("ID",style = "white",justify= "right")
    table.add_column("Task",style = "cyan")
    table.add_column("Category",style= "green")
    table.add_column("Status", style="yellow")

    cursor.execute("SELECT * from tasks")

    rows = cursor.fetchall()
    for row in rows:
        status = "✅" if row[3] else "❌"
        table.add_row(str(row[0]), row[1], row[2], status)
    console = Console()
    console.print(table)

if __name__ == "__main__":
    app()
