from abc import ABC
from typing import Type, Any, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar('T', bound='ResponseModel')


class ResponseModel(ABC, BaseModel):
    @classmethod
    def from_response(cls: Type[T], obj: Any) -> Optional[T]:
        try:
            return cls(**obj)
        except:
            return None
