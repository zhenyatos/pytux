import pytux.const as const

import os
import sys
import logging


def setup_logging(log_level):
    logging.basicConfig(stream=const.LOG_FILE,
                        format=const.LOG_FORMAT,
                        datefmt=const.LOG_FORMAT_ASCTIME,
                        level=const.LOG_SEVERITY_LEVELS[log_level])


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.addHandler(logging.NullHandler())
    return logger


def get_err_tb(err):
    info = sys.exc_info()
    name = info[0].__name__
    tb_frame = info[2]
    while tb_frame.tb_next is not None:
        tb_frame = tb_frame.tb_next
    file = os.path.basename(tb_frame.tb_frame.f_code.co_filename)
    line = tb_frame.tb_lineno
    return "%s at [%s:%d] %s" % (name, file, line, str(err))
