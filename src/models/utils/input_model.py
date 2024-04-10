from abc import ABC
from typing import Any, Type, TypeVar

from pydantic import BaseModel, ValidationError

from errors import BadRequestError
from .event_model import EventModel

T = TypeVar('T', bound='InputModel')


class InputModel(ABC, BaseModel):
    @classmethod
    def from_input(cls: Type[T], obj: Any) -> T:
        try:
            return cls(**obj)
        except ValidationError as e:
            raise BadRequestError(BadRequestError.format_pydantic_errors(errors=e.errors()))

    @classmethod
    def from_event(cls: Type[T], event: EventModel) -> T:
        return cls.from_input(event.get_input_args())
