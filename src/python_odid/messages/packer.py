from ..message import Message, RID_VERSION


def pack(message: Message) -> bytes:
    type_nibble = (message.rid << 4) & 0xF0
    version_nibble = RID_VERSION & 0x0F
    header = (type_nibble | version_nibble).to_bytes(1, "little")
    return header + message.pack()
