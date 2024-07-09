import unittest

from application.data_models.settings import Settings


class TestSettings(unittest.TestCase):

    def setUp(self):
        self.settings = Settings(
            **{
                "logging": {
                    "logLevel": "DEBUG",
                    "logFile": "output/logs/obd.log"
                },
                "commandos": {
                    "allCommandos": "resource/commands/all.json",
                    "supportedCommandos": "output/commands/megane_3.json"
                },
                "connection": {
                    "type": "sync",
                    "connected": True,
                    "interval": 0.1
                }
            }
        )

    def test_to_serializable(self):
        serialized_settings = self.settings.to_serializable()

        for model in ['logging', 'commandos', 'connection']:
            self.assertIn(model, serialized_settings)

    def test_logging_to_serialize(self):
        serialized_logging = self.settings.logging.to_serializable()

        for attr in ['logLevel', 'logFile']:
            self.assertIn(attr, serialized_logging)

    def test_commandos_to_serialize(self):
        serialized_commandos = self.settings.commandos.to_serializable()

        for attr in ['allCommandos', 'supportedCommandos']:
            self.assertIn(attr, serialized_commandos)

    def test_connection_to_serialize(self):
        serialized_connection = self.settings.connection.to_serializable()

        for attr in ['type', 'connected', 'interval']:
            self.assertIn(attr, serialized_connection)
