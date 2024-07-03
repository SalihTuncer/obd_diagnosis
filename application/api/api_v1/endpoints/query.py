from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_query_manager
from application.data_models.command import OBDCommandModel
from application.utils.query_manager import QueryManager

router = APIRouter()


@router.post('/sync')
async def sync_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    # TODO: Return proper responses instead of None.

    return JSONResponse(
        content=query_manager.sync_queries(commands),
        status_code=200
    )


@router.post('/async')
async def async_queries(
        commands: list[OBDCommandModel],
        query_manager: QueryManager = Depends(get_query_manager)
):
    # TODO: Return proper responses instead of None as well as non-blocking sleeps.

    return JSONResponse(
        content=query_manager.async_queries(commands),
        status_code=200
    )
