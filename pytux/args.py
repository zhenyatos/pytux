import pytux.const as const

import argparse


class __CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
    pass


def __add_args_config(subparsers_base):
    parser = subparsers_base.add_parser("config",
                                        formatter_class=__CustomFormatter,
                                        help="works with config file.\n")

    subparsers = parser.add_subparsers(title="available tasks",
                                       metavar="task [-h] [options ...]",
                                       dest="task")
    subparsers.required = True

    # ADD
    parser_add = subparsers.add_parser("add",
                                        formatter_class=__CustomFormatter,
                                        help="makes changes to configuration.\n")

    parser_add.add_argument("-l", "--log-level", metavar="", 
                            action="store", 
                            dest="log", 
                            type=str.upper, 
                            default=None, 
                            choices=const.LOG_SEVERITY_LEVELS.keys(),
                            help="specify level of logging severity.\n"
                                 " (сhoices: %(choices)s)\n")

    parser_add.add_argument("-y", "--yes", metavar="", 
                            action="store", 
                            dest="yes", 
                            default=None, 
                            help="specify quiz message to correct answer.\n")

    parser_add.add_argument("-n", "--no", metavar="", 
                            action="store", 
                            dest="no", 
                            default=None, 
                            help="specify quiz message to incorrect answer.\n")

    parser_add.add_argument("-s", "--score", metavar="", 
                            action="store", 
                            dest="score", 
                            default=None, 
                            help="specify quiz result format message.\n")

    # SHOW
    parser_show = subparsers.add_parser("show",
                                        formatter_class=__CustomFormatter,
                                        help="prints current configuration.\n")

    # CLEAR
    parser_clear = subparsers.add_parser("clear",
                                         formatter_class=__CustomFormatter,
                                         help="clears current configuration to default state.\n")

def __add_args_build(subparsers_base):
    parser = subparsers_base.add_parser("build",
                                        formatter_class=__CustomFormatter,
                                        help="works with building renpy project.\n")

    parser.add_argument("-f", "--file", metavar="",
                        type=argparse.FileType("r"),
                        dest="file",
                        default=None)


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

    __add_args_config(subparsers)
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
