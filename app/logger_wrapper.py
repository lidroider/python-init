import os
import sys

from loguru import logger

import const

DEFAULT_FORMAT = "{time:HH:MM:ss.SSS} | {level} | {process} - {thread} | {file} | {function} | {message}"
INFO_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> \
| <level>{level: <8}</level> | <white>{process} - {thread}</white> \
| <cyan>{file}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> \
- <level>{message}</level>"

DEFAULT_PREFIX_PATH = const.DEFAULT_LOG_PATH


def config():
    error_log_path = os.path.join(
        DEFAULT_PREFIX_PATH, "error__{time:YYYY-MM-DD}.log"
    )
    all_log_path = os.path.join(
        DEFAULT_PREFIX_PATH, "all__{time:YYYY-MM-DD}.log"
    )

    error_handler = {
        "sink": error_log_path,
        "level": "ERROR",
        "backtrace": True,
        "diagnose": True,
        "enqueue": True,
        "format": DEFAULT_FORMAT,
        "rotation": "1 days",
        "retention": "1 months",
    }

    all_handler = {
        "sink": all_log_path,
        "level": "TRACE",
        "backtrace": True,
        "diagnose": True,
        "enqueue": True,
        "format": DEFAULT_FORMAT,
        "rotation": "1 days",
        "retention": "1 weeks",
    }

    info_handler = {
        "sink": sys.stderr,
        "level": "INFO",
        "backtrace": True,
        "diagnose": True,
        "enqueue": True,
        "format": INFO_FORMAT,
    }

    config_log = {"handlers": [error_handler, all_handler, info_handler]}
    logger.remove()
    logger.configure(**config_log)


def create_log(
    logname: str,
    level: str = "INFO",
):
    def check_match_logname(record) -> bool:
        if "logname" in record["extra"]:
            return record["extra"]["logname"] == logname

        return False

    new_log_path = os.path.join(
        DEFAULT_PREFIX_PATH, logname, f"{logname}__{{time:YYYY-MM-DD}}.log"
    )

    logger.add(
        sink=new_log_path,
        level=level,
        backtrace=True,
        diagnose=True,
        enqueue=True,
        format=DEFAULT_FORMAT,
        rotation="1 days",
        retention="1 months",
        filter=check_match_logname,
    )
    return logger.bind(logname=logname)
