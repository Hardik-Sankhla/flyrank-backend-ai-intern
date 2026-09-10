from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing a to-do list",
    version="1.0"
)

# --- Models ---

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="The title of the task")
    done: Optional[bool] = Field(None, description="The status of the task")

# --- In-memory Data Store ---

def get_initial_tasks():
    return [
        {"id": 1, "title": "Buy groceries", "done": False},
        {"id": 2, "title": "Read a book", "done": True},
        {"id": 3, "title": "Write some code", "done": False}
    ]

tasks_db = get_initial_tasks()
next_id = 4

# --- Endpoints ---

@app.get("/", summary="API Root", description="Returns basic information about the API.")
def get_root():
    """
    Returns basic information about the API, including the name, version, and available endpoints.
    """
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health", summary="Health Check", description="Returns the health status of the server.")
def get_health():
    """
    Returns a simple JSON indicating that the server is alive and functioning.
    """
    return {"status": "ok"}

@app.get("/tasks", response_model=List[Task], summary="List Tasks", description="Returns a list of all tasks. Can be filtered by completion status or searched by title.")
def get_tasks(
    done: Optional[bool] = Query(None, description="Filter tasks by completion status"),
    search: Optional[str] = Query(None, description="Filter tasks by a search term in the title")
):
    """
    Returns the list of tasks. 
    Supports optional query parameters to filter by 'done' status or to 'search' within the title.
    """
    filtered_tasks = tasks_db
    if done is not None:
        filtered_tasks = [t for t in filtered_tasks if t["done"] == done]
    if search is not None:
        filtered_tasks = [t for t in filtered_tasks if search.lower() in t["title"].lower()]
    return filtered_tasks

@app.get("/tasks/{id}", response_model=Task, summary="Get a Task", description="Returns a specific task by its ID.")
def get_task(id: int):
    """
    Fetches a single task by its ID.
    Returns a 404 error if the task is not found.
    """
    for task in tasks_db:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, summary="Create a Task", description="Creates a new task with the provided title.")
def create_task(task_in: TaskCreate):
    """
    Creates a new task. The task's title is required.
    Returns the newly created task and a 201 Created status code.
    Returns 400 Bad Request if the title is empty.
    """
    global next_id
    new_task = {
        "id": next_id,
        "title": task_in.title,
        "done": False
    }
    tasks_db.append(new_task)
    next_id += 1
    return new_task

@app.put("/tasks/{id}", response_model=Task, summary="Update a Task", description="Updates an existing task's title or completion status.")
def update_task(id: int, task_in: TaskUpdate):
    """
    Updates a task by its ID. You can update the 'title', 'done' status, or both.
    Returns the updated task.
    Returns a 404 error if the task is not found.
    """
    for task in tasks_db:
        if task["id"] == id:
            if task_in.title is not None:
                task["title"] = task_in.title
            if task_in.done is not None:
                task["done"] = task_in.done
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a Task", description="Deletes a task by its ID.")
def delete_task(id: int):
    """
    Deletes a task by its ID.
    Returns a 204 No Content status code upon success.
    Returns a 404 error if the task is not found.
    """
    for i, task in enumerate(tasks_db):
        if task["id"] == id:
            del tasks_db[i]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@app.get("/stats", summary="Get Statistics", description="Returns statistics about the tasks.")
def get_stats():
    """
    Returns statistics about the tasks, including the total count, number of done tasks, and number of open tasks.
    """
    total = len(tasks_db)
    done_count = sum(1 for t in tasks_db if t["done"])
    open_count = total - done_count
    return {
        "total": total,
        "done": done_count,
        "open": open_count
    }

@app.post("/reset", summary="Reset Tasks", description="Resets the task list to its initial state.")
def reset_tasks():
    """
    Restores the initial 3 example tasks and resets the ID counter.
    """
    global tasks_db, next_id
    tasks_db = get_initial_tasks()
    next_id = 4
    return {"message": "Tasks reset to initial state"}