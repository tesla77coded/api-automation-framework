import random


def create_order_payload(product_id, max_qty=3):
    return [{"product_id": product_id, "quantity": random.randint(1, max_qty)}]
