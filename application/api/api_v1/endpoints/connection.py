from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_query_manager
from application.data_models.connection import AsyncConnection, ConnectionStatus, SyncConnection
from application.utils.query_manager import QueryManager

router = APIRouter()


@router.get('/status', response_model=ConnectionStatus)
async def get_connections(query_manager: QueryManager = Depends(get_query_manager)):
    """
        Returns the synchronous and asynchronous connection status.

        :param query_manager: The query manager
        :return The connection status
    """
    return JSONResponse(
        content=ConnectionStatus(
            sync_connection=SyncConnection(
                connected=query_manager.is_sync_connected()
            ),
            async_connection=AsyncConnection(
                connected=query_manager.is_async_connected(),
                running=query_manager.is_async_running()
            )
        ).model_dump(),
        status_code=200
    )


@router.get('/sync', response_model=SyncConnection)
async def sync_connections(
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Returns the synchronous connection status.

        :param query_manager: The query manager
        :return The synchronous connection status
    """
    return JSONResponse(
        content=SyncConnection(
            connected=query_manager.is_sync_connected()
        ).model_dump(),
        status_code=200
    )


@router.get('/async', response_model=AsyncConnection)
async def async_connections(
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Returns the asynchronous connection status.

        :param query_manager: The query manager
        :return The asynchronous connection status
    """
    return JSONResponse(
        content=AsyncConnection(
            connected=query_manager.is_async_connected(),
            running=query_manager.is_async_running()
        ).model_dump(),
        status_code=200
    )


@router.post('/sync', response_model=SyncConnection)
async def connect_sync(
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Connects synchronously.

        :param query_manager: The query manager
        :return The connection status
    """
    query_manager.connect_sync()

    return JSONResponse(
        content=SyncConnection(
            connected=query_manager.is_sync_connected()
        ).model_dump(),
        status_code=200
    )


@router.post('/async', response_model=AsyncConnection)
async def connect_async(
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Connects asynchronously.

        :param query_manager: The query manager
        :return The connection status
    """
    query_manager.connect_async()

    return JSONResponse(
        content=AsyncConnection(
            connected=query_manager.is_async_connected(),
            running=query_manager.is_async_running()
        ).model_dump(),
        status_code=200
    )
