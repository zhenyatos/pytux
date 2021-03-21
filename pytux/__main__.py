import pytux.util as util
import pytux.args as args
import pytux.const as const
import pytux.log.log as log

from pytux.config.core import get_config

from pytux.config.__main__ import main as command_config
from pytux.build.__main__ import main as command_build
from pytux.log.__main__ import main as command_log

import os
import sys

__logger = None
__commands = {
    "config": command_config,
    "build": command_build,
    "log": command_log
}


def main():
    """
    Entry point of `pytux` program.

    :return: return code of specified command.
    """
    if os.name not in const.PATH_DIRS_LOG.keys():
        util.print_err_msg("unable to run on %s platform" % os.name, False)
        return -1

    working_dirs = [
        const.PATH_DIR_HOME,
        const.PATH_DIRS_LOG[os.name]
    ]
    util.make_dirs(working_dirs)
    if len(working_dirs) != 0:
        util.print_err_msg("unable to make working dirs", False)
        return -1

    try:
        const.LOG_FILE = open(const.PATH_FILE_LOG, "a")
    except EnvironmentError as err:
        util.print_err_msg(log.get_err_tb(err))
        return -1

    argv = args.parse_args()
    argv.config = get_config()
    if argv.config is None:
        util.print_err_msg("unable to get config", False)
        return -1
    if argv.command == "log":
        const.LOG_FILE.close()
        const.LOG_FILE = sys.stdout
    if argv.command != "log":
        log.setup_logging(argv.config[const.CONFIG_KEY_LOG_LEVEL])

    global __logger
    __logger = log.get_logger(__name__)
    __logger.info("starting...")
    __logger.info("executing <%s> command" % argv.command)
    code = __commands[argv.command](argv)
    __logger.info("exiting...")
    log.stop_logging()
    const.LOG_FILE.close()


if __name__ == "__main__":
    exit(main())
