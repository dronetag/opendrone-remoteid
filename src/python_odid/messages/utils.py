
from typing import TypeVar, Union


T = TypeVar("T")


def get_key_by_value(data: dict[str, T], val: T) -> Union[str, T]:
    keys = [k for k, v in data.items() if v == val]
    if keys:
        return keys[0]
    return val
