TODO_FILE = 'tudu.list'

# Returns the content from the file
def read_todo():
    with open(TODO_FILE) as f:
        return f.read()


# Overwrites the entire file
def overwrite_todo(content):
    with open(TODO_FILE, "w") as f:
        f.write(content)


# Appends content to the file
def append_todo(content):
    with open(TODO_FILE, "a") as f:
        f.write(content)


# Adds a new todo item with title
def todo_add(title):
    pass


# Lists all current todo items
def todo_list():
    pass


# Marks the todo item with the given title as done
def todo_done(title):
    pass
