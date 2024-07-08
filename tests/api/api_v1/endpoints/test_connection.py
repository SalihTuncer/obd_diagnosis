import unittest
from unittest import mock

from fastapi.testclient import TestClient

from application.data_models.connection import ConnectionStatus, SyncConnection, AsyncConnection
from main import app

CLIENT = TestClient(
    app=app,
    base_url="http://localhost/connection"
)


class TestConnectionEndpoint(unittest.TestCase):

    def setUp(self):
        base_url = 'application.utils.query_manager.QueryManager'

        self.sync_conn = mock.patch(f'{base_url}.connect_sync')
        self.async_conn = mock.patch(f'{base_url}.connect_async')

        self.mock_sync_conn = self.sync_conn.start()
        self.mock_async_conn = self.async_conn.start()

    def tearDown(self):
        self.sync_conn.stop()
        self.async_conn.stop()

    def test_get_connections_status(self):
        response = CLIENT.get("/status")

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(ConnectionStatus(**response.json()), ConnectionStatus)

    def test_get_sync_connections_status(self):
        response = CLIENT.get("/sync")

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(SyncConnection(**response.json()), SyncConnection)

    def test_get_async_connections_status(self):
        response = CLIENT.get("/async")

        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(AsyncConnection(**response.json()), AsyncConnection)

    def test_connect_sync(self):
        response = CLIENT.post("/sync")

        self.assertEquals(response.status_code, 200)
        self.mock_sync_conn.assert_called_once()

    def test_connect_async(self):
        response = CLIENT.post("/async")

        self.assertEquals(response.status_code, 200)
        self.mock_async_conn.assert_called_once()
