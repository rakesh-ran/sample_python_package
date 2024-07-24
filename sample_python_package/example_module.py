import logging 

logger = logging.getLogger(__name__)
def hello_world():
    logger.info("inside hello world function")
    return "Hello, world!"
