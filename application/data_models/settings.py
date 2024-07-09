import logging

from pydantic import BaseModel, FilePath, NewPath, field_validator


class LogSettings(BaseModel):
    logLevel: str | int
    logFile: NewPath | FilePath

    @field_validator('logLevel')
    @classmethod
    def validate_log_level(cls, level):
        return cls.log_level_to_int(level)

    def to_serializable(self):
        return {
            'logLevel': self.int_to_log_level(self.logLevel),
            'logFile': str(self.logFile)
        }

    @staticmethod
    def int_to_log_level(level: int) -> str:
        return {
            50: 'CRITICAL',
            40: 'ERROR',
            30: 'WARNING',
            20: 'INFO',
            10: 'DEBUG',
            0: 'NOTSET'
        }[level]

    @staticmethod
    def log_level_to_int(level: str) -> int:
        return {
            'CRITICAL': 50,
            'ERROR': 40,
            'WARNING': 30,
            'INFO': 20,
            'DEBUG': 10,
            'NOTSET': 0
        }[level]


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
