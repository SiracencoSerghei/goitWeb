import logging
import sys

# log_format = (
#     "%(asctime)s [%(levelname)s] %(filename)s %(funcName)15s(%(lineno)d) - %(message)s"
# )
log_format = "{asctime} [{levelname}] {name} {funcName:15}({lineno}) - {message}"
log_formatter = logging.Formatter(log_format, style="{")

file_handler = logging.FileHandler("app.logs")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(log_formatter)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(log_formatter)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
