import json

import obd

from data_models.settings import CommandosSettings


class CommandHelper:
    def __init__(self, settings: CommandosSettings):
        self.settings = settings

    def get_commands_from_file(self, file: str) -> dict[str, list[obd.OBDCommand]]:
        """
            Loads the commands from the given file.

            :param file: The file to load the commands from
            :return: The commands loaded from the file
        """
        with open(file, 'r') as f:
            cmds_json = json.load(f)

            cmds_result = {}

            for mode, cmds in cmds_json.items():

                cmds_result[mode] = []

                for cmd in cmds:
                    cmds_result[mode].append(
                        obd.OBDCommand(
                            name=cmd['name'],
                            desc=cmd['desc'],
                            command=bytes(cmd['command'], 'utf-8'),
                            _bytes=cmd['bytes'],
                            decoder=lambda x: x,
                            ecu=cmd['ecu'],
                            fast=cmd['fast'],
                            header=bytes(cmd['header'], 'utf-8')
                        )
                    )

            return cmds_result

    def save_all_commands(self) -> None:
        """
            Saves all the commands to a json file.
        :return: None
        """

        # make a copy of a list
        modes = list(obd.commands.modes)

        cmds = {}

        for idx, mode in enumerate(modes):

            mode_cmds = []

            for cmd in mode:

                if not cmd:
                    continue

                cmd.header = cmd.header.decode('utf-8')
                cmd.command = cmd.command.decode('utf-8')
                del cmd.decode

                mode_cmds.append(cmd.__dict__)

            cmds[f'mode_{idx}'] = mode_cmds

        # list to json file
        with open(self.settings.allCommandos, 'w') as f:
            json.dump(cmds, f, indent=4)

    def save_all_supported_commands(self, connection: obd.OBD) -> None:
        """
            Saves all the commands to a json file.
        :param connection: The connection to get the supported commands from
        :return: None
        """

        # make a copy of a list
        supported_cmds: list[obd.OBDCommand] = connection.supported_commands

        modes = obd.commands.modes

        cmds = {}

        for idx, mode in enumerate(modes):

            mode_cmds = []

            supported_cmd: obd.OBDCommand
            for supported_cmd in supported_cmds:

                if supported_cmd in mode:
                    supported_cmd.header = supported_cmd.header.decode('utf-8')
                    supported_cmd.command = supported_cmd.command.decode('utf-8')
                    del supported_cmd.decode

                    mode_cmds.append(supported_cmd.__dict__)

            cmds[f'mode_{idx}'] = mode_cmds

        # list to json file
        with open(self.settings.supportedCommandos, 'w') as f:
            json.dump(cmds, f, indent=4)
