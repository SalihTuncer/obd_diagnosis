from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_query_manager
from application.query_manager import QueryManager
from data_models.command import OBDCommandModel

router = APIRouter()


@router.post('/sync')
async def sync_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    return JSONResponse(
        # Please careful: this is just a placeholder and has no functionality yet
        content=query_manager.sync_queries(commands),
        status_code=200
    )


@router.post('/async')
async def async_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    return JSONResponse(
        content=query_manager.async_queries(commands),
        status_code=200
    )
