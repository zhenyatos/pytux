import os
import sys
import pytux.log as log

__logger = log.get_logger(__name__)


def confirm(message, yes="yes", no="no"):
    while True:
        reply = input("%s [%s/%s]: " % (message, yes, no)).strip().lower()
        if reply == yes:
            return True
        if reply == no:
            return False


def print_err_msg(msg):
    print("ERROR: %s" % str(msg), file=sys.stderr)
    print("------ try 'pytux log show' for details", file=sys.stderr)


def make_dirs(dir_paths):
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
