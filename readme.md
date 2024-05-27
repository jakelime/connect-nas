# Connect NAS

App to automatically mount an connection to your Synology NAS or any network drive using `SMB://`

Built for MacOS.

## Quickstart

1. Clone into your local

   ```shell
   git clone git@github.com:jakelime/connect-nas.git
   cd connect-nas
   ```

1. Create the config file

   ```shell
   touch config.toml
   ```

1. Follow this template for the `config.toml`. This is a list
   of `key: value` pairs, and there must be at least 1 pair.

   `key` is local address, in MacOS, it will be mounted as `/Volumes/xxx`

   `value` is network address using the smb protocol.

   ```toml
   [network_maps]
   "/Volumes/data" = "smb://10.10.10.10/home/data"
   "/Volumes/photos" = "smb://10.10.10.10/photos"
   "/Volumes/videos" = "smb://10.10.10.10/photos"
   ```

1. Running from the entry point, `cli.py`

   ```shell
   python cli.py
   ```

## Packaging into an app

```bash
source venv/bin/activate
pyinstaller cli.py --noconsole --name connectNas --add-data 'config.toml:.' --icon icon.icns
```

1. Package to `connectNas.app` using `pyinstaller`

1. Simply double click `connectNas.app` to get get connected to your server, configure `Open at login` or task schedulers

## Environment

Tested with

- Apple Silicon MacOS14.5 Sonoma
- `python` == `3.12.3`
- `pip install -r requirements.txt`
