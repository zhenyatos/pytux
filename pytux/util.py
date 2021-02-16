import sys


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
