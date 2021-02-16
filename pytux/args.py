import pytux.const as const

import argparse


class __CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
    pass


def __add_args_build(subparsers_base):
    parser = subparsers_base.add_parser("build",
                                        formatter_class=__CustomFormatter,
                                        help="works with building renpy project.\n")


def __add_args_log(subparsers_base):
    parser = subparsers_base.add_parser("log",
                                        formatter_class=__CustomFormatter,
                                        help="works with logs.\n")

    subparsers = parser.add_subparsers(title="available tasks",
                                       metavar="task [-h] [options ...]",
                                       dest="task")
    subparsers.required = True

    # SHOW
    parser_show = subparsers.add_parser("show",
                                        formatter_class=__CustomFormatter,
                                        help="prints contents of log file.\n")

    # CLEAR
    parser_clear = subparsers.add_parser("clear",
                                         formatter_class=__CustomFormatter,
                                         help="clears contents of log file.\n")


def parse_args():
    """
    Parses command line arguments.

    :return: Namespace object of argument.
    """
    parser = argparse.ArgumentParser(prog="pytux",
                                     formatter_class=__CustomFormatter)

    subparsers = parser.add_subparsers(title="available commands",
                                       metavar="command [-h] task [options ...]",
                                       dest="command")

    subparsers.required = True

    __add_args_build(subparsers)
    __add_args_log(subparsers)

    parser.add_argument("-l", "--log-level", metavar="",
                        action="store",
                        dest="log_level",
                        type=str.upper,
                        default=const.LOG_LEVEL,
                        choices=const.LOG_SEVERITY_LEVELS.keys(),
                        help="specify level of logging severity.\n"
                             " (сhoices: %(choices)s)\n")

    return parser.parse_args()
