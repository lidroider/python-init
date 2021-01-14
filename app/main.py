import time

from loguru import logger
from logger_wrapper import config, create_log

config()

if __name__ == "__main__":
    with logger.catch(message="UNCATCH EXCEPTION in main"):
        logger.info("Hello world")

        while True:
            logger.info("Hello world")
            logger.error("Hello world")

            time.sleep(2)
