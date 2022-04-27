from sys import stdout

from loguru import logger


def init(app):
    # removing default handler
    logger.remove()

    logger.info("starting logger extension")

    prod_env = app.env == "production"
    level, sink = "INFO", "app.log" if prod_env else "TRACE", stdout

    # create a new handler
    logger.add(sink=sink, level=level)
