from clients.base_client import BaseClient


class ProductClient(BaseClient):
    def get_products(self):
        return self.request("GET", "/products")
