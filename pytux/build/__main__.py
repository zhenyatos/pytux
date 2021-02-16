import pytux.log as log

__logger = log.get_logger(__name__)


def main(argv):
    __logger.debug("test log debug")
    __logger.info("test log info")
    __logger.warning("test log warning")
    __logger.error("test log error")
    __logger.critical("test log critical")

    try:
        raise ValueError("test exception")
    except ValueError as err:
        __logger.error(log.get_err_tb(err))

    return 0
