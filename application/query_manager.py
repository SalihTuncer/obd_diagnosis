import time

import obd


class QueryManager:
    def __init__(self, delay_cmds=2):

        self.connect_sync()
        self.connect_async(delay_cmds=delay_cmds)

    def __del__(self):
        if self.sync_conn.is_connected():
            self.sync_conn.close()

        if self.async_conn.is_connected():
            self.async_conn.close()

    def connect_sync(self) -> None:
        """
            Connects to the OBD interface synchronously.

        """
        obd.logger.info('Connecting to the OBD interface synchronously.')

        self.sync_conn = obd.OBD()

    def connect_async(self, delay_cmds=2) -> None:
        """
            Connects to the OBD interface asynchronously.

            :param delay_cmds: The delay between commands
        """
        obd.logger.info('Connecting to the OBD interface asynchronously.')

        self.async_conn = obd.Async(delay_cmds=delay_cmds)

    def sync_queries(self, cmds: list[obd.OBDCommand]) -> None:
        """
            Queries the given connection for all available commands.

            :param cmds: The commands to query
            :return: None
        """
        if not self.is_sync_connected():
            self.connect_sync()

        for cmd in cmds:

            resp = self.sync_conn.query(cmd.command)  # send the command, and parse the resp

            if resp.is_null():
                obd.logger.info(f'{cmd} is not supported.')
                continue

            obd.logger.info(f'{cmd.name}: {resp.value}')

    def async_queries(self, cmds: list[obd.OBDCommand], duration=60) -> None:
        """
            Queries the given connection for all available commands asynchronously.

            :param cmds: The commands to query
            :param duration: The duration to query the commands for
            :return: None
        """
        if not self.is_async_connected():
            self.connect_async()

        cmd: obd.OBDCommand
        for cmd in cmds:
            self.async_conn.watch(cmd.command, callback=self.cmd_to_cli)

        self.async_conn.start()

        time.sleep(duration)

        self.async_conn.stop()

    def cmd_to_cli(self, resp: obd.OBDResponse) -> None:
        """
            A callback function that prints the given OBDResponse.

            :param resp: The OBDResponse to print
            :return: None
        """
        obd.logger.info(f'{resp.command}: {resp.value}')

    def is_sync_connected(self) -> bool:
        """
            Returns whether the synchronous connection is connected.

            :return: Whether the synchronous connection is connected
        """
        return self.sync_conn.is_connected()

    def is_async_connected(self) -> bool:
        """
            Returns whether the asynchronous connection is connected.

            :return: Whether the asynchronous connection is connected
        """
        return self.async_conn.is_connected()
