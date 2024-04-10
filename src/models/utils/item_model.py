from abc import ABC
from typing import Any, Dict, Optional, TypeVar, Type
from uuid import uuid4

from pydantic import BaseModel

T = TypeVar('T', bound='ItemModel')


class ItemModel(ABC, BaseModel):
    def to_item(self) -> Dict[str, Any]:
        return self.model_dump(mode='json')

    @classmethod
    def from_item(cls: Type[T], item: Dict[str, Any]) -> Optional[T]:
        return cls(**item)

    @classmethod
    def generate_id(cls) -> str:
        return str(uuid4())
