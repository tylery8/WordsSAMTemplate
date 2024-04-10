from abc import ABC
from typing import Type, Any, TypeVar, Dict

from pydantic import BaseModel, ValidationError

from errors.utils import InternalServerError

T = TypeVar('T', bound='EventModel')


class EventModel(ABC, BaseModel):
    @classmethod
    def from_event(cls: Type[T], event: Dict[str, Any]) -> T:
        try:
            return cls(**event)
        except ValidationError as e:
            raise InternalServerError(InternalServerError.format_pydantic_errors(errors=e.errors()))

    def get_input_args(self):
        return self.model_dump()
