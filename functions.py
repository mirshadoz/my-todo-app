print("I am in functions file")

def read_data(os, path):
    # todo_list = []
    with open(os.path.abspath(path), "r") as file:
        todo_list = file.readlines()
    return todo_list

def write_data(os, path, todos):
    with open(os.path.abspath(path), "w") as file:
        print("Add - Writing to file, todos.txt")
        # todos.append("\n")
        # todos = [todo + "\n" for todo in todos]
        file.writelines(todos)

def remove_new_line(todos):
    return [todo.replace("\n", "") for todo in todos]

def print_list(todos):
    for index, item in enumerate(todos):
        print(f"{index + 1}-{item}")