from fastapi import APIRouter

from application.api_v1.endpoints import commands, configuration, connection, queries

api_v1_router = APIRouter()
api_v1_router.include_router(commands.router, prefix="/command", tags=['command'])
api_v1_router.include_router(queries.router, prefix="/query", tags=['query'])
api_v1_router.include_router(connection.router, prefix="/connection", tags=['connection'])
api_v1_router.include_router(configuration.router, prefix="/configuration", tags=['configuration'])
