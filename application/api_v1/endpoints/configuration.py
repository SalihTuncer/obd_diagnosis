from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api_v1.deps import get_configuration
from data_models.settings import Settings

router = APIRouter()


@router.get("/")
async def get_configuration(settings: Settings = Depends(get_configuration)):
    return JSONResponse(
        content=settings.model_dump(),
        status_code=200
    )
