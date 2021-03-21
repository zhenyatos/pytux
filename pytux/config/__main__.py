import pytux.util as util
import pytux.const as const
import pytux.log.log as log
import pytux.config.core as core


__logger = log.get_logger(__name__)
__tasks_config = {
    "add": core.add,
    "show": core.show,
    "clear": core.clear,
}


def main(argv):
    """
    Entry point of `pytux config` command.

    :param argv: command line arguments passed to tasks.
    :return: 0 on success, -1 on error.
    """
    try:
        msg = __tasks_config[argv.task](argv)
        if msg is not None:
            util.print_err_msg(msg)
            return -1
    except Exception as err:
        __logger.critical(log.get_info(err))
        util.print_err_msg("an unhandled exception has been caught")
        return -1
    return 0
