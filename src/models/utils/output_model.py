from abc import ABC

from pydantic import BaseModel


class OutputModel(ABC, BaseModel):
    def to_output(self) -> str:
        return self.model_dump_json()
