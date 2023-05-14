from typing import Optional
from fastapi import FastAPI, HTTPException
from .models import Item, UpdateItem
from pathlib import Path
import json

app = FastAPI()

products = []

@app.on_event('startup')
async def startup_event():
    datapath = Path('src') / 'data' / 'products.json'
    with open(datapath, 'r') as f:
        data = json.load(f)
        for product in data['products']:
            products.append(Item(**product).dict())
            

@app.get('/', tags=['Info'])
def get_products():
    return {"items_count": len(products)}


@app.get('/items')
def get_products(limit: Optional[int] = None):
    if limit != None:
        return products[:limit]
    return products


@app.get('/items/{item_id}')
def get_product_by_id(item_id: int):
    for item in products:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="The item ID doesn't exist. Try again.")


@app.post('/items/{item_id}', status_code=201)
def create_product(item_id: int, item: Item):
    for product in products:
        if product["id"] == item_id:
            raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")
    new_item = {"id": item_id, "name": item.name, "stock": item.stock, "price": item.price}
    products.append(new_item)


@app.put('/items/{item_id}', status_code=201)
def update_product(item_id: int, item: UpdateItem):
    for product in products:
        if product["id"] == item_id:
            if item.name != None:
                product["name"] = item.name
            if item.stock != None:
                product["stock"] = item.stock
            if item.price != None:
                product["price"] = item.price
            if item.brand != None:
                product["brand"] = item.brand
            return {"Result": "item updated"}
    raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")    
   
    
@app.delete('/items/{item_id}')
def delete_product(item_id: int):
    for product in products:
        if product["id"] == item_id:
            products.remove(product)
            return {"Response": "Item deleted."}
    raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")
