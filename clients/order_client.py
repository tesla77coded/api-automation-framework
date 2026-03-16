from clients.base_client import BaseClient


class OrderClient(BaseClient):
    def create_order(self, items):
        payload = {"items": items}
        return self.request("POST", "/orders", json=payload)

    def pay_order(self, order_id):
        return self.request("POST", f"/pay/{order_id}")
