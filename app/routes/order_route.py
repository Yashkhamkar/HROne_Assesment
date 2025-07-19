from fastapi import APIRouter
from app.models.order_model import Order
from app.controllers.order_controller import create_order, get_user_orders

router = APIRouter()


@router.post("/orders", response_model=dict)
async def create_order_route(order: Order):
    """
    Create a new order.
    """
    return create_order(order)


@router.get("/orders/{user_id}")
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    """
    Get orders for a specific user.
    """

    return get_user_orders(user_id, limit, offset)
