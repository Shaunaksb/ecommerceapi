from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from pymongo import MongoClient

class Item(BaseModel):
    productId: str
    boughtQuantity: int

class Address(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    items: List[Item]
    totalAmount: float
    userAddress: Address

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
orders_collection = db['orders']

@app.post("/orders/")
async def create_order(order: Order):
    order_dict = order.dict()
    order_dict['createdOn'] = datetime.now()

    result = orders_collection.insert_one(order_dict)

    inserted_order = orders_collection.find_one({'_id': result.inserted_id})
    inserted_order['_id'] = str(inserted_order['_id'])

    return inserted_order