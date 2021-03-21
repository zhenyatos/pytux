import os
import sys
import pytux.log.log as log

__logger = log.get_logger(__name__)


def confirm(message, yes="yes", no="no"):
    """
    Interacts with user in order to confirm further processing.

    :param message: confirm statement.
    :param yes: 1st option.
    :param no: 2nd option.
    :return: True on 1st option chosen, False on 2nd option chosen.
    """
    while True:
        reply = input("%s [%s/%s]: " % (message, yes, no)).strip().lower()
        if reply == yes:
            return True
        if reply == no:
            return False


def print_err_msg(msg, hint=True):
    """
    Prints error message.

    :param msg: message to print.
    :return: None.
    """
    print("ERROR: %s" % str(msg), file=sys.stderr)
    if hint:
        print("------ try 'pytux log show' for details", file=sys.stderr)


def make_dirs(dir_paths):
    """
    Creates specified directories in file system.

    :param dir_paths: list of directories' paths to create.
    :return: None.
    """
    for dir_path in dir_paths[:]:
        try:
            os.makedirs(dir_path, exist_ok=True)
            if os.name == "posix":
                os.chown(dir_path, os.getuid(), gid=-1)
            if not os.access(dir_path, os.R_OK | os.W_OK):
                raise PermissionError("no permissions to dir: %s" % dir_path)
        except PermissionError as err:
            __logger.error(log.get_err_tb(err))
            continue
        except (ValueError, TypeError, EnvironmentError) as err:
            __logger.error(log.get_err_tb(err))
            continue
        dir_paths.remove(dir_path)
