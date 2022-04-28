from sys import stdout

from loguru import logger


def init(app):
    # removing default handler
    logger.remove()

    logger.info("starting logger extension")

    level = "INFO" if app.env == "production" else "TRACE"
    sink = "app.log" if app.env == "production" else stdout

    # create a new handler
    logger.add(sink=sink, level=level)
