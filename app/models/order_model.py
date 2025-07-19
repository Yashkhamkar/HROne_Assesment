from pydantic import BaseModel, Field
from typing import List


class OrderItem(BaseModel):
    productId: str
    qty: int = Field(gt=0, description="Quantity must be greater than 0")


class Order(BaseModel):
    userId: str
    items: List[OrderItem] = Field(min_items=1, description="At least one item required")
