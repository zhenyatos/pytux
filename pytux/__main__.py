import pytux.log as log
import pytux.util as util
import pytux.args as args
import pytux.const as const

from pytux.build.__main__ import main as command_build
from pytux.log.__main__ import main as command_log

import os
import sys

__logger = None
__commands = {
    "build": command_build,
    "log": command_log
}


def main():
    if os.name not in const.PATH_DIRS_LOG.keys():
        util.print_err_msg("unable to run on %s platform" % os.name)
        return -1

    working_dirs = [
        const.PATH_DIR_HOME,
        const.PATH_DIRS_LOG[os.name]
    ]
    util.make_dirs(working_dirs)
    if len(working_dirs) != 0:
        util.print_err_msg("unable to make working dirs")
        return -1

    try:
        const.LOG_FILE = open(const.PATH_FILE_LOG, "a")
    except EnvironmentError as err:
        util.print_err_msg(log.get_err_tb(err))
        return -1

    argv = args.parse_args()
    if argv.command == "log":
        const.LOG_FILE.close()
        const.LOG_FILE = sys.stdout
    if argv.command != "log":
        log.setup_logging(argv.log_level)

    global __logger
    __logger = log.get_logger(__name__)
    __logger.info("starting...")
    __logger.info("executing <%s> command" % argv.command)
    code = __commands[argv.command](argv)
    __logger.info("exiting...")
    const.LOG_FILE.close()
    return code


if __name__ == "__main__":
    exit(main())
