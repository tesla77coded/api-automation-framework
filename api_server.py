from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()


# -------------- In Memory State -------------------

USERS = {"test@example.com": {"password": "password123", "token": None}}
PRODUCTS = {
    1: {"name": "Laptop", "price": 1000, "stock": 5},
    2: {"name": "Phone", "price": 500, "stock": 10},
}

ORDERS = {}


# ------------------ SCHEMAS ---------------------
class LoginRequest(BaseModel):
    email: str
    password: str


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class CreateOrderRequest(BaseModel):
    items: list[OrderItem]


# ------------------ ROUTES ---------------------
@app.post("/login")
def login(data: LoginRequest):
    user = USERS.get(data.email)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    token = str(uuid.uuid4())
    user["token"] = token

    return {"access_token": token}


@app.get("/products")
def get_products():
    return PRODUCTS


@app.post("/orders")
def create_orders(data: CreateOrderRequest):
    total = 0

    for item in data.items:
        product = PRODUCTS.get(item.product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product["stock"] < item.quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock")

        total += product["price"] * item.quantity

    order_id = str(uuid.uuid4())

    ORDERS[order_id] = {"items": data.items, "total": total, "status": "CREATED"}

    # reduce inventory
    for item in data.items:
        PRODUCTS[item.product_id]["stock"] -= item.quantity

    return {"order_id": order_id, "total": total, "status": "CREATED"}


@app.post("/pay/{order_id}")
def pay_order(order_id: str):

    order = ORDERS.get(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order["status"] = "PAID"

    return {"order_id": order_id, "payment_status": "SUCCESS"}


@app.post("/reset")
def reset_state():
    global PRODUCTS, ORDERS

    PRODUCTS = {
        1: {"name": "Laptop", "price": 1000, "stock": 5},
        2: {"name": "Phone", "price": 500, "stock": 10},
    }

    ORDERS = {}

    return {"status": "reset"}
