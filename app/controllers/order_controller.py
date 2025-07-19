from fastapi.responses import JSONResponse
from app.config.db import db
from uuid import uuid4
from app.models.order_model import Order

orders = db.orders
products = db.products


def create_order(order: Order):
    order_id = str(uuid4())

    items_list = []
    for item in order.items:
        product = products.find_one({"_id": item.productId})
        if not product:
            return JSONResponse(
                status_code=400,
                content={"error": f"Invalid productId: {item.productId}"},
            )

        item_dict = {"productId": item.productId, "qty": item.qty}
        items_list.append(item_dict)

    order_data = {"_id": order_id, "userId": order.userId, "items": items_list}

    try:
        orders.insert_one(order_data)
        return JSONResponse(status_code=201, content={"id": order_id})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


def get_user_orders(user_id: str, limit: int, offset: int):
    try:
        pipeline = [
            {"$match": {"userId": user_id}},
            {"$unwind": "$items"},
            {
                "$lookup": {
                    "from": "products",
                    "localField": "items.productId",
                    "foreignField": "_id",
                    "as": "product_info",
                }
            },
            {"$unwind": "$product_info"},
            {
                "$addFields": {
                    "itemTotal": {"$multiply": ["$items.qty", "$product_info.price"]}
                }
            },
            {
                "$group": {
                    "_id": "$_id",
                    "items": {
                        "$push": {
                            "productDetails": {
                                "name": "$product_info.name",
                                "id": "$product_info._id",
                            },
                            "qty": "$items.qty",
                        }
                    },
                    "total": {"$sum": "$itemTotal"},
                }
            },
            {"$skip": offset},
            {"$limit": limit},
        ]

        orders_result = list(db.orders.aggregate(pipeline))
        for order in orders_result:
            order["id"] = str(order.pop("_id"))

        return JSONResponse(
            status_code=200,
            content={
                "data": orders_result,
                "page": {
                    "next": str(offset + limit),
                    "limit": limit,
                    "previous": max(offset - limit, 0),
                },
            },
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
