"""
Codveda Internship — Level 2, Task 1: To-Do List Application
Author: Clemence
Description: Command-line task manager. Tasks are persisted in JSON.
             Supports add, list, done, delete, with error handling.

Usage:  python task2_todo_list.py
Commands inside the app:
  list              — Show all tasks
  add <title>       — Add a task
  done <id>         — Mark task complete
  delete <id>       — Remove a task
  clear             — Delete ALL completed tasks
  help              — Show commands
  quit              — Exit
"""

import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    # If the file doesn't exist yet, return an empty list
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    print("\n--- Current Tasks ---")
    for index, task in enumerate(tasks):
        status = " Done" if task["completed"] else " Pending"
        print(f"{index + 1}. {task['title']} [{status}]")

def main_todo():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task description: ")
            tasks.append({"title": title, "completed": False})
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= idx < len(tasks):
                        tasks[idx]["completed"] = True
                        save_tasks(tasks)
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Enter task number to delete: ")) - 1
                    if 0 <= idx < len(tasks):
                        removed = tasks.pop(idx)
                        save_tasks(tasks)
                        print(f"Deleted task: '{removed['title']}'")
                    else:
                        print("Error: That task number does not exist.")  # Error handling requirement
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please pick between 1 and 5.")

# Run the app
main_todo()
