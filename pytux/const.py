import os
import logging
from collections import OrderedDict

# JSON
JSON_EXT = ".json"
JSON_INDENT = 4

# PATHS
PATH_DIR_HOME = os.path.join(os.path.expanduser("~"), ".pytux")
PATH_DIRS_LOG = {
    "nt": PATH_DIR_HOME,
    "posix": "/var/log/pytux"
}
PATH_FILE_CONFIG = os.path.join(PATH_DIR_HOME, "config" + JSON_EXT)
PATH_FILE_LOG = os.path.join(PATH_DIRS_LOG[os.name], "pytux.log")

# CONFIG
CONFIG_KEY_LOG_LEVEL = "log level"
CONFIG_KEY_QUIZ_YES = "quiz yes"
CONFIG_KEY_QUIZ_NO = "quiz no"
CONFIG_KEY_QUIZ_SCORE = "quiz score"
CONFIG_DEFAULT = {
	CONFIG_KEY_LOG_LEVEL: "DEBUG",
	CONFIG_KEY_QUIZ_YES: "Yes, you are right!",
	CONFIG_KEY_QUIZ_NO: "Nope, wrong answer...",
	CONFIG_KEY_QUIZ_SCORE: "%s test: you have obtained [score_%d] out of %d points.",
}

# LOG
LOG_FILE = None
LOG_FORMAT = "[%(asctime)s] %(levelname)-8s [%(name)-20s:%(lineno)3d] %(message)s"
LOG_FORMAT_ASCTIME = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = "DEBUG"
LOG_SEVERITY_LEVELS = OrderedDict([
    ("DEBUG", logging.DEBUG),
    ("INFO", logging.INFO),
    ("WARNING", logging.WARNING),
    ("ERROR", logging.ERROR),
    ("CRITICAL", logging.CRITICAL)
])
