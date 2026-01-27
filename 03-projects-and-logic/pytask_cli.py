import json
import os

from numpy import rint
file_name = "tasks.json"
def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)
def main():
    tasks = load_tasks()
    while True:
        print("Welcome to the Task Manager!")
        print("1 Add tasks")
        print("2 View tasks")
        print("3 Exit")
        input_choice = input("Choose an option: ")
        if input_choice == "1":
            task = input("Enter the task description: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif input_choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif input_choice == "3":
            print("Exiting the Task Manager. Goodbye!")
            break
main()