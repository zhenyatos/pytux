import pytux.util as util
import pytux.log.log as log
import pytux.log.core as core


__tasks_log = {
    "show": core.show,
    "clear": core.clear
}


def main(argv):
    """
    Entry point of `pytux log` command.

    :param argv: command line arguments passed to tasks.
    :return: 0 on success, -1 on error.
    """
    try:
        msg = __tasks_log[argv.task](argv)
        if msg is not None:
            util.print_err_msg(msg)
            return -1
    except Exception as err:
        util.print_err_msg(log.get_err_tb(err))
        return -1
    return 0
