from typing import Optional

import obd
from obd import ECU
from obd.protocols import ECU_HEADER
from pydantic import BaseModel, Field


class OBDCommandModel(BaseModel):
    name: str
    desc: str
    command: bytes
    bytes_: int = Field(alias='bytes')
    decoder: any = lambda x: x
    ecu: int = ECU.ALL
    fast: bool = False
    header: bytes = ECU_HEADER.ENGINE

    class Config:
        arbitrary_types_allowed = True

    def to_obd_command(self) -> obd.OBDCommand:
        return obd.OBDCommand(
            name=self.name,
            desc=self.desc,
            command=self.command,
            _bytes=self.bytes_,
            decoder=self.decoder,
            ecu=self.ecu,
            fast=self.fast,
            header=self.header
        )

    @classmethod
    def from_obd_command(cls, obd_command: obd.OBDCommand):
        return cls(
            name=obd_command.name,
            desc=obd_command.desc,
            command=obd_command.command,
            bytes=obd_command.bytes,
            decoder=obd_command.decode,
            ecu=obd_command.ecu,
            fast=obd_command.fast,
            header=obd_command.header
        )

    def to_serializable(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'command': self.command.decode('utf-8'),
            'bytes': self.bytes_,
            'ecu': self.ecu,
            'fast': self.fast,
            'header': self.header.decode('utf-8')
        }


class OBDCommandsModel(BaseModel):
    mode_0: Optional[list[OBDCommandModel]]
    mode_1: Optional[list[OBDCommandModel]]
    mode_2: Optional[list[OBDCommandModel]]
    mode_3: Optional[list[OBDCommandModel]]
    mode_4: Optional[list[OBDCommandModel]]
    mode_5: Optional[list[OBDCommandModel]]
    mode_6: Optional[list[OBDCommandModel]]
    mode_7: Optional[list[OBDCommandModel]]
    mode_8: Optional[list[OBDCommandModel]]
    mode_9: Optional[list[OBDCommandModel]]
