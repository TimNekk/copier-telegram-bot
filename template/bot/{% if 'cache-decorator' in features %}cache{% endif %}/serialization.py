from __future__ import annotations

import pickle
from abc import ABC, abstractmethod
from typing import Any

import orjson


class AbstractSerializer(ABC):

    @abstractmethod
    def serialize(self, obj: Any) -> Any:
        ...

    @abstractmethod
    def deserialize(self, obj: Any) -> Any:
        ...


class PickleSerializer(AbstractSerializer):

    def serialize(self, obj: Any) -> bytes:
        return pickle.dumps(obj)

    def deserialize(self, obj: bytes) -> Any:
        return pickle.loads(obj)  # noqa: S301


class JSONSerializer(AbstractSerializer):
    def serialize(self, obj: Any) -> bytes:
        return orjson.dumps(obj)

    def deserialize(self, obj: str) -> Any:
        return orjson.loads(obj)
