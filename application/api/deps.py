import json

import obd

from application.data_models.settings import LogSettings, Settings
from application.utils.command_helper import CommandHelper
from application.utils.query_manager import QueryManager

SETTINGS_PATH = 'resource/settings.json'


def load_settings(path: str = SETTINGS_PATH) -> Settings:
    """
        Loads the settings from the given file.

        :param path: The path to the settings file
        :return: The settings loaded from the file
    """
    with open(path, 'r') as f:
        settings_json = json.load(f)

        return Settings(**settings_json)


def update_settings(new_settings: Settings, path: str = SETTINGS_PATH):
    """
        Updates the settings in the file.

        :param path: The path to the settings file
        :param new_settings: The settings to update
    """
    with open(path, 'w') as f:
        json.dump(new_settings.to_serializable(), f, indent=4)

    global settings
    settings = new_settings


def configure_logger(log_settings: LogSettings):
    """
        Configures the logger to print all debug information.
    """
    obd.logger.setLevel(log_settings.logLevel)  # enables all debug information

    # logs should be appended to files
    obd.logger.addHandler(obd.logging.FileHandler(log_settings.logFile, mode='a', encoding='utf-8'))


# load the settings
settings = load_settings()

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
