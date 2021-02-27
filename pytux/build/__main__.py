import pytux.log as log
from pytux.build.semen import parse
from pytux.build.quiz import QuizError
from pytux.build.lexa import Lexa
from os import path

__logger = log.get_logger(__name__)


def main(argv):
    """
    Entry point of `pytux build` command.

    :param argv: command line arguments passed to tasks.
    :return: 0 on success, -1 on error.
    """
    __logger.debug("test log debug")
    __logger.info("test log info")
    __logger.warning("test log warning")
    __logger.error("test log error")
    __logger.critical("test log critical")

    try:
        raise ValueError("test exception")
    except ValueError as err:
        __logger.error(log.get_err_tb(err))

    if argv.file is not None:
        source_file_name = argv.file.name
        result_file_name = path.splitext(source_file_name)[0] + ".rpy"
        try:
            result = parse(argv.file)
            with open(result_file_name, "w") as result_file:
                result_file.write(result)
        except QuizError as err:
            print(f"Quiz error in {source_file_name}, check log via [pytux log show] for details")
            __logger.error(err)

    return 0
