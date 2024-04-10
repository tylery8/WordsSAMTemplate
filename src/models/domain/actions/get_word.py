from pydantic import Field

from models.domain import Word
from models.utils import InputModel, OutputModel


class GetWordInput(InputModel):
    id: str = Field(..., min_length=1)


class GetWordOutput(OutputModel):
    id: str
    word: str

    @classmethod
    def from_word(cls, word: Word):
        return cls(**word.model_dump())
