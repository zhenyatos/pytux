import pytux.log as log
import pytux.util as util
import pytux.const as const


def __show(argv):
    try:
        with open(const.PATH_FILE_LOG, "r") as file:
            print(file.read())
    except EnvironmentError as err:
        return log.get_err_tb(err)
    return None


def __clear(argv):
    try:
        with open(const.PATH_FILE_LOG, "w"): pass
    except EnvironmentError as err:
        return log.get_err_tb(err)
    return None


__tasks_log = {
    "show": __show,
    "clear": __clear
}


def main(argv):
    try:
        msg = __tasks_log[argv.task](argv)
        if msg is not None:
            util.print_err_msg(msg)
            return -1
    except Exception as err:
        util.print_err_msg(log.get_err_tb(err))
        return -1
    return 0
