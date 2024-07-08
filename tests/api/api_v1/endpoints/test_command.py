import unittest

from starlette.testclient import TestClient

from application.data_models.command import OBDCommandsModel
from main import app

CLIENT = TestClient(
    app=app,
    base_url='http://localhost/command'
)


class TestCommandEndpoint(unittest.TestCase):

    def test_get_supported_commands(self):
        response = CLIENT.get('/supported')

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(OBDCommandsModel(**response.json()), OBDCommandsModel)

    def test_get_all_commands(self):
        response = CLIENT.get('/all')

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(OBDCommandsModel(**response.json()), OBDCommandsModel)
