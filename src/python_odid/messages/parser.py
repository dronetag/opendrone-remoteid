import logging
from typing import Type

from ..message import Message, RID_VERSION

from .auth import Auth
from .system import System
from .selfid import SelfID
from .basicid import BasicID
from .location import Location
from .messagepack import MessagePack
from .operatorid import OperatorID


TYPES: dict[int, Type[Message]] = {
    BasicID.rid: BasicID,
    Location.rid: Location,
    Auth.rid: Auth,
    SelfID.rid: SelfID,
    System.rid: System,
    OperatorID.rid: OperatorID,
    MessagePack.rid: MessagePack,
}

logger = logging.getLogger("odid")


def parse(data: bytes) -> Message:
    # sanity check that the message type (half)byte agrees with `self.rid`
    parsed_type = (data[0] & 0xF0) >> 4
    if parsed_type not in TYPES:
        raise ValueError(f"Unknown message type {parsed_type}! Known {TYPES.keys()}")

    rid_version = data[0] & 0x0F  # RID version (does anyone use that?)
    if rid_version != RID_VERSION:
        logger.warning(
            f"RID version {rid_version} arrived! We support only version {RID_VERSION}"
        )

    message = TYPES[parsed_type]()
    message.parse(data[1:])
    return message
