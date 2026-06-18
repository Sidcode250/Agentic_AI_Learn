from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
from sqlalchemy.orm import Session
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Product(id=1,name="Mobile",description="Phone",price=99.99, quantity=10), # if using Basemodel : Product(id=1,namw="Mobile",description="Phone",price=99.99, quantity=10)
    Product(id=2,name="Laptop",description="Laptop",price=199.99, quantity=20)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int): # id should be same name in both
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return products

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product added successfully"
    return "No product found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Product not found"