# 🛍️ E-commerce Backend API – FastAPI + MongoDB

This is a simple e-commerce backend application built with **FastAPI** and **MongoDB**. It allows you to manage products and user orders — similar to basic functionality in apps like Flipkart or Amazon.

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
