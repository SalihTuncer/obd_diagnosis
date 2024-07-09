import unittest
from typing import Callable

import obd

from application.data_models.command import OBDCommandsModel, OBDCommandModel


class TestOBDCommandsModel(unittest.TestCase):
    def setUp(self):
        self.cmds = OBDCommandsModel(
            **{
                'mode_1': [
                    {
                        "name": "INTAKE_PRESSURE",
                        "desc": "Intake Manifold Pressure",
                        "command": "010B",
                        "bytes": 3,
                        "ecu": 2,
                        "fast": True,
                        "header": "7E0"
                    }
                ]
            }
        )

        self.cmd: OBDCommandModel = self.cmds.mode_1[0].model_copy()

    def test_commands_model(self):
        self.assertIsNotNone(self.cmds.mode_1)
        # All elements of cmds.mode_0 are of type OBDCommandModel
        self.assertTrue(all(isinstance(cmd, OBDCommandModel) for cmd in self.cmds.mode_1))
        # All other modes are None
        self.assertTrue(all(mode is None for mode in [self.cmds.mode_0, self.cmds.mode_2, self.cmds.mode_3]))

    def test_to_obd_command(self):
        obd_cmd = self.cmd.to_obd_command()

        self.assertIsInstance(obd_cmd, obd.OBDCommand)
        self.assertEquals(self.cmd, obd_cmd)
        self.assertIsNotNone(obd_cmd.decode)

    def test_internal_equals_method(self):
        obd_cmd: obd.OBDCommand = self.cmd.to_obd_command()

        self.assertIsInstance(obd_cmd, obd.OBDCommand)
        self.assertIsInstance(self.cmd, OBDCommandModel)
        self.assertEquals(self.cmd, obd_cmd)

    def test_from_obd_command(self):
        obd_cmd: obd.OBDCommand = self.cmd.to_obd_command()

        cmd = OBDCommandModel.from_obd_command(obd_cmd)

        self.assertIsInstance(obd_cmd, obd.OBDCommand)
        self.assertIsInstance(cmd, OBDCommandModel)
        self.assertEquals(self.cmd, obd_cmd)

    def test_to_serializable(self):
        serialized_cmd = self.cmd.to_serializable()

        for attr in ['name', 'desc', 'command', 'ecu', 'fast', 'header']:
            if attr == 'command' or attr == 'header':
                self.assertEquals(serialized_cmd[attr], getattr(self.cmd, attr).decode('utf-8'))
                continue

            self.assertEquals(serialized_cmd[attr], getattr(self.cmd, attr))

    def test_assign_decoder(self):
        self.cmd.decode = None
        self.cmd.assign_decoder()

        self.assertIsInstance(self.cmd.decode, Callable)
