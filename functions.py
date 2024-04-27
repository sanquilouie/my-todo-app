def get_todo(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, file_path="todos.txt"):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)