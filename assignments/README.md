# Task CRUD API

This is a simple in-memory CRUD API for managing a to-do list, built with FastAPI. It supports creating, reading, updating, and deleting tasks. It also features optional query parameters for filtering/searching, a stats endpoint, and a reset endpoint.

## Installation & Running

Ensure you have `uv` installed, then run the following command to start the development server:

```bash
uv run uvicorn assignments.main:app --reload
```
*(Note: If you are already inside the `assignments` folder, you can run `uv run uvicorn main:app --reload`)*

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint returning API metadata |
| GET | `/health` | Health check endpoint |
| GET | `/tasks` | List all tasks (supports `?done=true` and `?search=term`) |
| GET | `/tasks/{id}` | Get a specific task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task by ID |
| GET | `/stats` | Get total, open, and done task counts |
| POST | `/reset` | Reset the task list to its initial state |

## Example `curl` Output

Here is an example of creating a new task using `curl`:

```bash
$ curl -s -i -X POST http://127.0.0.1:8000/tasks -H "Content-Type: application/json" -d '{"title":"Test new task"}'

HTTP/1.1 201 Created
date: Mon, 24 Aug 2026 00:37:13 GMT
server: uvicorn
content-length: 45
content-type: application/json

{"id":4,"title":"Test new task","done":false}
```

## Swagger UI Screenshot

![Swagger UI Screenshot](swagger.png)
*(Please replace `swagger.png` with your actual screenshot of the `/docs` page)*
