import json

import obd

from application.command_helper import CommandHelper
from application.query_manager import QueryManager
from data_models.settings import LogSettings, Settings


def load_settings(file: str) -> Settings:
    """
        Loads the settings from the given file.

        :param file: The file to load the settings from
        :return: The settings loaded from the file
    """
    with open(file, 'r') as f:
        settings_json = json.load(f)

        return Settings(**settings_json)


def configure_logger(log_settings: LogSettings):
    """
        Configures the logger to print all debug information.
    """
    obd.logger.setLevel(log_settings.logLevel)  # enables all debug information

    # logs should be appended to files
    obd.logger.addHandler(obd.logging.FileHandler(log_settings.logFile, mode='a', encoding='utf-8'))


# load the settings
settings = load_settings(
    'resource/settings.json'
)

# configure the logger
configure_logger(
    log_settings=settings.logging
)

command_helper = CommandHelper(
    settings=settings.commandos
)

query_manager = QueryManager(
    delay_cmds=settings.connection.interval
)


def get_configuration():
    return settings


def get_command_helper():
    return command_helper


def get_query_manager():
    return query_manager
