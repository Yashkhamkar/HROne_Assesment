import pytest
import httpx

BASE_URL = (
    "https://hrone-assesment.onrender.com"  # Replace with your actual Render deployment
)


@pytest.fixture(scope="session")
def client():
    return httpx.Client(base_url=BASE_URL)


# -------------------- Product Creation --------------------
@pytest.fixture(scope="session")
def created_products(client):
    product_1 = {
        "name": "Blue Jeans",
        "price": 1200,
        "sizes": [{"size": "large", "quantity": 5}, {"size": "medium", "quantity": 10}],
    }
    product_2 = {
        "name": "White Shirt",
        "price": 800,
        "sizes": [{"size": "large", "quantity": 2}, {"size": "small", "quantity": 4}],
    }
    res1 = client.post("/products", json=product_1)
    res2 = client.post("/products", json=product_2)
    assert res1.status_code == 201
    assert res2.status_code == 201
    return [res1.json()["id"], res2.json()["id"]]


# -------------------- Tests --------------------


def test_create_product(client):
    payload = {
        "name": "Test Product",
        "price": 100,
        "sizes": [{"size": "medium", "quantity": 5}],
    }
    res = client.post("/products", json=payload)
    assert res.status_code == 201
    assert "id" in res.json()


def test_list_products(client):
    res = client.get("/products")
    assert res.status_code == 200
    data = res.json()
    assert "data" in data and isinstance(data["data"], list)
    assert "page" in data


def test_filter_by_name(client):
    res = client.get("/products?name=shirt")
    assert res.status_code == 200
    assert isinstance(res.json()["data"], list)


def test_filter_by_size(client):
    res = client.get("/products?size=large")
    assert res.status_code == 200
    assert isinstance(res.json()["data"], list)


def test_pagination(client):
    res = client.get("/products?limit=1&offset=0")
    assert res.status_code == 200
    body = res.json()
    assert "page" in body
    assert "next" in body["page"]
    assert "limit" in body["page"]
    assert "previous" in body["page"]


# -------------------- Orders --------------------


def test_create_order_valid(client, created_products):
    payload = {
        "userId": "user_123",
        "items": [
            {"productId": created_products[0], "qty": 2},
            {"productId": created_products[1], "qty": 1},
        ],
    }
    res = client.post("/orders", json=payload)
    assert res.status_code == 201
    assert "id" in res.json()


def test_create_order_invalid_product(client):
    payload = {"userId": "user_123", "items": [{"productId": "invalid-id", "qty": 2}]}
    res = client.post("/orders", json=payload)
    assert res.status_code in [400, 404]


def test_get_orders(client):
    res = client.get("/orders/user_123")
    assert res.status_code == 200
    body = res.json()
    assert "data" in body
    assert "page" in body
