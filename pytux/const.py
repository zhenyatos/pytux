import os
import logging
from collections import OrderedDict

# PATHS
PATH_DIR_HOME = os.path.join(os.path.expanduser("~"), ".pytux")
PATH_DIRS_LOG = {
    "nt": PATH_DIR_HOME,
    "posix": "/var/log/pytux"
}
PATH_FILE_LOG = os.path.join(PATH_DIRS_LOG[os.name], "pytux.log")

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
