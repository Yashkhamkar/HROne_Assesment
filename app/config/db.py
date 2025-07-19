from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["ecommerce"]


def test_connection():
    try:
        # Ping the MongoDB server
        client.admin.command("ping")
        print("✅ Connected to MongoDB")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)
        raise

def create_indexes():
    try:
        db.products.create_index([("name", "text")])
        db.products.create_index("sizes.size")
        db.orders.create_index("userId")
        print("✅ Indexes created")
    except Exception as e:
        print("❌ Failed to create indexes:", e)
