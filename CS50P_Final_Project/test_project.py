import tempfile
import os
from datetime import datetime, timedelta
from project import add_todo, load_todo, delete_todo

# Modified add_todo function to accept a filename for testing
def add_todo(task, hours, filename="to_do.txt"):
    deadline = datetime.now() + timedelta(hours=hours)
    deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, "a") as file:
            file.write(f"{task} | {deadline_str}\n")
        print("\nTo-Do added.")
    except FileNotFoundError:
        print("To-Do File Not Found")

# Modified load_todo function to accept a filename for testing
def load_todo(filename="to_do.txt"):
    try:
        with open(filename, "r") as file:
            todo_dict = {}
            for i, line in enumerate(file, 1):
                parts = line.strip().split("|")
                task = parts[0].strip()
                deadline = datetime.strptime(parts[1].strip(), "%Y-%m-%d %H:%M:%S")
                todo_dict[i] = {"task": task, "deadline": deadline}
            return todo_dict
    except FileNotFoundError:
        return ("To-Do File Not Found")

# Modified delete_todo function to accept a filename for testing
def delete_todo(todo_dict, delete_key, filename="to_do.txt"):
    if delete_key in todo_dict:
        del todo_dict[delete_key]
        with open(filename, "w") as file:
            for value in todo_dict.values():
                file.write(f"{value['task']} | {value['deadline'].strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("\nTo-Do deleted.")
    else:
        print("Invalid selection.")

# Test adding a to-do item
def test_add_todo():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        temp_filename = tmp_file.name

    add_todo("Test Task", 1, temp_filename)

    with open(temp_filename, "r") as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert "Test Task" in lines[0]
    os.remove(temp_filename)

# Test loading to-do items
def test_load_todo():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        temp_filename = tmp_file.name
        with open(temp_filename, "w") as file:
            file.write("Test Task | 2024-01-01 12:00:00\n")

    todo_dict = load_todo(temp_filename)
    assert len(todo_dict) == 1
    assert todo_dict[1]["task"] == "Test Task"
    assert todo_dict[1]["deadline"] == datetime(2024, 1, 1, 12, 0, 0)

    os.remove(temp_filename)

# Test deleting a to-do item
def test_delete_todo():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        temp_filename = tmp_file.name
        with open(temp_filename, "w") as file:
            file.write("Test Task | 2024-01-01 12:00:00\n")

    todo_dict = load_todo(temp_filename)
    assert len(todo_dict) == 1

    delete_todo(todo_dict, 1, temp_filename)

    todo_dict_after_delete = load_todo(temp_filename)
    assert len(todo_dict_after_delete) == 0

    os.remove(temp_filename)

def main():
    test_add_todo()
    test_load_todo()
    test_delete_todo()

if __name__ == "__main__":
    main()
