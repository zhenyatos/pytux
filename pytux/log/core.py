import pytux.const as const
import pytux.log.log as log


def show(argv):
    """
    Entry point of `pytux log show` task.
    Prints contents of log file.

    :param argv: unused.
    :return: None on success, str with error description on error.
    """
    try:
        with open(const.PATH_FILE_LOG, "r") as file:
            print(file.read())
    except EnvironmentError as err:
        return log.get_err_tb(err)
    return None


def clear(argv):
    """
    Entry point of `pytux log clear` task.
    Prints contents of log file.

    :param argv: unused.
    :return: None on success, str with error description on error.
    """
    try:
        with open(const.PATH_FILE_LOG, "w"): pass
    except EnvironmentError as err:
        return log.get_err_tb(err)
    return None
