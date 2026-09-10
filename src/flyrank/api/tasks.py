from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
import flyrank.store as store
from flyrank.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter()

@router.get("/tasks", response_model=List[Task], summary="List Tasks", description="Returns a list of all tasks. Can be filtered by completion status or searched by title.")
def get_tasks(
    done: Optional[bool] = Query(None, description="Filter tasks by completion status"),
    search: Optional[str] = Query(None, description="Filter tasks by a search term in the title")
):
    filtered_tasks = store.tasks_db
    if done is not None:
        filtered_tasks = [t for t in filtered_tasks if t["done"] == done]
    if search is not None:
        filtered_tasks = [t for t in filtered_tasks if search.lower() in t["title"].lower()]
    return filtered_tasks

@router.get("/tasks/{id}", response_model=Task, summary="Get a Task", description="Returns a specific task by its ID.")
def get_task(id: int):
    for task in store.tasks_db:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, summary="Create a Task", description="Creates a new task with the provided title.")
def create_task(task_in: TaskCreate):
    new_task = {
        "id": store.next_id,
        "title": task_in.title,
        "done": False
    }
    store.tasks_db.append(new_task)
    store.next_id += 1
    return new_task

@router.put("/tasks/{id}", response_model=Task, summary="Update a Task", description="Updates an existing task's title or completion status.")
def update_task(id: int, task_in: TaskUpdate):
    for task in store.tasks_db:
        if task["id"] == id:
            if task_in.title is not None:
                task["title"] = task_in.title
            if task_in.done is not None:
                task["done"] = task_in.done
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@router.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a Task", description="Deletes a task by its ID.")
def delete_task(id: int):
    for i, task in enumerate(store.tasks_db):
        if task["id"] == id:
            del store.tasks_db[i]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {id} not found")

@router.get("/stats", summary="Get Statistics", description="Returns statistics about the tasks.")
def get_stats():
    total = len(store.tasks_db)
    done_count = sum(1 for t in store.tasks_db if t["done"])
    open_count = total - done_count
    return {
        "total": total,
        "done": done_count,
        "open": open_count
    }
