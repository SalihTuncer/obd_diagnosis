import unittest
from unittest import mock

from fastapi.testclient import TestClient

from application.data_models.command import OBDCommandModel
from application.data_models.connection import AsyncConnection
from main import app

CLIENT = TestClient(
    app=app,
    base_url='http://localhost/query'
)


class TestQueryEndpoint(unittest.TestCase):

    def setUp(self):
        self.is_sync_connected_patch = mock.patch('obd.OBD.is_connected')
        self.is_async_connected_patch = mock.patch('obd.Async.is_connected')

        self.sync_query_patch = mock.patch('obd.OBD.query')
        self.async_watch_patch = mock.patch('obd.Async.watch')
        self.async_start_patch = mock.patch('obd.Async.start')
        self.async_stop_patch = mock.patch('obd.Async.stop')

        self.mock_is_sync_connected = self.is_sync_connected_patch.start()
        self.mock_is_async_connected = self.is_async_connected_patch.start()

        self.mock_sync_query = self.sync_query_patch.start()
        self.mock_async_watch = self.async_watch_patch.start()
        self.mock_async_start = self.async_start_patch.start()
        self.mock_async_stop = self.async_stop_patch.start()

    def test_sync_queries(self):
        cmds = [
            OBDCommandModel(**{
                "name": "RPM",
                "desc": "Engine RPM",
                "command": "010C",
                "bytes": 4,
                "ecu": 2,
                "fast": True,
                "header": "7E0"
            }).to_serializable()
        ]

        response = CLIENT.post('/sync', json=cmds)

        self.assertEquals(response.status_code, 200)
        self.mock_is_sync_connected.assert_called_once()
        self.mock_sync_query.assert_called_once()
        self.assertEquals(response.json(), cmds)

    def test_async_queries(self):
        cmds = [
            OBDCommandModel(**{
                "name": "RPM",
                "desc": "Engine RPM",
                "command": "010C",
                "bytes": 4,
                "ecu": 2,
                "fast": True,
                "header": "7E0"
            }).to_serializable()
        ]

        response = CLIENT.post('/async', json=cmds)

        self.assertEquals(response.status_code, 200)
        self.mock_is_async_connected.assert_called_once()
        self.mock_async_watch.assert_called_once()
        self.mock_async_start.assert_called_once()
        self.assertEquals(response.json(), cmds)

    def test_stop_async_query(self):
        response = CLIENT.post('/async/stop')

        self.assertEquals(response.status_code, 200)
        self.mock_async_stop.assert_called_once()
        self.assertIsInstance(AsyncConnection(**response.json()), AsyncConnection)
