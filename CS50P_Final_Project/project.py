import sys
import time
from datetime import datetime, timedelta
import os

# Load to-do items from file
def load_todo():
    try:
        with open("to_do.txt", "r") as file:
            todo_dict = {}
            for i, line in enumerate(file, 1):
                parts = line.strip().split("|")
                task = parts[0].strip()
                deadline = datetime.strptime(parts[1].strip(), "%Y-%m-%d %H:%M:%S")
                todo_dict[i] = {"task": task, "deadline": deadline}
            return todo_dict
    except FileNotFoundError:
        return ("To-Do File Not Found")

# Clear console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display to-do list and remaining time
def show_todo(todo_dict):
    if not todo_dict:
        print("\nTo-Do list is empty")
    else:
        for _ in range(5):  # 5 seconds
            clear_screen()
            print("\nTO-DO")
            print("------")
            now = datetime.now()
            for key, value in todo_dict.items():
                task = value["task"]
                deadline = value["deadline"]
                time_left = deadline - now
                if time_left.total_seconds() > 0:
                    # Calculate hours, minutes, and seconds left
                    hours, remainder = divmod(time_left.total_seconds(), 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"{key}. {task} (Time Left: {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds)")
                else:
                    # If time is up
                    print(f"{key}. {task} (Time's Up)")
            time.sleep(1)

# Add new to-do
def add_todo():
    add = input("Add new To-Do: ").strip()
    hours = int(input("How many hours do you give? "))
    deadline = datetime.now() + timedelta(hours=hours)
    deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("to_do.txt", "a") as file:
            file.write(f"{add} | {deadline_str}\n")
        print("\nTo-Do added.")
    except FileNotFoundError:
        print("To-Do File Not Found")

# Delete selected to-do
def delete_todo(todo_dict):
    # Instead of showing live countdown, show a static view
    clear_screen()
    print("\nTO-DO")
    print("------")
    now = datetime.now()
    for key, value in todo_dict.items():
        task = value["task"]
        deadline = value["deadline"]
        time_left = deadline - now
        if time_left.total_seconds() > 0:
            hours, remainder = divmod(time_left.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{key}. {task} (Time Left: {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds)")
        else:
            print(f"{key}. {task} (Time's Up)")

    try:
        delete_key = int(input("Select which To-Do you want to delete: "))
        if delete_key in todo_dict:
            del todo_dict[delete_key]
            with open("to_do.txt", "w") as file:
                for value in todo_dict.values():
                    file.write(f"{value['task']} | {value['deadline'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            print("\nTo-Do deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def main():
    print("\n--> Hi, Welcome to To-Do List <--\n")
    print("##################################################################\n")

    while True:
        print()
        print("-----------------------")
        print("Show To-Do list (1)")
        print("Add To-Do (2)")
        print("Delete To-Do (3)")
        print("Exit (4)")
        print("-----------------------")
        print()

        choice = int(input("Select: "))
        todo_dict = load_todo()
        if choice == 1:
            show_todo(todo_dict)
        elif choice == 2:
            add_todo()
        elif choice == 3:
            delete_todo(todo_dict)
        elif choice == 4:
            sys.exit("\n--> See you later <--\n")
        else:
            print("Try again.")
            continue

if __name__ == "__main__":
    main()
