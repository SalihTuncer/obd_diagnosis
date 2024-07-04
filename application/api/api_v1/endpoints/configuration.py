from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_configuration
from application.data_models.settings import Settings

router = APIRouter()


@router.get("/", response_model=Settings)
async def get_configuration(settings: Settings = Depends(get_configuration)):
    """
        Returns the current configuration.

        :param settings: The settings
        :return The configuration
    """
    return JSONResponse(
        content=settings.to_serializable(),
        status_code=200
    )
