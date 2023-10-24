# Connect NAS

App to maintain connection to NAS servers

## Quickstart

```bash
git clone git@github.com:jakelime/connect-nas.git
cd connect-nas
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

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

[!NOTE]
`.env` will be packaged and distributed together in `.app`

```bash
pyinstaller cli.py --noconsole --name connectNas --add-data '.env:.'
```
