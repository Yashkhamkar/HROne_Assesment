from fastapi import FastAPI
from config.db import test_connection
from routes.product_route import router as product_router

app = FastAPI(
    title="Ecommerce API",
    description="Backend for a simple ecommerce app using FastAPI + MongoDB",
    version="1.0.0",
)

test_connection()  # Test the database connection on startup

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

app.include_router(product_router)