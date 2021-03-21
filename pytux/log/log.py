import pytux.const as const

import os
import sys
import logging


def setup_logging(log_level):
    """
    Sets up basic configs for logging module (via logging.basicConfig).

    :param log_level: level of logging.
    :return: None.
    """
    logging.basicConfig(stream=const.LOG_FILE,
                        format=const.LOG_FORMAT,
                        datefmt=const.LOG_FORMAT_ASCTIME,
                        level=const.LOG_SEVERITY_LEVELS[log_level])


def get_logger(name):
    """
    Gets logger for specified name.

    :param name: logger name.
    :return: logger.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.addHandler(logging.NullHandler())
    return logger


def get_err_tb(err):
    """
    Makes system call to gather details about thrown
    exception's traceback (sys.exc_info()).

    :param err: caught exception.
    :return: str representation of error type,
    file and line it was thrown from, error text itself.
    """
    info = sys.exc_info()
    name = info[0].__name__
    tb_frame = info[2]
    while tb_frame.tb_next is not None:
        tb_frame = tb_frame.tb_next
    file = os.path.basename(tb_frame.tb_frame.f_code.co_filename)
    line = tb_frame.tb_lineno
    return "%s at [%s:%d] %s" % (name, file, line, str(err))


def stop_logging():
    logging.shutdown()
