import os
import sys
from cnns.utils import init_logger
import dotenv

extDataDir = os.getcwd()
if getattr(sys, "frozen", False):
    extDataDir = sys._MEIPASS
dotenv.load_dotenv(dotenv_path=os.path.join(extDataDir, ".env"))

APP_NAME = "cnns"

log = init_logger(APP_NAME)

kv_list = [
    ("NAS_ADDR01_SMB", "NAS_ADDR01_LOCAL"),
    ("NAS_ADDR02_SMB", "NAS_ADDR02_LOCAL"),
]

paths_db = {}
# Example .env file
# NAS_ADDR01_SMB="smb://10.10.10.10/data"
# NAS_ADDR01_LOCAL="/Volumes/data"
# NAS_ADDR02_SMB="smb://10.10.10.10/photos"
# NAS_ADDR02_LOCAL="/Volumes/photos"

for key, value in kv_list:
    k = os.getenv(key, None)
    if not k:
        raise EnvironmentError(f"missing {key=}")
    v = os.getenv(value, None)
    if not v:
        raise EnvironmentError(f"missing {value=}")
    paths_db[k] = v
