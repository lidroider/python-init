import os
import sys
from loguru import logger

DEFAULT_FORMAT = "{time:HH:MM:ss.SSS} | {level} | {process} - {thread} | {file} | {function} | {message}"
TRACE_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> \
| <level>{level: <8}</level> | <white>{process} - {thread}</white> \
| <cyan>{file}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> \
- <level>{message}</level>"

DEFAULT_PREFIX_PATH = "/logs"


def __prefix_daily_log_path():
    return os.path.join(DEFAULT_PREFIX_PATH, "{time:YYYY-MM-DD}")


def config():
    error_log_path = os.path.join(__prefix_daily_log_path(), "error.log")
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

    trace_handler = {
        "sink": sys.stderr,
        "level": "TRACE",
        "backtrace": True,
        "diagnose": True,
        "enqueue": True,
        "format": TRACE_FORMAT,
    }

    config_log = {"handlers": [error_handler, trace_handler]}
    logger.remove()
    logger.configure(**config_log)


def create_log(
    logname: str,
    level: str = "INFO",
):
    def check_match_logname(record) -> bool:
        if "logname" in record["extra"]:
            return record["extra"]["logname"] == logname
        else:
            return False

    new_log_path = os.path.join(__prefix_daily_log_path(), f"{logname}.log")

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
