from clients.base_client import BaseClient


class AuthClient(BaseClient):
    def __init__(self) -> None:
        super().__init__()
        self.token = None

    def login(self, email, password):
        payload = {"email": email, "password": password}

        response = self.request("POST", "/login", json=payload)

        if response.status_code == 200:
            self.token = response.json()["access_token"]
            self.headers["Authorization"] = f"Bearer {self.token}"

        return response
