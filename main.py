import json

import obd
import time


def configure_logger(log_level: int | None = obd.logging.DEBUG):
    """
        Configures the logger to print all debug information.
    """
    if log_level:
        obd.logger.setLevel(log_level)  # enables all debug information

    # logs should be written to files too
    obd.logger.addHandler(obd.logging.FileHandler('obd.log'))


def save_all_commands(output_file: str) -> None:
    """
        Saves all the commands to a json file.
    :param output_file: The file to save the commands to
    :return: None
    """

    # make a copy of a list
    modes = list(obd.commands.modes)

    cmds = {}

    mode_ctr = 0

    for mode in modes:

        mode_cmds = []

        for cmd in mode:

            if not cmd:
                continue

            cmd.header = cmd.header.decode('utf-8')
            cmd.command = cmd.command.decode('utf-8')
            del cmd.decode

            mode_cmds.append(cmd.__dict__)

        cmds[f'mode_{mode_ctr}'] = mode_cmds

        mode_ctr += 1

    # list to json file
    with open(output_file, 'w') as f:
        json.dump(cmds, f, indent=4)


def save_all_supported_commands(connection: obd.OBD, output_file: str) -> None:
    """
        Saves all the commands to a json file.
    :param output_file: The file to save the commands to
    :return: None
    """

    # make a copy of a list
    supported_cmds: list[obd.OBDCommand] = connection.supported_commands

    cmds = []

    for cmd in supported_cmds:

        if not cmd:
            continue

        cmd.header = cmd.header.decode('utf-8')
        cmd.command = cmd.command.decode('utf-8')
        del cmd.decode

        cmds.append(cmd.__dict__)

    # list to json file
    with open(output_file, 'w') as f:
        json.dump(cmds, f, indent=4)


def cmd_to_cli(resp: obd.OBDResponse) -> None:
    """
        A callback function that prints the given OBDResponse.

        :param resp: The OBDResponse to print
        :return: None
    """
    print(f'{resp.command}: {resp.value}')


def sync_queries(connection: obd.OBD, cmds: dict[str, obd.OBDCommand]) -> None:
    """
        Queries the given connection for all available commands.

        :param connection: The connection to query
        :return: None
    """
    for naming, cmd in cmds.items():

        resp = connection.query(cmd)  # send the command, and parse the resp

        if resp.is_null():
            print(f'{cmd} is not supported.')
            continue

        print(f'{naming}: {resp.value}')


def async_queries(connection: obd.Async, cmds: dict[str, obd.OBDCommand], duration=60) -> None:
    """
        Queries the given connection for all available commands asynchronously.

        :param connection: The connection to query
        :return: None
    """
    for naming, cmd in cmds.items():
        connection.watch(cmd, callback=cmd_to_cli)

    connection.start()

    time.sleep(duration)

    connection.stop()


mode_1_cmds = {
    'Engine RPM': obd.commands['RPM'],
    'Vehicle Speed': obd.commands['SPEED'],
    'Throttle Position': obd.commands['THROTTLE_POS'],
    'Relative throttle position': obd.commands['RELATIVE_THROTTLE_POS'],
    'Engine Coolant Temperature': obd.commands['COOLANT_TEMP'],
    'Intake Air Temp': obd.commands['INTAKE_TEMP'],
    'Ambient air temperature': obd.commands['AMBIANT_AIR_TEMP'],
    'Engine oil temperature	': obd.commands['OIL_TEMP'],
    'Fuel Type': obd.commands['FUEL_TYPE'],
    'Fuel System Status': obd.commands['FUEL_STATUS'],
    'Engine fuel rate': obd.commands['FUEL_RATE'],
    'Fuel Level Input': obd.commands['FUEL_LEVEL']
}

# mode_2_cmds = {
#     for k, v in obd.commands.mode_1_cmds.items()
# }

# https://python-obd.readthedocs.io/en/latest/Command%20Tables/
relevant_cmds = {
    'Engine RPM': obd.commands.SPEED,
    'Vehicle Speed': obd.commands.SPEED,
    'Throttle Position': obd.commands.THROTTLE_POS,
    'Relative throttle position': obd.commands.RELATIVE_THROTTLE_POS,
    'Engine Coolant Temperature': obd.commands.COOLANT_TEMP,
    'Intake Air Temp': obd.commands.INTAKE_TEMP,
    'Ambient air temperature': obd.commands.AMBIANT_AIR_TEMP,
    'Engine oil temperature	': obd.commands.OIL_TEMP,
    'Fuel Type': obd.commands.FUEL_TYPE,
    'Fuel System Status': obd.commands.FUEL_STATUS,
    'Engine fuel rate': obd.commands.FUEL_RATE,
    'Fuel Level Input': obd.commands.FUEL_LEVEL
}

if __name__ == "__main__":
    configure_logger(log_level=None)

    sync_conn = obd.OBD()

    # save_all_supported_commands(sync_conn, 'supported_cmds.json')

    # resp = sync_conn.query(obd.commands.GET_DTC)  # send the command, and parse the resp

    # print(f'{resp.value}')

    # sync_queries(sync_conn, relevant_cmds)

    async_conn = obd.Async(delay_cmds=2)

    # async_queries(async_conn, mode_1_cmds)
    print()