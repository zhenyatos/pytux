import pytux.util as util
import pytux.const as const
import pytux.log.log as log

import os
import json

__logger = log.get_logger(__name__)


def __create_default_config(exists_ok=False):
    if os.path.exists(const.PATH_FILE_CONFIG) and not exists_ok:
        try:
            with open(const.PATH_FILE_CONFIG, "r", encoding="utf-8") as file:
                config = json.load(file)
            for key in const.CONFIG_DEFAULT.keys():
                if key not in config:
                    config[key] = const.CONFIG_DEFAULT[key]
            with open(const.PATH_FILE_CONFIG, "w", encoding="utf-8") as file:
                json.dump(config, file, ensure_ascii=False, indent=const.JSON_INDENT)
        except (EnvironmentError, json.decoder.JSONDecodeError) as err:
            __logger.error(log.get_err_tb(err))
            return err
    else:
        config = const.CONFIG_DEFAULT.copy()
        try:
            with open(const.PATH_FILE_CONFIG, "w", encoding="utf-8") as file:
                json.dump(config, file, ensure_ascii=False, indent=const.JSON_INDENT)
        except (EnvironmentError, TypeError) as err:
            __logger.error(log.get_err_tb(err))
            return str(err)


def __set_configs_attribute(key, value):
    try:
        with open(const.PATH_FILE_CONFIG, "r", encoding="utf-8") as file:
            config = json.load(file)
        config[key] = value
        with open(const.PATH_FILE_CONFIG, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=const.JSON_INDENT)
    except (EnvironmentError, json.decoder.JSONDecodeError, KeyError, TypeError) as err:
        __logger.error(log.get_err_tb(err))
        return str(err)


def get_config():
    """
    Is not entry point of particular task.
    Serves to get configuration data for the running application.

    :return: configuration dict.
    """
    try:
        with open(const.PATH_FILE_CONFIG, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except (EnvironmentError, json.decoder.JSONDecodeError) as err:
        # if corrupted => rewrite with defaults
        # util.print_err_msg(log.get_err_tb(err))
        config = const.CONFIG_DEFAULT.copy()
        try:
            with open(const.PATH_FILE_CONFIG, "w", encoding="utf-8") as file:
                json.dump(config, file, ensure_ascii=False, indent=const.JSON_INDENT)
        except (EnvironmentError, TypeError) as err:
            util.print_err_msg(log.get_err_tb(err))
            return
        return config


def add(argv):
    """
    Entry point of `pytux config add` task.
    Sets specified pytux config parameter.

    :param argv: unused.
    :return: None on success, str with error description on error.
    """
    err = __create_default_config()
    if err:
        return err
    if argv.log:
        err = __set_configs_attribute(const.CONFIG_KEY_LOG_LEVEL, argv.log)
        if err:
            return err
    if argv.yes:
        err = __set_configs_attribute(const.CONFIG_KEY_QUIZ_YES, argv.yes)
        if err:
            return err
    if argv.no:
        err = __set_configs_attribute(const.CONFIG_KEY_QUIZ_NO, argv.no)
        if err:
            return err
    if argv.score:
        err = __set_configs_attribute(const.CONFIG_KEY_QUIZ_SCORE, argv.score)
        if err:
            return err


def show(argv):
    """
    Entry point of `pytux config show` task.
    Prints contents of pytux config file.

    :param argv: unused.
    :return: None on success, str with error description on error.
    """
    err = __create_default_config()
    if err:
        return err
    try:
        with open(const.PATH_FILE_CONFIG, "r", encoding="utf-8") as file:
            print(file.read())
    except EnvironmentError as err:
        __logger.error(log.get_err_tb(err))
        return str(err)


def clear(argv):
    """
    Entry point of `pytux config clear` task.
    Clears pytux config file to default state.

    :param argv: unused.
    :return: None on success, str with error description on error.
    """
    return __create_default_config(exists_ok=True)
