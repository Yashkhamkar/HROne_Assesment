from pydantic import BaseModel
from typing import List
from uuid import uuid4


class SizeItem(BaseModel):
    size: str
    quantity: int


class ProductItem(BaseModel):
    name: str
    price: float
    sizes: List[SizeItem]
