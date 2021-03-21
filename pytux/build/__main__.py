import pytux.log.log as log
import pytux.util as util
from pytux.build.semen import parse
from os import path

__logger = log.get_logger(__name__)


def main(argv):
    """
    Entry point of `pytux build` command.

    :param argv: command line arguments passed to tasks.
    :return: 0 on success, -1 on error.
    """
    if argv.file is not None:
        source_file_name = argv.file.name
        result_file_name = path.splitext(source_file_name)[0] + ".rpy"
        try:
            result = parse(argv.file)
            with open(result_file_name, "w") as result_file:
                result_file.write(result)
            print(f"Pytux successfully translated {source_file_name} to {result_file_name}")
        except Exception as err:
            __logger.error(log.get_err_tb(err))
            util.print_err_msg(err)
            return -1

    return 0
