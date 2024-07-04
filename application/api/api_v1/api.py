from fastapi import APIRouter

from application.api.api_v1.endpoints import command, configuration, connection, query

api_v1_router = APIRouter()
api_v1_router.include_router(command.router, prefix="/command", tags=['command'])
api_v1_router.include_router(query.router, prefix="/query", tags=['query'])
api_v1_router.include_router(connection.router, prefix="/connection", tags=['connection'])
api_v1_router.include_router(configuration.router, prefix="/configuration", tags=['configuration'])
