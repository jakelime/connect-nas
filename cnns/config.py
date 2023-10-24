import os
import dotenv

dotenv.load_dotenv()

paths_db = {}
# Key: smb address
# Value: mounted local address
# e.g. "smb://10.10.1.2/photos": "/Volumes/photos"
# "smb://192.168.50.243/home": "/Volumes/home"
paths_db[os.getenv("NAS_ADDR01_SMB")] = os.getenv("NAS_ADDR01_LOCAL")
