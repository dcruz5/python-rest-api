from typing import Optional 
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from pathlib import Path
import json

from .models import Product
from .schemas import CreateProduct, UpdateProduct
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event('startup')
async def startup_event():
    db = SessionLocal()
    products = db.query(Product).count()
    if products == 0:   
        datapath = Path('src') / 'data' / 'products.json'
        with open(datapath, 'r') as f:
            data = json.load(f)
            for product in data['products']:
                db.add(Product(**product))
            db.commit()
    else:
        print(f"{products} in store.")
    db.close()

@app.get('/', tags=['Info'])
def get_products(db:Session = Depends(get_db)):
    return {"items_count": db.query(Product).count()}

# response_model=List[Item]
@app.get('/items')
def get_products(db: Session = Depends(get_db), limit:Optional[int] = None):
    if limit != None:
        return db.query(Product).limit(limit).all()
    return db.query(Product).all()


@app.get('/items/{item_id}')
def get_product_by_id(item_id: int, db: Session = Depends(get_db)):
    found_product = db.query(Product).filter(Product.id ==item_id).first()
    
    if found_product:
        return found_product
    
    raise HTTPException(status_code=404, detail="The item ID doesn't exist. Try again.")


@app.post('/items/', status_code=201)
def create_product(item: CreateProduct, db: Session = Depends(get_db)):
    new_product = Product(
        name = item.name,
        stock = item.stock,
        price = item.price,
        brand = item.brand
    )
    
    db.add(new_product)
    db.commit()
    return {"created_id" : new_product.id}

    #raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")


@app.put('/items/{item_id}', status_code=201)
def update_product(item_id: int, item: UpdateProduct, db: Session = Depends(get_db)):
    product = db.query(Product).where(Product.id == item_id)
    # for product in products: 
    #     if product["id"] == item_id:
    #         product["name"] = item.name or product['name']
    #         product["stock"] = item.stock or product['stock'] 
    #         product["price"] = item.price or product['price']
    #         product["brand"] = item.brand or product['brand']
    #         return {"Result": "item updated"}
    # raise HTTPException(status_code=400, detail="The item ID doesn't exist. Try again.")    
   
    
@app.delete('/items/{item_id}')
def delete_product(item_id: int, db: Session = Depends(get_db)):
    
    db.query(Product).filter(Product.id == item_id).delete()
    db.commit()
    return {"Response": "Item deleted."}

    # raise HTTPException(status_code= 400, detail="The item ID does n't exist. Try again.")
