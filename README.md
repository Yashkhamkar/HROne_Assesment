
# 🛍️ E-commerce Backend API – FastAPI + MongoDB

This is a simple e-commerce backend application built with **FastAPI** and **MongoDB**. It allows you to manage products and user orders.

---

## 🚀 Features Implemented

- ✅ **Create Products** with sizes and prices
- ✅ **Filter and paginate products** using query params
- ✅ **Create Orders** with multiple products
- ✅ **Get user-specific orders** with product details and totals
- ✅ **MongoDB Aggregation** for calculating totals and product lookups
- ✅ **Indexing** on `name`, `sizes.size`, and `orders.userId` for optimized queries
- ✅ Clean, modular structure using FastAPI + Pydantic
- ✅ Fully compliant response formats for evaluation

---

## 🧠 Tech Stack

- **Backend:** FastAPI (Python 3.11)
- **Database:** MongoDB (Atlas)
- **Driver:** PyMongo
- **Deployment:** [Render](https://render.com)

---

## 📦 API Endpoints

### 🔹 `POST /products`

Create a new product

**Request:**
```json
{
  "name": "Classic Cotton Tee",
  "price": 499.0,
  "sizes": [
    { "size": "medium", "quantity": 10 }
  ]
}
```

**Response:**
```json
{ "id": "product_id_here" }
```

---

### 🔹 `GET /products`

List products with optional filters and pagination

**Query Params:**
- `name` (regex partial match)
- `size` (exact match)
- `limit` (pagination)
- `offset` (pagination)

**Example:**
```
GET /products?name=Denim&size=medium&limit=5&offset=0
```

---

### 🔹 `POST /orders`

Create a user order

**Request:**
```json
{
  "userId": "user_123",
  "items": [
    { "productId": "abc123", "qty": 2 },
    { "productId": "def456", "qty": 1 }
  ]
}
```

**Response:**
```json
{ "id": "order_id_here" }
```

---

### 🔹 `GET /orders/{user_id}`

List all orders for a user with pagination and product details

**Response:**
```json
{
  "data": [
    {
      "id": "order_id",
      "items": [
        {
          "productDetails": {
            "name": "Product Name",
            "id": "product_id"
          },
          "qty": 2
        }
      ],
      "total": 998.0
    }
  ],
  "page": {
    "next": "10",
    "limit": 5,
    "previous": 0
  }
}
```

---

## 🗂️ MongoDB Collections

### `products`
```json
{
  "_id": "uuid",
  "name": "Product Name",
  "price": 1000.0,
  "sizes": [
    { "size": "medium", "quantity": 10 }
  ]
}
```

### `orders`
```json
{
  "_id": "uuid",
  "userId": "user_123",
  "items": [
    { "productId": "uuid", "qty": 2 }
  ]
}
```

---

## 🔎 Indexes Used

```python
db.products.create_index([("name", "text")])
db.products.create_index("sizes.size")
db.orders.create_index("userId")
```

---

## 📊 Aggregation Pipeline Used

- `$lookup` to join product details into orders
- `$unwind`, `$group`, `$addFields` to calculate totals
- `$skip`, `$limit` for pagination
- `$project` / `$addFields` for formatting

---

## 🧪 Testing

- A full `pytest` script is included to test:
  - Product creation
  - Filtering + pagination
  - Order creation (valid/invalid)
  - Order listing with pagination

---

## 🌐 Live Deployment

Base URL:
```
https://hrone-assesment.onrender.com
```

Test endpoints:
- `/products`
- `/orders/user_122`, `/orders/user_123`, etc.
---
