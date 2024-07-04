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

    def to_serializable(self):
        return {
            'logLevel': self.logLevel,
            'logFile': str(self.logFile)
        }


class CommandSettings(BaseModel):
    allCommandos: NewPath | FilePath
    supportedCommandos: NewPath | FilePath

    def to_serializable(self):
        return {
            'allCommandos': str(self.allCommandos),
            'supportedCommandos': str(self.supportedCommandos)
        }


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

    def to_serializable(self):
        return {
            'type': self.type,
            'connected': self.connected,
            'interval': self.interval
        }


class Settings(BaseModel):
    logging: LogSettings
    commandos: CommandSettings
    connection: ConnectionSettings

    def to_serializable(self):
        return {
            'logging': self.logging.to_serializable(),
            'commandos': self.commandos.to_serializable(),
            'connection': self.connection.to_serializable()
        }
