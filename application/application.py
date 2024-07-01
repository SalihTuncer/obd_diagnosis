from application.command_helper import CommandHelper
from application.query_manager import QueryManager
from data_models.settings import Settings


class Application:

    def __init__(self, settings: Settings):
        self.settings = settings

        self.command_helper = CommandHelper(
            settings=settings.commandos
        )

        if settings.connection.connected:
            self.query_manager = QueryManager(
                delay_cmds=settings.connection.interval
            )

    def run(self):
        """
            Runs the application.
        """
        if not self.settings.connection.connected:
            return

        supported_mode_1_cmds = self.command_helper.get_commands_from_file(
            file=self.settings.commandos.supportedCommandos
        )['mode_1']

        if self.settings.connection.type == 'sync':
            self.query_manager.sync_queries(
                cmds=supported_mode_1_cmds
            )

        elif self.settings.connection.type == 'async':
            self.query_manager.async_queries(
                cmds=supported_mode_1_cmds
            )

    def get_sync_connection(self):
        """
            Returns a synchronous connection.
        """
        return self.query_manager.sync_conn
