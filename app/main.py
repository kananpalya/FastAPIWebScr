from fastapi import FastAPI
from app.routes import task_routes, user_routes

app = FastAPI(
    title="Walmart Scraper FastAPI Project",
    version="1.0"
)
"""
FastAPI application instance for the Walmart product scraper project.

Includes routers for:
- Task-related endpoints under the "/tasks" prefix (e.g., starting scraping tasks)
- User-related endpoints under the "/users" prefix (e.g., creating users)
"""

app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
