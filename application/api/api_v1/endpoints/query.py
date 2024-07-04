from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_query_manager
from application.data_models.command import OBDCommandModel
from application.data_models.connection import AsyncConnection
from application.utils.query_manager import QueryManager

router = APIRouter()


@router.post('/sync', response_model=list[OBDCommandModel])
async def sync_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Queries the given connection for all available commands synchronously.

        :param commands: The commands to query
        :param query_manager: The query manager
        :return: The queried commands
    """
    return JSONResponse(
        content=query_manager.sync_queries(commands),
        status_code=200
    )


@router.post('/async', response_model=list[OBDCommandModel])
async def async_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Queries the given connection for all available commands asynchronously.

        :param commands: The commands to query
        :param query_manager: The query manager
        :return: The queried commands
    """
    if query_manager.is_async_running():
        return JSONResponse(
            content='An async query is already running.',
            status_code=400
        )

    return JSONResponse(
        content=query_manager.async_queries(commands),
        status_code=200
    )


@router.post('/async/stop', response_model=AsyncConnection)
async def stop_async_query(
        query_manager: QueryManager = Depends(get_query_manager)
):
    """
        Stops the current async query.

        :param query_manager: The query manager
        :return: The connection status
    """
    query_manager.stop_async()

    return JSONResponse(
        content=AsyncConnection(
            connected=query_manager.is_async_connected(),
            running=query_manager.is_async_running()
        ).model_dump(),
        status_code=200
    )
