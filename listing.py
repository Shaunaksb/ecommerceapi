from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List
from pymongo import MongoClient
from products import generate_products

app = FastAPI()
db_config = {
    'url': 'mongodb://localhost:27017/',
    'db_name': 'ecommerce',
    'collection_name': 'listing'
}

client = MongoClient(db_config['url'])
db = client[db_config['db_name']]
collection = db[db_config['collection_name']]

class Product(BaseModel):
    id: Optional[str] = Field(alias='_id')
    name: str
    price: float
    quantity: int

class Pagination(BaseModel):
    limit: int
    nextOffset: Optional[int]
    prevOffset: Optional[int]
    total: int

class ProductList(BaseModel):
    data: List[Product]
    page: Pagination

@app.on_event("startup")
async def startup_event():
    if collection.count_documents({}) == 0:
        generate_products(db_config)

@app.get("/products/", response_model=ProductList)
async def get_products(limit: int = 10, offset: int = 0, min_price: Optional[float] = None, max_price: Optional[float] = None):
    pipeline = []
    
    if min_price is not None and max_price is not None:
        pipeline.append({"$match": {"price": {"$gte": min_price, "$lte": max_price}}})
    
    pipeline.append({"$facet": {
        "data": [{"$skip": offset}, {"$limit": limit}],
        "metadata": [{"$count": "total"}]
    }})
    
    results = collection.aggregate(pipeline)
    results = list(results)[0]
    for product in results['data']:
        product['_id'] = str(product['_id'])
    return {"data": results['data'], "page": {"limit": limit, "nextOffset": offset + limit if offset + limit < results['metadata'][0]['total'] else None, "prevOffset": offset - limit if offset - limit >= 0 else None, "total": results['metadata'][0]['total']}}