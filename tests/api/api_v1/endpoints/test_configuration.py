import unittest
from unittest import mock

from fastapi.testclient import TestClient

from application.data_models.settings import Settings
from main import app

CLIENT = TestClient(
    app=app,
    base_url='http://localhost/configuration'
)


class TestConfigurationEndpoint(unittest.TestCase):

    def setUp(self):
        self.open_patch = mock.patch('builtins.open')
        self.json_dump_patch = mock.patch('json.dump')

        self.mock_open = self.open_patch.start()
        self.mock_json_dump = self.json_dump_patch.start()

    def tearDown(self):
        self.json_dump_patch.stop()
        self.open_patch.stop()

    def test_get_configuration(self):
        response = CLIENT.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(Settings(**response.json()), Settings)

    def test_update_configuration(self):
        new_settings = Settings(
            logging={
                'logLevel': 'DEBUG',
                'logFile': 'test.log'
            },
            commandos={
                "allCommandos": "all_path.json",
                "supportedCommandos": "car_path.json"
            },
            connection={
                "type": "async",
                "connected": True,
                "interval": 2.0
            }
        ).to_serializable()

        response = CLIENT.post('/', json=new_settings)

        self.assertEquals(response.status_code, 200)
        self.mock_json_dump.assert_called_once()
        self.mock_open.assert_called_once()
