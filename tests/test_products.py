from clients.product_client import ProductClient
from schemas.product_schema import ProductResponse


def test_get_products_schema():
    client = ProductClient()

    response = client.get_products()

    assert response.status_code == 200

    data = response.json()

    validated = ProductResponse.model_validate(data)

    assert validated is not None


def test_products_business_login():
    client = ProductClient()

    response = client.get_products()
    data = response.json()

    for product_id, product in data.items():
        assert product["price"] > 0
        assert product["stock"] >= 0
