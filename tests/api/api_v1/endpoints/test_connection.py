from unittest import mock

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(
    app=app,
    base_url="http://localhost/connection"
)


class ConnectMock:
    def __init__(self, sync_mock: mock.Mock, async_mock: mock.Mock):
        self.sync_mock = sync_mock
        self.async_mock = async_mock


def test_get_connections_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "sync_connection" in response.json()
    assert "async_connection" in response.json()


def test_get_sync_connections_status():
    response = client.get("/sync")
    assert response.status_code == 200
    assert "connected" in response.json()


def test_get_async_connections_status():
    response = client.get("/async")
    assert response.status_code == 200
    assert "connected" in response.json()
    assert "running" in response.json()


@pytest.fixture
def mock_connect() -> ConnectMock:
    base_path = 'application.utils.query_manager.QueryManager'

    with mock.patch(f'{base_path}.connect_sync') as sync_connect_mock:
        with mock.patch(f'{base_path}.connect_async') as async_connect_mock:
            yield ConnectMock(
                sync_connect_mock,
                async_connect_mock
            )


def test_connect_sync(mock_connect: ConnectMock):
    response = client.post("/sync")
    assert response.status_code == 200
    mock_connect.sync_mock.assert_called_once()


def test_connect_async(mock_connect: ConnectMock):
    response = client.post("/async")
    assert response.status_code == 200
    mock_connect.async_mock.assert_called_once()
