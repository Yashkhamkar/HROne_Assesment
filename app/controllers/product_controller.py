from fastapi.responses import JSONResponse
from app.config.db import db
from uuid import uuid4

products = db.products


def create_product(product):
    product_id = str(uuid4())
    sizes_list = []
    for size in product.sizes:
        sizes_list.append({"size": size.size, "quantity": size.quantity})

    data = {
        "_id": product_id,
        "name": product.name,
        "price": product.price,
        "sizes": sizes_list,
    }
    try:
        products.insert_one(data)
        return JSONResponse(status_code=201, content={"id": product_id})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if size:
        query["sizes.size"] = size

    try:
        cursor = products.find(query, {"sizes": 0}).skip(offset).limit(limit)
        product_list = []
        for product in cursor:
            product["_id"] = str(product["_id"])  # Convert ObjectId to string
            product_list.append(product)
        return JSONResponse(
            status_code=200,
            content={
                "data": product_list,
                "page": {
                    "next": str(offset + limit),
                    "limit": limit,
                    "previous": max(offset - limit, 0),
                },
            },
        )

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
