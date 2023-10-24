# Connect NAS

App to maintain connection to NAS servers

## Quickstart

1. Clone `git clone git@github.com:jakelime/connect-nas.git`

1. Go to root dir `cd connect-nas`

1. Create `.env` to load NAS server ip-addresses and local mount point. For example:

   ```bash
   # Example .env file (//connect-nas/.env)
   NAS_ADDR01_SMB="smb://10.10.10.10/data"
   NAS_ADDR01_LOCAL="/Volumes/data"
   NAS_ADDR02_SMB="smb://10.10.10.10/photos"
   NAS_ADDR02_LOCAL="/Volumes/photos"
   ```

1. Run from entry point `cli.py`

   ```bash
   python cli.py

   INFO    : logger initialized - cnns.log
   INFO    : logfile_path='/var/folders/qy/_bfxymvj5zb_5c5z881z14q40000gn/T/tmpgb1x_dv7/cnns.log'
   INFO    : already mounted - local_path=PosixPath('/Volumes/xx')
   file photo:
   INFO    : mounted successfully - local_path=PosixPath('/Volumes/yy')
   ```

## Setup

Tested with

- `python` == `3.11.5`
- `pip install -r requirements.txt`

### Pyinstaller

WARNING:

- `.env` will be packaged and distributed together in the `.app` distribution file

```bash
pyinstaller cli.py --noconsole --name connectNas --add-data '.env:.' --icon icon.icns
```
