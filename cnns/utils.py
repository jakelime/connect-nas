import logging
import tempfile
from pathlib import Path

APP_NAME = "cnns"


def init_logger(
    name: str = "", logfile_in_temp_dir: bool = True, cleanup_logfile: bool = True
) -> logging.Logger:
    """
    initialize an logger (console output and file output)
    returns existing logger if already initialized before

    :param name: name of the logger. this name must be consistent throughout the app, defaults to ""
    :type name: str, optional
    :param logfile_in_temp_dir: creates the log file in the tmpdir = tempfile.TemporaryDirectory(), defaults to True
    :type logfile_in_temp_dir: bool, optional
    :param cleanup_logfile: tempfile.TemporaryDirectory(delete=True), defaults to True
    :type cleanup_logfile: bool, optional
    :return: _description_
    :rtype: logging.Logger
    """

    logger_name = name if name else __name__
    logger = logging.getLogger(logger_name)
    if logger.hasHandlers():
        return logger
    c_handler = logging.StreamHandler()
    c_format = logging.Formatter("%(levelname)-8s: %(message)s")
    c_handler.setFormatter(c_format)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger_filename = (
        f"{logger_name}.log" if logger_name != "__main__" else f"{name}.log"
    )
    if logfile_in_temp_dir:
        global tmpdir
        tmpdir = tempfile.TemporaryDirectory()
        f_handler = logging.FileHandler(Path(tmpdir.name) / logger_filename)
    else:
        f_handler = logging.FileHandler(logger_filename)
    f_format = logging.Formatter(
        "[%(asctime)s]%(levelname)-8s: %(message)s", "%d-%b-%y %H:%M"
    )
    f_handler.setFormatter(f_format)
    f_handler.setLevel(logging.INFO)
    logger.addHandler(f_handler)
    logger.setLevel(logging.INFO)
    logger.info(f"logger initialized - {logger_filename}")
    try:
        logfile_path = logger.handlers[-1].baseFilename  # type: ignore
        logger.info(f"{logfile_path=}")
    except Exception as e:
        logger.debug(f"failed to acquire logger path, {e=}")
    return logger
