from clients.product_client import ProductClient
from clients.order_client import OrderClient
from schemas.order_schema import OrderResponse, PaymentResponse


def test_order_full_flow():
    product_client = ProductClient()
    order_client = OrderClient()

    # get products
    products = product_client.get_products().json()

    first_product_id = list(products.keys())[0]
    first_product = products[first_product_id]

    initial_stock = first_product["stock"]
    price = first_product["price"]

    # create order
    items = [{"product_id": int(first_product_id), "quantity": 1}]

    order_response = order_client.create_order(items)

    assert order_response.status_code == 200

    order_data = OrderResponse.model_validate(order_response.json())

    assert order_data.total == price
    assert order_data.status == "CREATED"

    # inventory validation
    updated_products = product_client.get_products().json()
    updated_stock = updated_products[first_product_id]["stock"]

    assert updated_stock == initial_stock - 1

    # payment
    payment_response = order_client.pay_order(order_data.order_id)

    assert payment_response.status_code == 200

    payment_data = PaymentResponse.model_validate(payment_response.json())

    assert payment_data.payment_status == "SUCCESS"
