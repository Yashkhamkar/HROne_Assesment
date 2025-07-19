from fastapi import FastAPI
from config.db import test_connection, create_indexes
from routes.product_route import router as product_router
from routes.order_route import router as order_router

app = FastAPI(
    title="Ecommerce API",
    description="Backend for a simple ecommerce app using FastAPI + MongoDB",
    version="1.0.0",
)

test_connection()
create_indexes()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


app.include_router(product_router)
app.include_router(order_router)
