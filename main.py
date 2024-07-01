import json
import os

import obd

from application.application import Application
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


if __name__ == "__main__":
    # load the settings
    settings = load_settings('resource/settings.json')

    # configure the logger
    configure_logger(log_settings=settings.logging)

    app = Application(settings)

    # Export all commands to a JSON if not already done
    if not os.path.exists(settings.commandos.allCommandos):
        app.command_helper.save_all_commands()

    # Export all supported commands to a JSON if not already done
    if not os.path.exists(settings.commandos.supportedCommandos):
        app.command_helper.save_all_supported_commands(
            connection=app.get_sync_connection()
        )

    app.run()
