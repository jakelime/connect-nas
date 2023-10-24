import os
from pathlib import Path
from cnns.config import paths_db
from cnns.utils import init_logger

APP_NAME = "cnns"
log = init_logger(APP_NAME)


def main():
    for smb_addr, local_addr in paths_db.items():
        local_path = Path(local_addr)
        if local_addr.is_dir():
            log.info(f"already mounted - {local_path=}")
        else:
            os.system(f"osascript -e 'mount volume \"{smb_addr}\"'")
            if local_addr.is_dir():
                log.info(f"mounted successfully - {local_path=}")
            else:
                log.info(f"mounting failed: '{smb_addr}'")
