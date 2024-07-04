from pydantic import BaseModel


class SyncConnection(BaseModel):
    connected: bool


class AsyncConnection(BaseModel):
    connected: bool
    running: bool


class ConnectionStatus(BaseModel):
    sync_connection: SyncConnection
    async_connection: AsyncConnection
