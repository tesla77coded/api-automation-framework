from pydantic import BaseModel


class OrderResponse(BaseModel):
    order_id: str
    total: int
    status: str


class PaymentResponse(BaseModel):
    order_id: str
    payment_status: str
