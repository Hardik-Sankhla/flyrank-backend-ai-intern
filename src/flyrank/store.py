def get_initial_tasks():
    return [
        {"id": 1, "title": "Buy groceries", "done": False},
        {"id": 2, "title": "Read a book", "done": True},
        {"id": 3, "title": "Write some code", "done": False}
    ]

tasks_db = get_initial_tasks()
next_id = 4

def reset_tasks_store():
    global tasks_db, next_id
    tasks_db = get_initial_tasks()
    next_id = 4
