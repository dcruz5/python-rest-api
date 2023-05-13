from typing import Optional
from fastapi import FastAPI, HTTPException
from .schemas import Item, UpdateItem

app = FastAPI()

products = [
    {"id": 1, "name": "cookies", "quantity": 4, "price": 3.20}, 
    {"id": 2, "name": "tuna can", "quantity": 10, "price": 5.00}
]

@app.get('/')
def get_products(limit: Optional[int] = None):
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
    new_item = {"id": item_id, "name": item.name, "quantity": item.quantity, "price": item.price}
    products.append(new_item)


@app.put('/items/{item_id}', status_code=201)
def update_product(item_id: int, item: UpdateItem):
    for product in products:
        if product["id"] == item_id:
            if item.name != None:
                product["name"] = item.name
            if item.quantity != None:
                product["quantity"] = item.quantity
            if item.price != None:
                product["price"] = item.price
            return {"Result": "item updated"}
    raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")    
   
    
@app.delete('/items/{item_id}')
def delete_product(item_id: int):
    for product in products:
        if product["id"] == item_id:
            products.remove(product)
            return {"Response": "Item deleted."}
    raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")
