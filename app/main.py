from fastapi import FastAPI
from app.routes import user_routes, task_routes

app = FastAPI(title="Walmart Scraper API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(task_routes.router, prefix="/tasks", tags=["Scraping Tasks"])

@app.get("/")
async def root():
    return {"message": "API is working!"}
