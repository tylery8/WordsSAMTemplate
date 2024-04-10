from typing import Optional

from pydantic import Field, model_validator

from models.domain import Word
from models.utils import InputModel, OutputModel


class CreateWordInput(InputModel):
    word: Optional[str] = Field(None, min_length=3, max_length=20)
    length: Optional[int] = Field(None, ge=3, le=20)

    @model_validator(mode='after')
    def validate_data(self):
        if self.word and self.length and self.length != len(self.word):
            raise ValueError("The given word does not match the given length")


class CreateWordOutput(OutputModel):
    id: str
    word: str

    @classmethod
    def from_word(cls, word: Word):
        return cls(**word.model_dump())
