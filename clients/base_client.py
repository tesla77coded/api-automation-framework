import requests
from utils.config_reader import get_config
from utils.logger import get_logger
import time


class BaseClient:
    def __init__(self) -> None:
        config = get_config()
        self.base_url = config["base_url"]

        self.session = requests.Session()
        self.logger = get_logger()

        self.timeout = 5
        self.retry_count = 2

        self.headers = {"content-type": "application/json"}

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)

        attempt = 0

        while attempt <= self.retry_count:
            try:
                self.logger.info(f"{method} {url}")
                response = self.session.request(method, url, **kwargs)
                self.logger.info(f"Status Code: {response.status_code}")

                return response
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Request failed: {e}")

                attempt += 1
                time.sleep(1)

        raise Exception("Maximum retries exceeded")
