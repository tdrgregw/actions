"""Module providing environment variables."""
import os

import logging
import logging.handlers

def init_logging():
    """  Docstring """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.handlers.RotatingFileHandler(
        "status.log",
        maxBytes=1024 * 1024,
        backupCount=1,
        encoding="utf8",
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    return logger

def check_tokens():
    """  Docstring """
    try:
        _snake_case = os.environ["SOME_SECRET"]
    except KeyError:
        _snake_case = "Token not available!"
    return _snake_case