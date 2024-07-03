import obd
from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api_v1.deps import get_query_manager
from application.query_manager import QueryManager

router = APIRouter()


@router.get('/status')
async def get_connections(query_manager: QueryManager = Depends(get_query_manager)):
    return JSONResponse(
        content={
            'sync connected': query_manager.is_sync_connected(),
            'async connected': query_manager.is_async_connected()
        },
        status_code=200
    )


@router.post('/sync')
async def sync_connections(
        commands: list[obd.OBDCommand],
        query_manager: QueryManager = Depends(get_query_manager)
):
    query_manager.connect_sync()

    return JSONResponse(
        content={
            'connected': query_manager.is_async_connected()
        },
        status_code=200
    )


@router.post('/async')
async def async_connections(
        commands: list[obd.OBDCommand],
        query_manager: QueryManager = Depends(get_query_manager)
):
    query_manager.connect_async()

    return JSONResponse(
        content={
            'connected': query_manager.is_async_connected()
        },
        status_code=200
    )
