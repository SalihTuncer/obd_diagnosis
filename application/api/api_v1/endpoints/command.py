from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from application.api.deps import get_command_helper, get_configuration
from application.data_models.command import OBDCommandsModel
from application.data_models.settings import Settings
from application.utils.command_helper import CommandHelper
from application.utils.query_manager import QueryManager

router = APIRouter()


@router.get("/supported", response_model=OBDCommandsModel)
async def get_supported_commands(
        command_helper: CommandHelper = Depends(get_command_helper),
        query_manager: QueryManager = Depends(get_command_helper),
        settings: Settings = Depends(get_configuration)
):
    """
        Returns all supported commands.

        :param command_helper: The command helper
        :param query_manager: The query manager
        :param settings: The settings
        :return The supported commands
    """
    if not command_helper.are_supported_commands_saved():
        command_helper.save_all_supported_commands(connection=query_manager.sync_conn)

    return JSONResponse(
        content=command_helper.get_commands_from_file(settings.commandos.supportedCommandos),
        status_code=200
    )


@router.get("/all", response_model=OBDCommandsModel)
async def get_all_commands(
        command_helper: CommandHelper = Depends(get_command_helper),
        settings: Settings = Depends(get_configuration)
):
    """
        Returns all commands.

        :param command_helper: The command helper
        :param settings: The settings
        :return All commands
    """
    return JSONResponse(
        content=command_helper.get_commands_from_file(settings.commandos.allCommandos),
        status_code=200
    )
