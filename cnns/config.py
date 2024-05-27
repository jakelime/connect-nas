import os
import sys
from pathlib import Path

# import dotenv
import tomllib

try:
    from utils import init_logger
except ImportError:
    from cnns.utils import init_logger

APP_NAME = "cnns"
extDataDir = os.getcwd()
if getattr(sys, "frozen", False):
    extDataDir = sys._MEIPASS
# config_filepath = Path(extDataDir) / APP_NAME / "bundles" / "config.toml"
config_filepath = Path(extDataDir) / "config.toml"


log = init_logger(APP_NAME)


def get_network_map():
    with open(config_filepath, "rb") as f:
        data = tomllib.load(f)
    if not data:
        raise EnvironmentError(f"missing {config_filepath=}")
    try:
        network_maps = data["network_maps"]
    except KeyError as e:
        log.error(f"missing key 'network_maps' in {config_filepath=}")
        raise e
    return network_maps


def main():
    log.info(get_network_map())


if __name__ == "__main__":
    main()
