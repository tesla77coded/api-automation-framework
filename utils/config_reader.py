import yaml
import os


def get_env():
    return os.getenv("TEST_ENV", "dev")


def get_config():
    env = get_env()

    with open("config/env.yaml") as f:
        data = yaml.safe_load(f)

    return data[env]
