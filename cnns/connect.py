import os
from pathlib import Path

try:
    from config import get_network_map
    from utils import init_logger
except ImportError:
    from cnns.config import get_network_map
    from cnns.utils import init_logger

APP_NAME = "cnns"
log = init_logger(APP_NAME)


def main():
    nwm = get_network_map()
    for local_addr, network_addr in nwm.items():
        local_path = Path(local_addr)
        if local_path.is_dir():
            log.info(f"already mounted - {local_path=}")
        else:
            command = f"osascript -e 'mount volume \"{network_addr}\"'"
            returncode = os.system(command)
            if returncode == 0 and local_path.is_dir():
                log.info(f"mounted successfully - {local_path=}")
            else:
                log.error(
                    f"mounting ({network_addr} failed. {returncode=}, \n{command=})"
                )


if __name__ == "__main__":
    main()
