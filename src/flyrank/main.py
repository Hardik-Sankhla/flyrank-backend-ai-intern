from fastapi import FastAPI
from flyrank.api.tasks import router as tasks_router
from flyrank.store import reset_tasks_store

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing a to-do list",
    version="1.0"
)

# --- Routes ---
app.include_router(tasks_router)

# --- Base Endpoints ---

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

@app.post("/reset", summary="Reset Tasks", description="Resets the task list to its initial state.")
def reset_tasks():
    """
    Restores the initial 3 example tasks and resets the ID counter.
    """
    reset_tasks_store()
    return {"message": "Tasks reset to initial state"}
