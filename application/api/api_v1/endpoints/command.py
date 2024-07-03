from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_command_helper, get_configuration
from application.data_models.settings import Settings
from application.utils.command_helper import CommandHelper

router = APIRouter()


@router.get("/supported")
async def get_supported_commands(
        command_helper: CommandHelper = Depends(get_command_helper),
        settings: Settings = Depends(get_configuration)
):
    # TODO: Instead of saving all supported commands at the beginning of the application, do it here or in another call.

    return JSONResponse(
        content=command_helper.get_commands_from_file(settings.commandos.supportedCommandos),
        status_code=200
    )


@router.get("/all")
async def get_all_commands(
        command_helper: CommandHelper = Depends(get_command_helper),
        settings: Settings = Depends(get_configuration)
):
    return JSONResponse(
        content=command_helper.get_commands_from_file(settings.commandos.allCommandos),
        status_code=200
    )
