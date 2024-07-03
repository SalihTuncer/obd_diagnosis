from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_query_manager
from application.query_manager import QueryManager

router = APIRouter()


@router.get('/')
async def get_queries(query_manager: QueryManager = Depends(get_query_manager)):
    return JSONResponse(
        content={'some': 'queries'},
        status_code=200
    )


@router.post('/sync')
async def sync_queries(query_manager: QueryManager = Depends(get_query_manager)):
    return JSONResponse(
        # Please careful: this is just a placeholder and has no functionality yet
        content=query_manager.sync_queries(),
        status_code=200
    )


@router.post('/async')
async def async_queries(query_manager: QueryManager = Depends(get_query_manager)):
    return JSONResponse(
        # Please careful: this is just a placeholder and has no functionality yet
        query_manager.async_queries(),
        status_code=200
    )
