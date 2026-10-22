"""
Simple To-Do List App - Python
Author: Salwa Chaib
GitHub: github.com/chaibsalwa
"""

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet! 🎉")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "⏳"
            print(f"{i}. {status} {task['title']}")

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Added: {title}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Completed: {tasks[index]['title']}")
    else:
        print("Invalid task number!")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed['title']}")

# Example usage
if __name__ == "__main__":
    add_task("Learn Python basics")
    add_task("Build GitHub portfolio")
    add_task("Apply to Shipd quests")
    show_tasks()
    complete_task(0)
    show_tasks()
