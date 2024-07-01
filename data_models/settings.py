import logging

from pydantic import BaseModel, FilePath, NewPath, field_validator


class LogSettings(BaseModel):
    logLevel: str
    logFile: NewPath | FilePath

    @field_validator('logLevel')
    @classmethod
    def validate_log_level(cls, level):
        log_levels = {
            'CRITICAL': logging.CRITICAL,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG,
            'NOTSET': logging.NOTSET,
        }

        if level not in log_levels:
            raise ValueError('Invalid log level')

        return log_levels[level]


class StageSettings(BaseModel):
    name: str

    # This is a custom validator
    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if name not in ['test', 'dev', 'prod']:
            raise ValueError('Stage must be one of test, dev, prod')

        return name


class CommandosSettings(BaseModel):
    allCommandos: NewPath | FilePath
    supportedCommandos: NewPath | FilePath


class ConnectionSettings(BaseModel):
    type: str
    connected: bool
    interval: float

    @field_validator('type')
    @classmethod
    def validate_connection_type(cls, connection_type):
        if connection_type not in ['sync', 'async']:
            raise ValueError('Connection type must be one of sync, async')

        return connection_type


class Settings(BaseModel):
    logging: LogSettings
    stage: StageSettings
    commandos: CommandosSettings
    connection: ConnectionSettings
