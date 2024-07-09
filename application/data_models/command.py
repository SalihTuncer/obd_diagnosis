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
    decode: any = None
    ecu: int = ECU.ALL
    fast: bool = False
    header: bytes = ECU_HEADER.ENGINE

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, name: str, desc: str, command: bytes, bytes: int, ecu: int, fast: bool, header: bytes,
                 decode: any = None):
        super().__init__(name=name, desc=desc, command=command, bytes=bytes, ecu=ecu, fast=fast, header=header,
                         decode=decode)

        self.assign_decoder()

    def __eq__(self, other: obd.OBDCommand):
        if not isinstance(other, obd.OBDCommand):
            return False

        return self.name == other.name and self.desc == other.desc and self.command == other.command and \
            self.bytes_ == other.bytes and self.ecu == other.ecu and self.fast == other.fast and \
            self.header == other.header

    def to_obd_command(self) -> obd.OBDCommand:
        return obd.OBDCommand(
            name=self.name,
            desc=self.desc,
            command=self.command,
            _bytes=self.bytes_,
            decoder=self.decode,
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
            decode=obd_command.decode,
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

    def assign_decoder(self) -> None:
        for mode in obd.commands.modes:

            cmd: obd.OBDCommand
            for cmd in mode:

                if self == cmd:
                    self.decode = cmd.decode
                    return

        obd.logger.warning('Decoder not found for command: %s', self.name)


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
