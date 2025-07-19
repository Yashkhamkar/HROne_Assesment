from fastapi import APIRouter
from models.product_model import ProductItem
from controllers.product_controller import create_product, list_products

router = APIRouter()

@router.post("/products", status_code=201)
def add_product(product: ProductItem):
    return create_product(product)

@router.get("/products")
def get_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    return list_products(name, size, limit, offset)