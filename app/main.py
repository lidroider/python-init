from loguru import logger
from logger_wrapper import config, create_log

config()

if __name__ == "__main__":
    log = create_log("main")

    log.info("Hello world")
    logger.info("This is loguru log")
    log.info('Done')
