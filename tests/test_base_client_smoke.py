from clients.base_client import BaseClient


def test_base_client_smoke():
    client = BaseClient()

    response = client.request("GET", "/products")

    assert response.status_code == 200
