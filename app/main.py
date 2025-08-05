# from fastapi import FastAPI
# from app.routes import task_routes, user_routes

# app = FastAPI(
#     title="Walmart Scraper FastAPI Project",
#     version="1.0"
# )
# """
# FastAPI application instance for the Walmart product scraper project.

# Includes routers for:
# - Task-related endpoints under the "/tasks" prefix (e.g., starting scraping tasks)
# - User-related endpoints under the "/users" prefix (e.g., creating users)
# """

# app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
# app.include_router(user_routes.router, prefix="/users", tags=["Users"])












# from fastapi import FastAPI
# from app.routes import task_routes

# app = FastAPI()
# app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])





# from app.routes import user_routes
# app.include_router(user_routes.router, prefix="/users", tags=["Users"])

# from app.routes import product_routes
# app.include_router(product_routes.router, prefix="/products", tags=["Products"])





# from fastapi import FastAPI
# from app.routes import user_routes, task_routes, product_routes

# app = FastAPI(
#     title="Walmart Scraper FastAPI Project",
#     version="1.0"
# )

# app.include_router(user_routes.router, prefix="/users", tags=["Users"])
# app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
# app.include_router(product_routes.router, prefix="/products", tags=["Products"])
from fastapi import FastAPI
from app.routes import user_routes, task_routes, product_routes

app = FastAPI(
    title="Walmart Scraper FastAPI Project",
    version="1.0"
)
"""
FastAPI application instance for the Walmart Scraper project.

This application provides RESTful APIs for managing:
- Users (`/users`)
- Tasks (`/tasks`)
- Products (`/products`)
"""

# Include user-related routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
"""
Routes under /users handle user creation and management.
"""

# Include task-related routes
app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
"""
Routes under /tasks handle background scraping tasks and tracking.
"""

# Include product-related routes
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
"""
Routes under /products handle retrieval and storage of scraped product data.
"""
