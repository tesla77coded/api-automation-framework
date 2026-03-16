import pytest
import requests
import os
from utils.config_reader import get_config


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests"
    )


@pytest.fixture()
def set_env(request):
    env = request.config.getoption("--env")
    os.environ["TEST-ENV"] = env


@pytest.fixture(autouse=True)
def reset_server_state():
    config = get_config()
    requests.post(f"{config['base_url']}/reset")
