import os
from pathlib import Path
from cnns.config import paths_db


def main():
    for smb_addr, local_addr in paths_db.items():
        os.system(f"osascript -e 'mount volume \"{smb_addr}\"'")
        local_path = Path(local_addr)
        if local_addr.is_dir():
            print(f"Mounted succesfully: '{local_path}'")
        else:
            print(f"Mounted failed: '{smb_addr}'")
