from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Product(id=1,name="Mobile",description="Phone",price=99.99, quantity=10), # if using Basemodel : Product(id=1,namw="Mobile",description="Phone",price=99.99, quantity=10)
    Product(id=2,name="Laptop",description="Laptop",price=199.99, quantity=20)
]

@app.get("/products")
def get_products():
    return products

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