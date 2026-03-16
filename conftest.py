import pytest
import os


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests"
    )


@pytest.fixture()
def set_env(request):
    env = request.config.getoption("--env")
    os.environ["TEST-ENV"] = env
