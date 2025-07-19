from fastapi.responses import JSONResponse
from config.db import db
from uuid import uuid4
from models.order_model import Order

orders = db.orders


def create_order(order: Order):
    order_id = str(uuid4())

    items_list = []
    for item in order.items:
        item_dict = {"productId": item.productId, "qty": item.qty}
        items_list.append(item_dict)

    order_data = {"_id": order_id, "userId": order.userId, "items": items_list}

    try:
        orders.insert_one(order_data)
        return JSONResponse(status_code=201, content={"id": order_id})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
